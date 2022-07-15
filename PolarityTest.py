from textblob import TextBlob

def analize_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity 

textTest = "My experience in Brazil was terrific"

print("")
print(textTest)
print("")
print(f"polarity: {analize_sentiment(textTest)}")
print("")
