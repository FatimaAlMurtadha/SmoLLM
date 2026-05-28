from app.chain.steps import PromptBuilder
from app.schemas import PromptInput

# This test checks the functionality of the PromptBuilder class
# which is responsible for constructing a prompt based on the provided dataset statistics and user question. 
# The test creates an instance of PromptBuilder, constructs a PromptInput with a sample question and dataset statistics, and then invokes the builder to generate a prompt. 
# Finally, it asserts that the generated prompt contains the expected question and statistics.
def test_prompt_builder():

    builder = PromptBuilder()

    data = PromptInput(
        question="What is the average score?",
        stats={"Final_Score": {"mean": 85}}
    )

    result = builder.invoke(data)

    assert "average score" in result.prompt.lower()
    assert "85" in result.prompt