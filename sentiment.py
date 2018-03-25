# import Google language libraries
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json

# Instantiates a client
client = language.LanguageServiceClient()

with open('usanews.txt') as f:
    articles = f.read().splitlines()

# usa_sent = open('usa_sentiment.txt', 'w')
# usa_mag = open('usa_magnitude.txt', 'w')


# For each article in the entire list of articles
for article in articles:
    # The text to analyze
    document = types.Document(content=article, type=enums.Document.Type.PLAIN_TEXT)

    # We send to the Google API to then analyze our text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # Voilà!
    print('Text: {}'.format(article))
    print('Sentiment value: {}'.format(sentiment.score))


#     usa_sent.write(str(sentiment.score) + '\n')
#     usa_mag.write(str(sentiment.magnitude) + '\n')
#
# usa_sent.close()
# usa_mag.close()
