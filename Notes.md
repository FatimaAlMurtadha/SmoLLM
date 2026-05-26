uv init
git init

source .venv/Scripts/activate
uv run main.py
uv add transformers
from transformers import pipline


# coding train youtube evaluationary algorithem - genaric algorithem

uv add torch

uv add pydantic

uv run fastapi dev main.py