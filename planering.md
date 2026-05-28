# smollm2-135-instruct:
## 1. pipeline("text-generation)
## 2. model = "HuggingFacsTB/SmolLM2-135M-Instruct

# Runnable pattern
- Runnable[I,O]
- or 
- RunnableSequence
- RunnableLambda


# Pytest
- TestClient
- monkeypatch
- assert

# Typing + Pydantic

# AI Safty Concepts 
- toxicity
- bias
- hallucinations
- prompt injection
- risk levels

# 1. GET/health
# 2. data - upload - CSV 
# 3. DS describe, ...
# 4. PromptBuilder (input "question, stats" - output "prompt string")
# 5. LLMRunner 
# 6. ResponseParser


Question
   ↓
PromptBuilder
   ↓
SmolLM
   ↓
ResponseParser
   ↓
JSON Answer


server actions	= behavior
file uploads =	debugging
AI questions =	monitoring
errors	= robustness
model failures	= observability



