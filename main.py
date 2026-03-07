import pyttsx3
import speech_recognition as sr
import ollama
import time
import webbrowser

def speak(text):
    print(f"Dura:{text}")
    engine=pyttsx3.init()
    engine.stop()
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)
    
def agent_llama(user_input):
    try:
        print(f"Sending to Llama: {user_input}") # Debug line
        
        response = ollama.chat(
            model='llama3.2:1b', 
            messages=[
                {'role': 'system', 'content': 'You are Dura a man , reponse to me as a friend whenever you are called'},
                {'role': 'user', 'content': user_input},
                ],
                keep_alive="30m"
            )
        
        # pulls the text out of the Ollama response object
        answer = response['message']['content']
        return answer

    except Exception as e:
        print(f"Ollama Error: {e}")
        return "I am having trouble connecting to my brain."
    
if __name__=="__main__":
    speak("initializing dura....")
    r=sr.Recognizer()
    r.pause_threshold = 0.6 # stops listening quickly after seaking is finish
    while True:
        reply=""
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening..")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source,phrase_time_limit=5)
                
            word= r.recognize_google(audio,language='en-in').lower()
            print(f"you say {word}")
            
            if "dura" in word.lower():
                user_input = word.replace("dura", "").strip()
                if user_input:
                    reply = agent_llama(user_input)
                else:
                    reply=" Yes? "
                    
            if "goodbye dura" in word or "stop" in word:
                        speak("Shutting down. Goodbye!")
                        break
        except sr.UnknownValueError:
            continue 
        except Exception as e:
            print(f"Notice: {e}")
            continue
        if reply:
            speak(reply)
            
            