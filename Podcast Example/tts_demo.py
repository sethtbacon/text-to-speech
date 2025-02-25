import os
import openai
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
import argparse  # added for argument parsing

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
azure_api_key = os.getenv("AZURE_API_KEY")
azure_region = os.getenv("AZURE_REGION")

# Added argument parsing to select endpoint
parser = argparse.ArgumentParser(description="TTS demo script")
parser.add_argument('--endpoint', choices=['azure', 'openai'], default='openai', help="Select TTS endpoint")
parser.add_argument('--voice', default='en-US-AriaNeural', help="Select Azure TTS voice")  # added voice option
parser.add_argument('--voice-oai', default='nova', help="Select OpenAI TTS voice")  # added OpenAI voice option
args = parser.parse_args()
selected_endpoint = args.endpoint
selected_voice = args.voice

with open("text_to_convert.txt", "r") as f:
    text_to_speak = f.read()

if selected_endpoint == "azure":
    if azure_api_key and azure_region:
        # Configure Azure TTS with provided API key and region
        speech_config = speechsdk.SpeechConfig(subscription=azure_api_key, region=azure_region)
        speech_config.speech_synthesis_voice_name = selected_voice  # set chosen voice
        # Save speech output to a file
        audio_config = speechsdk.audio.AudioConfig(filename="output_azure.mp3")
        # Create a SpeechSynthesizer instance for Azure TTS
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        # Generate speech and wait for completion
        result = synthesizer.speak_text_async(text_to_speak).get()
        # Print a confirmation message
        print(f"Azure TTS using voice '{selected_voice}' has saved audio to output_azure.mp3")
    else:
        print("Azure environment variables are not set.")
        exit(1)
else:
    # Fallback to OpenAI TTS
    response = openai.audio.speech.create(
        model="tts-1",
        voice=args.openai_voice,  # use chosen OpenAI voice
        input=text_to_speak,
        response_format="mp3"
    )

    # Save the generated audio to a file
    with open("output.mp3", "wb") as audio_file:
        audio_file.write(response.content)

    print(f"OpenAI TTS using voice '{args.openai_voice}' has saved audio to output.mp3")
