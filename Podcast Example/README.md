# OpenAI & Azure TTS Demo in GitHub Codespaces

This project demonstrates how to use Text-to-Speech (TTS) APIs from OpenAI and Azure within GitHub Codespaces. The demo includes a Python script that converts text into speech and saves the output as an audio file.

## Features

- **Text-to-Speech Conversion:** Generate speech audio from text using either OpenAI's or Azure's TTS API.
- **Customizable Voices:** Select from multiple voices for each endpoint.
- **GitHub Codespaces Ready:** Preconfigured for a seamless development experience in GitHub Codespaces.
- **Environment Management:** Securely load your API keys using environment variables.

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

## Setup

### 1. Clone the Repository in GitHub Codespaces

- Open your repository in GitHub and click the **Code** button.
- Select the **Codespaces** tab and create a new Codespace.

### 2. Create a `.env` File

In the root directory, create a file named `.env` and add your API keys:

```env
OPENAI_API_KEY=your-openai-api-key
AZURE_API_KEY=your-azure-api-key
AZURE_REGION=your-azure-region
```

### 3. Install Dependencies

Navigate to the project directory and install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Running the TTS Demo

Run the Python script with your preferred endpoint and voice options:

For OpenAI TTS:
```bash
python tts_demo.py --endpoint openai --voice-oai nova
```

For Azure TTS (example):
```bash
python tts_demo.py --endpoint azure --voice en-US-AriaNeural
```

After execution, you should see an audio file (either `output.mp3` for OpenAI or `output_azure.mp3` for Azure) in your repository.

## Additional References

- [OpenAI TTS API Documentation](https://platform.openai.com/docs/guides/text-to-speech)
- [Azure Speech Service Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/)
- [GitHub Codespaces Documentation](https://docs.github.com/en/codespaces)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

## License

This project is for educational purposes. Please adhere to OpenAI's and Azure's usage policies when using their services.

## Acknowledgments

- OpenAI and Azure for their TTS services.
- Contributors to GitHub Codespaces documentation.
