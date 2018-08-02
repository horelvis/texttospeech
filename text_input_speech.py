# Google's CLOUD TEXT-TO-SPEECH https://cloud.google.com/text-to-speech/

from google.cloud import texttospeech
import os

# auth setup https://cloud.google.com/docs/authentication/getting-started
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/Users/horelvis/git/speech-to-text-google/sanny-a84f639cfb00.json'

# Instantiates client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(
    ssml="<speak> <emphasis >¡Hi!</emphasis> <break time=\"400ms\"/> My name is Sonny, <break time=\"200ms\"/> ¿How can I help you ? </speak>")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(language_code='en-US', ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('text_output_speech.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
