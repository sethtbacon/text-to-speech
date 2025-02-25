import os
import azure.cognitiveservices.speech as speechsdk

azure_api_key = os.getenv("AZURE_API_KEY")
azure_region = os.getenv("AZURE_REGION")

if azure_api_key and azure_region:
    try:
        speech_config = speechsdk.SpeechConfig(subscription=azure_api_key, region=azure_region)
        print("Azure configuration is working: SpeechConfig created successfully.")
    except Exception as e:
        print("Failed to create Azure SpeechConfig:", e)
else:
    print("Azure environment variables are not set.")
