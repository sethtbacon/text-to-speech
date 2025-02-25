import os

# Check if the environment variables are injected
if os.getenv("OPENAI_API_KEY"):
    print("OpenAI API key is set.")
else:
    print("OpenAI API key is NOT set.")

if os.getenv("AZURE_API_KEY"):
    print("Azure API key is set.")
else:
    print("Azure API key is NOT set.")

if os.getenv("AZURE_REGION"):
    print("Azure region is set.")
else:
    print("Azure region is NOT set.")