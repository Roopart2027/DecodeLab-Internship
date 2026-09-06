from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()

# Input data
X = iris.data

# Output data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create AI model
model = DecisionTreeClassifier()

# Train AI
model.fit(X_train, y_train)

# Test AI
prediction = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, prediction)

print("AI Data Classification Project")
print("--------------------------------")
print("Number of training data:", len(X_train))
print("Number of testing data:", len(X_test))
print("Accuracy:", accuracy * 100, "%")

# Test a new flower
new_flower = [[5.1, 3.5, 1.4, 0.2]]

result = model.predict(new_flower)

print("Predicted flower:", iris.target_names[result[0]])