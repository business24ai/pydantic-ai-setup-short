from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# define the model
model = OpenAIModel("gpt-4o")

# define the agent
agent = Agent(
    model=model,
    system_prompt="Be concise, reply with one sentence.",
)

# run the agent
result = agent.run_sync("What does AGI mean?")

# print the result
print("\n=== Data ===")
print(result.data)

# print the Usage
print("\n=== usage ===")
print(result.usage())

# print the Messages
print("\n=== messages ===")
print(result.all_messages())
