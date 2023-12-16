import speech_recognition as sr

class CustomMicrophone(sr.Microphone):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()

# Initialize the recognizer with the custom microphone class
recognizer = sr.Recognizer()

def voice_to_text():
    # Capture audio from the microphone
    with CustomMicrophone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)  # Set a timeout value for listening (in seconds)
            text = recognizer.recognize_google(audio)
            print(text)
            return text
        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ =='__main__':
    iteration_count = 0
    max_iterations = 4

    while True:
        try:
            # Call the function
            voice_to_text()
            iteration_count += 1
            if iteration_count >= max_iterations:
                iteration_count = 0
                # Explicitly release the microphone resource
                recognizer.__exit__(None, None, None)
        except TimeoutError:
            print("The function took too long to execute (more than 2 seconds).")
