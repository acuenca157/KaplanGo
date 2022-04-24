import speech_recognition as sr


recognizer = sr.Recognizer()

with sr.Microphone() as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language="es-ES")
    print(text)