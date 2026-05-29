from app.chain.steps import (
    PromptBuilder,
    LLMRunner,
    ResponseParser
)

# The oracle_chain is a sequential processing chain that combines the PromptBuilder, LLMRunner, and ResponseParser steps. 
# This chain takes an input, processes it through each step in order, and produces a final output. 
# The PromptBuilder constructs a prompt based on the dataset statistics and user question, the LLMRunner generates a response using the language model, and the ResponseParser extracts a clean answer from the generated text. 
# This modular design allows for clear separation of concerns and easy maintenance of each individual step in the processing pipeline.

oracle_chain = (
    PromptBuilder(name="prompt_builder")
    | LLMRunner(name="llm_runner")
    | ResponseParser(name="response_parser")
)