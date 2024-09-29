import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load your preprocessed data
df = pd.read_csv('cleaned_messages.csv')

# Check if 'stock_movement' exists
print("Columns in DataFrame:", df.columns)

# If 'stock_movement' doesn't exist, create it (Example: based on sentiment)
if 'stock_movement' not in df.columns:
    # Create a stock movement based on some logic, e.g., sentiment > 0.5 means positive movement
    df['stock_movement'] = df['sentiment'].apply(lambda x: 1 if x > 0 else 0)

# Features (assuming you have numerical features like sentiment, volume, etc.)
X = df[['sentiment']]  # Modify this to include other features if you have them
y = df['stock_movement']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple RandomForest classifier (you can use any other model as well)
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Evaluate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy}")

# Save the model results to a CSV (optional)
df['predicted_movement'] = clf.predict(X)
df.to_csv('model_output.csv', index=False)
