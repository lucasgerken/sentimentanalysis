from tkinter import *
from tkinter import ttk
import tkinter
import numpy as np
import pandas as pd
import tweepy
import matplotlib as plt
import seaborn as sns
import textblob
from IPython.display import display
from textblob import TextBlob
import re

# Dados da API Twitter
CONSUMER_KEY = '<INSERT YOUR KEY>'
CONSUMER_SECRET = '<INSERT YOUR KEY>'

# Access Twitter:
ACCESS_TOKEN = '<INSERT YOUR KEY>'
ACCESS_SECRET = '<INSERT YOUR KEY>'

# Max Tweets Retrive
MAX_TWEETS = 50

SEPARATOR = "\n-----------------------------------------------------------------------\n"

# API setup:

def twitter_setup():
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    # Retorna a api autenticada:
    api = tweepy.API(auth)
    return api

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|       (\w+:\/\/\S+)", " ", tweet).split())

def analize_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
       return 1
    elif analysis.sentiment.polarity == 0:
       return 0
    else:
        return -1

def search_tweets(text_search):
    # Start Extractor
    extractor = twitter_setup()

    # Extração dos tweets
    tweets = extractor.search_tweets(q=text_search,count=MAX_TWEETS,lang="en")

    print("Number of tweets extracted: {}.\n".format(len(tweets)))

    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

    data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])

    pos_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] > 0]
    neu_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] == 0]
    neg_tweets = [ tweet for index, tweet in enumerate(data['Tweets']) if data['SA'][index] < 0]

    # Printando as porcentagens:
    lbl_positive_text.set("{:.2f}".format(len(pos_tweets)*100/len(data['Tweets']))+'%')
    lbl_neutral_text.set("{:.2f}".format(len(neu_tweets)*100/len(data['Tweets']))+'%')
    lbl_negative_text.set("{:.2f}".format(len(neg_tweets)*100/len(data['Tweets']))+'%')

    # Populando Tweets

    tx_positive = ""
    tx_neutral = ""
    tx_negative = ""

    for index, tweet in enumerate(data['Tweets']):
        if (data['SA'][index] > 0):
            tx_positive += data['Tweets'][index]+SEPARATOR
        if (data['SA'][index] == 0):
            tx_neutral += data['Tweets'][index]+SEPARATOR
        if (data['SA'][index] < 0):
            tx_negative += data['Tweets'][index]+SEPARATOR

    enPositive.delete('1.0',END)
    enPositive.insert("end-1c",tx_positive)

    enNeutral.delete('1.0',END)
    enNeutral.insert("end-1c",tx_neutral)

    enNegative.delete('1.0',END)
    enNegative.insert("end-1c",tx_negative)


def command_search():
    lbl_positive_text.set('0.00%')
    lbl_neutral_text.set('0.00%')
    lbl_negative_text.set('0.00%')

    search_tweets(str(en_search_text.get()))

# Start TK

root = Tk()

root.title("Sentiment Analysis")

# Resilze Window -------------------------------------------------------------

window_width = 640
window_height = 480

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Frame -----------------------------------------------------------------------

frameTop = Frame(root)
frameTop.place(x=10,y=10,width=620,height=40)

en_search_text = tkinter.StringVar()

enSearch = ttk.Entry(frameTop,textvariable=en_search_text)
enSearch.place(x=0,y=0,width=530,height=25)

btPesquisar = ttk.Button(frameTop,text='Search',command=command_search)
btPesquisar.place(x=540,y=0,width=80,height=25)

separator1 = ttk.Separator(frameTop, orient='horizontal')
separator1.place(x=0,y=38,width=620)

# Frame Tweets

frameMidle = Frame(root)
frameMidle.place(x=10,y=60,width=620,height=400)

notebook = ttk.Notebook(frameMidle)
notebook.place(x=0,y=0)

# Tab Positive

frPositive = ttk.Frame(notebook, width=615, height=300)
frPositive.pack(fill='both', expand=True)

enPositive = tkinter.Text(frPositive, width=50,height=10)
enPositive.place(x=10,y=10,width=575,height=280)

scPositive = tkinter.Scrollbar(frPositive, width=40)
scPositive.place(x=585,y=10,width=20,height=280)

scPositive.config(command=enPositive.yview)
enPositive.configure(yscrollcommand=scPositive.set)

notebook.add(frPositive, text='Positive Tweets')

# Tab Neutral

frNeutral = ttk.Frame(notebook, width=615, height=300)
frNeutral.pack(fill='both', expand=True)

text_neutral = tkinter.StringVar()

enNeutral = tkinter.Text(frNeutral, width=50,height=10)
enNeutral.place(x=10,y=10,width=575,height=280)

scNeutral = tkinter.Scrollbar(frNeutral, width=40)
scNeutral.place(x=585,y=10,width=20,height=280)

scNeutral.config(command=enNeutral.yview)
enNeutral.configure(yscrollcommand=scNeutral.set)

notebook.add(frNeutral, text='Neutral Tweets')

# Tab Negative

frNegative = ttk.Frame(notebook, width=615, height=300)
frNegative.pack(fill='both', expand=True)

enNegative = tkinter.Text(frNegative, width=50,height=10)
enNegative.place(x=10,y=10,width=575,height=280)

scNegative = tkinter.Scrollbar(frNegative, width=40)
scNegative.place(x=585,y=10,width=20,height=280)

scNegative.config(command=enNegative.yview)
enNegative.configure(yscrollcommand=scNegative.set)

notebook.add(frNegative, text='Negative Tweets')

# Frame Result

frameResult = Frame(root)
frameResult.place(x=10,y=400,width=640,height=80)

separator1 = ttk.Separator(frameResult, orient='horizontal')
separator1.place(x=0,y=0,width=620)

#

lfPositive = ttk.LabelFrame(frameResult, text=' % Positive Tweets: ')
lfPositive.place(x=0,y=10,width=200,height=60) 

lbl_positive_text=tkinter.StringVar()

lblPositive = ttk.Label(lfPositive,text='0.00%',font=("Arial", 25),textvariable=lbl_positive_text,foreground='green')
lblPositive.pack()

lbl_positive_text.set('0.00%')

#

lfNeutral = ttk.LabelFrame(frameResult, text=' % Neutral Tweets: ')
lfNeutral.place(x=210,y=10,width=200,height=60) 

lbl_neutral_text=tkinter.StringVar()

lfNeutral = ttk.Label(lfNeutral,text='00.0%',font=("Arial", 25),textvariable=lbl_neutral_text,foreground='orange')
lfNeutral.pack()

lbl_neutral_text.set('0.00%')

#

lfNegative = ttk.LabelFrame(frameResult, text=' % Negative Tweets: ')
lfNegative.place(x=420,y=10,width=200,height=60) 

lbl_negative_text=tkinter.StringVar()

lfNegative = ttk.Label(lfNegative,text='00.0%',font=("Arial", 25),textvariable=lbl_negative_text,foreground='red')
lfNegative.pack()

lbl_negative_text.set('0.00%')

root.mainloop()
