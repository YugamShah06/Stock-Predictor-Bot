import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the data
def load_data():
    scraped_data = pd.read_csv('cleaned_messages.csv')
    preprocessed_data = pd.read_csv('messages_with_sentiment.csv')
    analysis_data = pd.read_csv('sentiment_analysis_output.csv')
    return scraped_data, preprocessed_data, analysis_data

# Prepare the dataset for training
def prepare_data(preprocessed_data, analysis_data):
    # Merge the preprocessed messages with analysis data
    df = pd.merge(preprocessed_data, analysis_data[['cleaned_message', 'sentiment']], on='cleaned_message', how='left')
    
    # Create stock movement labels (1 for positive sentiment, 0 for negative sentiment)
    df['stock_movement'] = df['sentiment'].apply(lambda x: 1 if x > 0 else 0)
    
    # Features and target variable
    X = df['sentiment'].values.reshape(-1, 1)  # Features
    y = df['stock_movement'].values  # Target variable
    return X, y

# Train the model
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f'Model accuracy: {accuracy:.2f}')
    return model

# Save the model
def save_model(model):
    joblib.dump(model, 'stock_predictor_model.pkl')
    print('Model saved successfully!')

# Main function
if __name__ == "__main__":
    scraped_data, preprocessed_data, analysis_data = load_data()
    X, y = prepare_data(preprocessed_data, analysis_data)
    model = train_model(X, y)
    save_model(model)
