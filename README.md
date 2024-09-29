
# Stock Movement Prediction using Sentiment Analysis

This project aims to predict stock movements based on sentiment analysis of messages from social media platforms like Telegram. The process involves scraping messages, preprocessing the text, performing sentiment analysis, and training a machine learning model to predict stock movements.

## Project Structure

1. **Data Scraping and Cleaning:**
   - Scrapes messages from Telegram using `Telethon`.
   - Cleans and preprocesses the messages, removing URLs, special characters, and irrelevant text.

2. **Sentiment Analysis:**
   - Applies VADER sentiment analysis to the preprocessed messages to determine the sentiment score of each message.
   - Creates a new column with sentiment scores in the range [-1, 1].

3. **Stock Movement Prediction:**
   - Creates a binary classification label `stock_movement` based on sentiment (1 for positive, 0 for neutral/negative).
   - Trains a Random Forest classifier to predict stock movements based on the sentiment.

4. **Model Saving:**
   - After training, the model is saved as a `stock_predictor_model.pkl` file using `joblib` for future use.

## Files in the Project

- **cleaned_messages.csv**: Contains preprocessed messages after cleaning.
- **messages_with_sentiment.csv**: Contains messages with corresponding sentiment scores.
- **sentiment_analysis_output.csv**: Contains sentiment analysis results, which are merged with the preprocessed messages.
- **stock_predictor_model.pkl**: The trained Random Forest model for predicting stock movements.

## How to Use the Code

1. **Data Loading:** 
   - Load the preprocessed and sentiment-analyzed data from CSV files.

2. **Data Preparation:**
   - Merge the preprocessed messages with sentiment analysis output to create the final dataset.
   - Create a binary target variable `stock_movement` based on sentiment scores.

3. **Model Training:**
   - Train a Random Forest model using sentiment as the feature.
   - Split the data into training and testing sets for evaluation.

4. **Model Saving:**
   - Save the trained model to a file for later use.

### Example Usage

```python
# Load data
scraped_data, preprocessed_data, analysis_data = load_data()

# Prepare data for model training
X, y = prepare_data(preprocessed_data, analysis_data)

# Train the model
model = train_model(X, y)

# Save the trained model
save_model(model)
```

## Dependencies

To run this project, you will need the following Python packages:

- `pandas`: For data manipulation and analysis.
- `spacy`: For natural language processing tasks.
- `telethon`: For scraping messages from Telegram.
- `vaderSentiment`: For sentiment analysis.
- `scikit-learn`: For machine learning tasks.
- `joblib`: For saving the trained model.

## Setup Requirements

1. **Python Environment**: Ensure you have Python 3.6 or higher installed on your system.
2. **Install Required Packages**: You can install the required packages using pip. Run the following command in your terminal:

```bash
pip install pandas spacy telethon vaderSentiment scikit-learn joblib
```

3. **Download spaCy Model**: After installing spaCy, you need to download the English language model. Run the following command:

```bash
python -m spacy download en_core_web_sm
```

## Notes

- You may need to modify the code if you wish to use additional features or a different model for stock prediction.
- Ensure you have the necessary API keys and credentials to scrape data from Telegram.
