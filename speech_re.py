import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

def voice_t_text():
    # Capture audio from the microphone
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    # Recognize speech using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio)
        print (text)
        return text
    except sr.UnknownValueError:
        return ("Please say again")
    except sr.RequestError as e:
        return ("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ =='__main__':
    itaration_counter=0
    max_iter=3
    while True:
        try:
            # Call the function
            voice_t_text()
            itaration_counter +=1
            if itaration_counter >=max_iter:
                iteration_count = 0
                # Explicitly release the microphone resource
                #recognizer.__exit__()
        except TimeoutError:
            print("The function took too long to execute (more than 2 seconds).")

