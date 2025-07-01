import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for i, voice in enumerate(voices):
    print(f"🔊 {i}: Trying voice - {voice.name} ({voice.id})")
    engine.setProperty('voice', voice.id)
    engine.say(f"This is voice number {i}. My name is {voice.name}. Do you like how I sound?")
    engine.runAndWait()
    time.sleep(0.5)
