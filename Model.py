import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset with sentiment analysis
df = pd.read_csv('messages_with_sentiment.csv')

# Ensure the 'sentiment' column exists
if 'sentiment' not in df.columns:
    raise KeyError("The 'sentiment' column does not exist. Run the sentiment analysis first.")

# Create 'stock_movement' column based on sentiment values
df['stock_movement'] = df['sentiment'].apply(lambda x: 1 if x > 0 else 0)

# Features (X) and labels (y)
X = df[['sentiment']]  # You can add more features here
y = df['stock_movement']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model (e.g., RandomForest)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")
