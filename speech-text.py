import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    while True:
        # Capture audio from the microphone
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            # Use the recognizer to convert speech to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            
            # Check if the user wants to exit
            if text.lower() == "stop":
                print("Press 1 again to exit.")
                break
                
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

if __name__ == "__main__":
    print("Say 'stop' to exit.")
    speech_to_text()
