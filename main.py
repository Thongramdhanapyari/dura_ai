import pyttsx3
import speech_recognition as sr
import ollama
import time
import webbrowser
import wikipedia
import psutil
import requests
import feedparser

engine=pyttsx3.init()

def speak(text):
    print(f"Dura:{text}")
    engine.stop()
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)
    
# wikipedia files
def get_wikipedia(query):
    try:
        result = wikipedia.summary(query,sentences=2)
        return result
    except Exception:
        return "I could not find a specfic entry for that,but I can search Google for you."
    
#system stats
def get_system_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    return f"CPU is at {cpu} percent and memory usage is at {ram} percent."
    
#weather
def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.20&current_weather=true"
    try:
        response = requests.get(url).json()
        temp = response['current_weather']['temperature']
        return f"The current temperature is {temp} degrees celsius."
    except Exception as e:
        return "I couldn't reach the weather satellite."
    

def get_news():
    # Using Google News RSS feed for "India"
    rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    try:
        feed = feedparser.parse(rss_url)
        headlines = []
        # Get the top 3 headlines
        for entry in feed.entries[:3]:
            headlines.append(entry.title)
        
        return "Here are the top stories. " + " ... ".join(headlines)
    except Exception:
        return "I'm having trouble reading the news feeds right now."
    
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
            
            if "goodbye dura" in word or "stop" in word:
                speak("Shutting down. Goodbye!")
                break
            if "dura" in word.lower():
                user_input = word.replace("hey dura", "").strip()
                if not user_input:
                    speak("yes?")
                    
                elif "who is" in user_input or "what is" in user_input:
                    topic = user_input.replace("who is", "").replace("what is", "").strip()
                    speak(get_wikipedia(topic))
                    
                elif "system status" in user_input or "performance" in user_input:
                    speak(get_system_stats())
                    
                elif "news" in user_input or "headlines" in user_input:
                    headlines = get_news()
                    speak(headlines)
                    
                elif "weather" in user_input:
                    report = get_weather()
                    speak(report)
                    
                else:
                    reply=agent_llama(user_input)
                    speak(reply)
        except sr.UnknownValueError:
            continue 
        except Exception as e:
            print(f"Notice: {e}")
            continue
            
            