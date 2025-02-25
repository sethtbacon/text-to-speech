# OpenAI & Azure TTS Demo in GitHub Codespaces

This project demonstrates how to convert text to speech using the TTS APIs from OpenAI and Azure. It has been reworked to provide a streamlined development experience in GitHub Codespaces with a modern file structure and improved diagnostics.

## Project Structure

- **tts_demo.py**: Main Python script that reads text from `text_to_convert.txt` and generates speech audio.
  - For **OpenAI TTS**, the script outputs `output.mp3`.
  - For **Azure TTS**, the script outputs `output_azure.mp3`.
- **text_to_convert.txt**: Contains the text to convert into speech.
- **.env**: Environment file (should contain your API keys and region) that is loaded via Codespaces secrets.
- **requirements.txt**: Lists the Python dependencies.
- **.devcontainer/**: Contains the `devcontainer.json` for setting up your Codespace.
- **diagnostics/**: Contains scripts for verifying environment variable injection and Azure configuration (`validate_env.py` and `validate_azure.py`).
- **.gitignore**: Ensures that generated audio files, environment files, and cache directories are not committed.

## Features

- **Dual TTS Endpoints:** Easily switch between OpenAI and Azure TTS using command-line options.
- **Customizable Voices:** Select voices using the command-line arguments (`--voice` for Azure, `--voice-oai` for OpenAI).
- **Diagnostics Tools:** Validate your environment setup with the scripts in the `diagnostics` folder.
- **GitHub Codespaces Ready:** Preconfigured with a `devcontainer` for a seamless VSCode experience in Codespaces.

## Available Voices

### OpenAI TTS Voices
- nova
- shimmer
- echo
- onyx
- fable
- alloy
- ash
- sage
- coral

### Azure TTS Voices (Examples)
- en-US-AriaNeural
- en-US-GuyNeural
- en-US-JennyNeural
- en-GB-LibbyNeural
- en-AU-CatherineNeural
- (See [Azure Voice Fonts Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/voice-fonts) for a full list)

## Prerequisites

- Python 3.8 or higher.
- An [OpenAI API key](https://platform.openai.com/account/api-keys).
- An [Azure Speech Service API key](https://portal.azure.com) and region if using Azure TTS.
- GitHub Codespaces or local Docker environment supporting the devcontainer configuration.

## Setup

1. **Clone the Repository in GitHub Codespaces**
   - Open your repository in GitHub, click the **Code** button, and select the **Codespaces** tab to create a new Codespace.

2. **Configure API Keys**
   - In the root directory, create a file named `.env` (or use Codespaces secrets) with the following content:
     ```env
     OPENAI_API_KEY=your-openai-api-key
     AZURE_API_KEY=your-azure-api-key
     AZURE_REGION=your-azure-region
     ```

3. **Install Dependencies**
   - Open a terminal in the project root and run:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run Diagnostics (Optional)**
   - Validate that your environment variables are correctly injected:
     ```bash
     python diagnostics/validate_env.py
     python diagnostics/validate_azure.py
     ```

5. **Running the TTS Demo**
   - For **OpenAI TTS**:
     ```bash
     python tts_demo.py --endpoint openai --voice-oai nova
     ```
   - For **Azure TTS**:
     ```bash
     python tts_demo.py --endpoint azure --voice en-US-AriaNeural
     ```

After running the script, check the output audio file (either `output.mp3` or `output_azure.mp3`) using your preferred media player.

## Additional Resources

- [OpenAI TTS API Documentation](https://platform.openai.com/docs/guides/text-to-speech)
- [Azure Speech Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/)
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

## License

This project is provided for educational purposes only. Please adhere to the usage policies of OpenAI and Azure when using their services.

## Acknowledgments

- Thanks to OpenAI and Azure for their TTS services.
- Special thanks to the GitHub Codespaces team for providing an excellent development environment.
