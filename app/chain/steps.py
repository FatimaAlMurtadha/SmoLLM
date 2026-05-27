from app.chain.runnable import Runnable
from app.schemas import (
    PromptInput,
    PromptOutput,
    LLMOutput,
    ParsedAnswer,
)

# The PromptBuilder class is a specific implementation of the Runnable interface that takes a PromptInput and produces a PromptOutput. The invoke method constructs a prompt string based on the provided dataset statistics and user question, following a specific format that instructs the AI to use only the provided data to answer the question. If the answer cannot be determined from the data, it instructs the AI to respond with "Not enough information." The generated prompt is then returned as a PromptOutput object.
class PromptBuilder(Runnable[PromptInput, PromptOutput]):

# The invoke method constructs a prompt string using the provided dataset statistics and user question. It follows a specific format that instructs the AI to use only the provided data to answer the question, and to respond with "Not enough information." if the answer cannot be determined from the data. The generated prompt is returned as a PromptOutput object.
    def invoke(self, data: PromptInput) -> PromptOutput:

# The prompt string is constructed using a multi-line f-string that incorporates the dataset statistics and user question from the PromptInput. The prompt instructs the AI to be a strict data analyst, to use only the provided dataset statistics, and to answer briefly and clearly. If the answer cannot be determined from the data, it explicitly tells the AI to respond with "Not enough information."
        prompt = f"""
You are a strict data analyst AI.

Use ONLY the provided dataset statistics.

If the answer cannot be determined from the data,
say: "Not enough information."

Dataset statistics:
{data.stats}

User question:
{data.question}

Answer briefly and clearly.
"""
# The generated prompt is returned as a PromptOutput object, which can be used in subsequent steps of the processing chain, such as sending it to a language model for generating an answer.
        return PromptOutput(prompt=prompt)