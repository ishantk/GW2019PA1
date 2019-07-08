from gtts import gTTS
tts = gTTS('Hello', lang='en')
tts.save('hello.mp3')
print(">> File Created")