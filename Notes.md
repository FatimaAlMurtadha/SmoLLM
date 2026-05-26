uv init
git init
touch .gitignore

source .venv/Scripts/activate
uv run main.py
uv add transformers
uv add "fastapi[standard]"
from transformers import pipline

uv add torch

uv add pydantic

uv run fastapi dev main.py










# coding train youtube evaluationary algorithem - genaric algorithem