import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load your preprocessed data
df = pd.read_csv('cleaned_messages.csv')

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define a function to handle NaN and apply sentiment analysis
def analyze_sentiment(msg):
    if isinstance(msg, str):  # Check if the message is a string
        return analyzer.polarity_scores(msg)['compound']
    else:
        return 0.0  # Neutral sentiment for empty or non-string entries

# Apply the sentiment analysis function to the 'cleaned_message' column
df['sentiment'] = df['cleaned_message'].apply(analyze_sentiment)

# Save the updated DataFrame to a new CSV file
df.to_csv('messages_with_sentiment.csv', index=False)

print("Sentiment analysis completed. File saved as 'messages_with_sentiment.csv'.")
