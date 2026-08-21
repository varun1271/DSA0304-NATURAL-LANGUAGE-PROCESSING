from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)

prompt = input("Enter a prompt: ")

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print("\nGenerated Text:\n")
print(response.output_text)