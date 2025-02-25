import os
import openai
import azure.cognitiveservices.speech as speechsdk
import argparse
import sys

def get_api_keys():
    """Retrieve API keys and region from environment variables."""
    return {
        "openai_key": os.getenv("OPENAI_API_KEY"),
        "azure_key": os.getenv("AZURE_API_KEY"),
        "azure_region": os.getenv("AZURE_REGION")
    }

def synthesize_azure(text_to_speak, voice, azure_key, azure_region):
    """Synthesize speech using Azure TTS."""
    if not (azure_key and azure_region):
        print("Azure environment variables are not set.")
        sys.exit(1)
    speech_config = speechsdk.SpeechConfig(subscription=azure_key, region=azure_region)
    speech_config.speech_synthesis_voice_name = voice
    audio_config = speechsdk.audio.AudioConfig(filename="output_azure.mp3")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    result = synthesizer.speak_text_async(text_to_speak).get()
    print("Azure synthesis result:", result.reason)
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Azure TTS using voice '{voice}' has saved audio to output_azure.mp3")
    else:
        error_message = getattr(result, "error_details", "No error details available")
        print("Azure TTS synthesis error:", error_message)

def synthesize_openai(text_to_speak, voice_oai):
    """Synthesize speech using OpenAI TTS."""
    response = openai.audio.speech.create(
        model="tts-1",
        voice=voice_oai,
        input=text_to_speak,
        response_format="mp3"
    )
    with open("output.mp3", "wb") as audio_file:
        audio_file.write(response.content)
    print(f"OpenAI TTS using voice '{voice_oai}' has saved audio to output.mp3")

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="TTS demo script")
    parser.add_argument('--endpoint', choices=['azure', 'openai'], default='openai', help="Select TTS endpoint")
    parser.add_argument('--voice', default='en-US-AriaNeural', help="Select Azure TTS voice")
    parser.add_argument('--voice-oai', default='nova', help="Select OpenAI TTS voice")
    return parser.parse_args()

def main():
    keys = get_api_keys()
    openai.api_key = keys["openai_key"]
    args = parse_arguments()
    
    # Read text to synthesize
    with open("text_to_convert.txt", "r") as f:
        text_to_speak = f.read()
    
    if args.endpoint == "azure":
        synthesize_azure(text_to_speak, args.voice, keys["azure_key"], keys["azure_region"])
    else:
        synthesize_openai(text_to_speak, args.voice_oai)

if __name__ == "__main__":
    main()
