# user_msg = input("Enter your messgae : ").lower()
# greet_msgs = ["hi","hello","hey","hi there","hello there"]
# if user_msg == "hi" or user_msg == "hello" or user_msg == "hey":
#     print("hell0")
# else:
#     print("I cannt understand")
import webbrowser
from datetime import datetime
import requests
# yha pr api se location ka data le rhe hain phir weather ka data le rhe hain using location data 
#hota kaise hain answer ye hain ki pehle hum ip-api se location ka data le rhe hain fir us location ke hisab se weather api se weather ka data le rhe hain
#Phir us data ko print kar rhe hain
# url2 = "https://ip-api.com/json"
# response2 = requests.get(url2)
# data2 = response2.json()
# #print(data2)
z

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = requests.get(url)    
    news_data = response.json()
    articles = news_data["articles"]
    for i in range(len(articles)):
        print(articles[i]['title']) 
news_articles = ["breaking news","latest news","news headlines","news"]
greet_msgs = ["hi","hello","hey","hi there","hello there"]
date_msgs = ["date","current date","today",]
time_msgs = ["current time","time","now"]
web = ["facebook","google","amazon","chatgpt"]
chat = True
while chat:
    user_msg = input("Enter your messgae : ").lower()

    if user_msg in greet_msgs:
        print("hell0")

    elif user_msg in web:
        if user_msg == "facebook":
            webbrowser.open("https://www.facebook.com")
        elif user_msg == "amazon":
            webbrowser.open("https://www.amazon.com")   
        elif user_msg == "chatgpt":
            webbrowser.open("https://chat.openai.com")
        elif user_msg == "google":  
            webbrowser.open("https://www.google.com")
    elif user_msg in date_msgs:
        print(f"TOday's date is  : {datetime.now().date()}")

    elif user_msg in time_msgs:
        currentime = datetime.now().time()
        print("time is:",current_time.strftime("%I:%M:%S %p"))

    # elif user_msg == "open":
    #     site = user_msg.split()[-1]
    #     webbrowser.open(f"https://www.{site}.com")

    elif "calculate" in user_msg:
        expression = user_msg.split("calculate")[-1]
        result = eval(expression)
        print("The result is:",result)

    elif user_msg in news_articles:
        print("Here are the latest news headlines:")
        get_news()
        # for i, article in enumerate(articles[:5], start=1):
        #     print(f"{i}. {article['title']}")
        
    elif user_msg =="bye":
        print("bye")
        chat = False
    elif user_msg =="breakup news":
        print("Shivam hua ek saal phale bhot bada breakup jisse shivam move on nhi ho para hain")

    else:
        print("I cannt understand")