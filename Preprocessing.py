import pandas as pd
import spacy
import re

# Load the spaCy English language model
nlp = spacy.load('en_core_web_sm')

# Function to clean and preprocess text
def clean_message(message):
    # Convert the message to a string if it’s not already one
    if not isinstance(message, str):
        return ''
    message = re.sub(r'http\S+|www\S+|https\S+', '', message, flags=re.MULTILINE)  # Remove URLs
    message = re.sub(r'\@w+|\#','', message)  # Remove @mentions and hashtags
    message = re.sub(r'[^A-Za-z0-9\s]+', '', message)  # Remove special characters and digits
    message = message.lower()  # Convert to lowercase
    return message

# Load your CSV file with messages
df = pd.read_csv('telegram_messages.csv')  # Update with your actual CSV file path

# Fill NaN values and ensure the column is string type
df['message'] = df['message'].fillna('').astype(str)

# Apply the cleaning function
df['cleaned_message'] = df['message'].apply(clean_message)


# Save the cleaned data to a new CSV file
df.to_csv('cleaned_messages.csv', index=False)

print("Preprocessing complete. Cleaned messages saved to 'cleaned_messages.csv'.")
