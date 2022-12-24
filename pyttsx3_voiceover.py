import pyttsx3

# Create an instance of the pyttsx3.init class
engine = pyttsx3.init()

# Set the text and voice parameters
text = "Hello, this is a generated voiceover. I can speak in different accents and languages, and I can also add pauses for emphasis."

# Generate audio demos with different styles

# Demo 1: Male voice, slower speed, higher pitch, and emphasis on "different accents and languages"
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
# engine.setProperty('voice', 'english-us+f1')  # Use the male voice "english-us+f1"
engine.setProperty('rate', 145)  # Slow down the speaking rate
engine.say(text)

# Save the audio to a file
# engine.save_to_file(text, 'demo1.mp3')

# Demo 2: Female voice, faster speed, lower pitch, and emphasis on "Python"
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
# engine.setProperty('voice', 'english-us')  # Use the female voice "english-us"
engine.setProperty('rate', 175)  # Increase the speaking rate
engine.say(text)

# Save the audio to a file
# engine.save_to_file(text, 'demo2.mp3')

# Demo 3: Neutral voice, normal speed, normal pitch, and pauses for emphasis
engine.setProperty('voice', 'english-us')  # Use the neutral voice "english-us"
engine.setProperty('rate', 150)  # Set the speaking rate to the default value
engine.say(text)

# Save the audio to a file
# engine.save_to_file(text, 'demo3.mp3')

# Run the voiceovers
engine.runAndWait()
