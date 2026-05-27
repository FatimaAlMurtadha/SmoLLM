# Runnable, RunnableLambda, RunnableSequence (från llm.py)
from pydantic import BaseModel, ConfigDict, SerializeAsAny
from typing import Generic, TypeVar, Any, Callable

# Type variables for input, output, and intermediate types
I = TypeVar("I")
O = TypeVar("O")
M = TypeVar("M")


# A Runnable is a callable object that can be invoked with some input data to produce an output.
class Runnable(BaseModel, Generic[I, O]):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str | None = None

# The invoke method must be implemented by subclasses to define how the Runnable processes input data to produce output.
    def invoke(self, data: I) -> O:
        raise NotImplementedError()

# The __or__ method allows chaining Runnables together using the | operator. If the other object is a Runnable, it creates a RunnableSequence. If the other object is a callable, it wraps it in a RunnableLambda and then creates a RunnableSequence.
    def __or__(self, other: Any):
        if isinstance(other, Runnable):
            return RunnableSequence.model_construct(first=self, second=other)

        if callable(other):
            return RunnableSequence.model_construct(
                first=self,
                second=RunnableLambda.model_construct(func=other, name=other.__name__)
            )

        return NotImplemented

# The __ror__ method allows chaining Runnables together in reverse order using the | operator. If the other object is a callable, it wraps it in a RunnableLambda and then creates a RunnableSequence with the current Runnable as the second part of the sequence.
    def __ror__(self, other: Any):
        if callable(other):
            return RunnableSequence.model_construct(
                first=RunnableLambda.model_construct(func=other),
                second=self
            )

        return NotImplemented

# RunnableLambda is a simple implementation of Runnable that wraps a callable function. The invoke method simply calls the wrapped function with the input data.
class RunnableLambda(Runnable[I, O]):
    func: Callable[[I], O]

# The invoke method calls the wrapped function with the provided input data and returns the result.
    def invoke(self, data: I) -> O:
        return self.func(data)

# RunnableSequence is an implementation of Runnable that represents a sequence of two Runnables. The invoke method first invokes the first Runnable with the input data, then takes the output and passes it to the second Runnable, returning the final output.
class RunnableSequence(Runnable[I, O], Generic[I, M, O]):
    first: SerializeAsAny[Runnable[I, M]]
    second: SerializeAsAny[Runnable[M, O]]

# The invoke method processes the input data through the first Runnable to get an intermediate result, which is then passed to the second Runnable to produce the final output.
    def invoke(self, data: I) -> O:
        return self.second.invoke(self.first.invoke(data))