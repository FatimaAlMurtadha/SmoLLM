from app.chain.steps import PromptBuilder, ResponseParser
from app.schemas import PromptInput, LLMOutput

def test_prompt_builder():

    builder = PromptBuilder(name="prompt_builder")

    data = PromptInput(
        question="What is the average score?",
        stats={"Final_Score": {"mean": 85}}
    )

    result = builder.invoke(data)
    prompt = result.prompt.lower()

    # the answer to the question is included in the prompt
    assert "what is the average score" in prompt

    # The column name is included in the prompt
    assert "final_score" in prompt

    # The dataset statistics are included in the prompt
    assert "mean" in prompt
    assert "85" in prompt

    assert "use only the provided dataset statistics" in prompt
    assert "not enough information" in prompt


def test_response_parser_basic():
    parser = ResponseParser(name="response_parser")

    output = LLMOutput(raw_text="The average is 85")
    result = parser.invoke(output)

    assert result.answer == "The average is 85"


def test_response_parser_removes_prefixes():
    parser = ResponseParser()

    output = LLMOutput(raw_text="Answer: 85")
    result = parser.invoke(output)

    assert result.answer == "85"

def test_response_parser_removes_quotes():
    parser = ResponseParser()

    output = LLMOutput(raw_text='"85"')
    result = parser.invoke(output)

    assert result.answer == "85"

# The response parser should be able to handle answers that are wrapped in multiple layers of quotes and prefixes, and still extract the clean answer.
def test_response_parser_empty_lines():
    parser = ResponseParser()

    output = LLMOutput(raw_text="\n\n  85  \n\n")
    result = parser.invoke(output)

    assert result.answer == "85"


# If the LLM output is empty or only contains whitespace, the response parser should return a default message indicating that no answer was generated.
def test_response_parser_no_content():
    parser = ResponseParser()

    output = LLMOutput(raw_text="   \n   ")
    result = parser.invoke(output)

    assert result.answer == "No answer generated."