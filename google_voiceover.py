from gtts import gTTS

# text to convert to speech
text = "Hello, this is a voiceover generated using Python. I can speak in different accents and languages, and I can also add pauses for emphasis."

# create the audio file with slower speed
audio1 = gTTS(text, lang="en", slow=True)
audio1.save("voiceover1.mp3")

# create the audio file with faster speed
audio2 = gTTS(text, lang="en", slow=False)
audio2.save("voiceover2.mp3")

# create the audio file with default speed
audio3 = gTTS(text, lang="en")
audio3.save("voiceover3.mp3")
