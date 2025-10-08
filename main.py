import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, function_tool

import mlflow

mlflow.set_tracking_uri("http://localhost:8080")
mlflow.set_experiment("experiment number 1 for my agent")
mlflow.openai.autolog()

# gemini_api_key = ""

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1",
)

set_tracing_disabled(disabled=True)

# @function_tool
# def add_number(num1: int, numb2:int):
#     return num1 + numb2

async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="manager",
        instructions="you are a panaversity project manager",
        model=OpenAIChatCompletionsModel(model="gemma3:1b", openai_client=client),
    )

    result = await Runner.run(
        agent,
        "who are you?",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())