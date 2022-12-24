import google.auth
from google.cloud import texttospeech

# Set up authentication
credentials, project_id = google.auth.default()

# Create a client
client = texttospeech.TextToSpeechClient(credentials=credentials)

# Set the text and voice parameters
synthesis_input = texttospeech.types.SynthesisInput(text="Hello, this is a voiceover generated using Python.")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL,
    pitch=1.5  # Increase the pitch of the generated speech
)

# Set the audio format
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3
)

# Perform the text-to-speech request
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# Save the response to an MP3 file
with open('voiceover.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio content written to file "voiceover.mp3"')
