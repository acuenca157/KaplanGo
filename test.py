import speech_recognition as sr

recognizer = sr.Recognizer()

activation = "glados"

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s.lower()

with sr.Microphone() as source:
    while 1:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="es-ES")
            text = normalize(text)

            if(activation in text):
                print("Si amo")

                audio = recognizer.listen(source)
                order = recognizer.recognize_google(audio, language="es-ES")
                order = normalize(order)
                print(order)
            else:
                print(text)
        except:
            print("Silecio, sigo esperando")
