import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Read the dataset
data = pd.read_csv('modul.10/iris.csv')

# Split the dataset
x = data.drop('species', axis=1)
y = data['species']

# Standardize the dataset
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Split the dataset into training and testing
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

# Train the model
model_svm = SVC()
model_svm.fit(x_train, y_train)

# Predict the test set
y_pred = model_svm.predict(x_test)

# Output results
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=data['species'].unique(), yticklabels=data['species'].unique())
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

# Pair plot for visualizing feature relationships
sns.pairplot(data, hue='species', markers=["o", "s", "D"])
plt.show()
