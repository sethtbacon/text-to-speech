import os
import openai
import azure.cognitiveservices.speech as speechsdk
import argparse

def main():
    # Set API keys from environment variables
    openai.api_key = os.getenv("OPENAI_API_KEY")
    azure_api_key = os.getenv("AZURE_API_KEY")
    azure_region = os.getenv("AZURE_REGION")
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="TTS demo script")
    parser.add_argument('--endpoint', choices=['azure', 'openai'], default='openai', help="Select TTS endpoint")
    parser.add_argument('--voice', default='en-US-AriaNeural', help="Select Azure TTS voice")
    parser.add_argument('--voice-oai', default='nova', help="Select OpenAI TTS voice")
    args = parser.parse_args()
    
    # Read text from file
    with open("text_to_convert.txt", "r") as f:
        text_to_speak = f.read()
    
    if args.endpoint == "azure":
        if not (azure_api_key and azure_region):
            print("Azure environment variables are not set.")
            exit(1)
        # Configure Azure TTS settings
        speech_config = speechsdk.SpeechConfig(subscription=azure_api_key, region=azure_region)
        speech_config.speech_synthesis_voice_name = args.voice
        audio_config = speechsdk.audio.AudioConfig(filename="output_azure.mp3")
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        
        # Generate speech and log result details
        result = synthesizer.speak_text_async(text_to_speak).get()
        print("Azure synthesis result:", result.reason)
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"Azure TTS using voice '{args.voice}' has saved audio to output_azure.mp3")
        else:
            error_message = getattr(result, "error_details", "No error details available")
            print("Azure TTS synthesis error:", error_message)
    else:
        # Fallback to OpenAI TTS
        response = openai.audio.speech.create(
            model="tts-1",
            voice=args.voice_oai,
            input=text_to_speak,
            response_format="mp3"
        )
        with open("output.mp3", "wb") as audio_file:
            audio_file.write(response.content)
        print(f"OpenAI TTS using voice '{args.voice_oai}' has saved audio to output.mp3")

if __name__ == "__main__":
    main()
