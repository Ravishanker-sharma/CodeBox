import speech_recognition as sr
listener = sr.Recognizer()
def listen_to_microphone():
    try:

      with sr.Microphone() as source:
          print("listening...")
          voice = listener.listen(source)
          command = listener.recognize_google(voice)
          command = command.lower()
          if  'alexa' in command:
               print(command)

    except sr.UnknownValueError:
        print("can not understand")
        pass

listen_to_microphone()