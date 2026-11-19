from openai import AzureOpenAI
endpoint = "https://project5635632-resource.services.ai.azure.com/api/projects/project5635632"
api_key = "G8XxpQn3oWmCohY1Q61HadKnAUJwYtSR1wUUiQ3IuWgL1jemyoquJQQJ99CKACF24PCXJ3w3AAAAACOGBzUX"
deployment_name = "gpt-5-mini"
# 4. Use AzureOpenAI client with Azure AI Studio Project API version
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-06-01"
)

# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "user", "content": "What is the capital of India?"}
    ]
)
print(response.choices[0].message.content)
