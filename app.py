import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Initialize FastAPI
app = FastAPI()

# Initialize OpenAI-compatible client (for Ollama)
client = AsyncOpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1",
)

# Disable tracing if using custom framework
set_tracing_disabled(disabled=True)

# Request schema
class ChatRequest(BaseModel):
    prompt: str

# Response schema
class ChatResponse(BaseModel):
    output: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    agent = Agent(
        name="manager",
        instructions="you are a panaversity project manager",
        model=OpenAIChatCompletionsModel(model="gemma3:1b", openai_client=client),
    )

    result = await Runner.run(agent, req.prompt)
    return ChatResponse(output=result.final_output)

@app.get("/")
def root():
    return {"message": "Agent API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
