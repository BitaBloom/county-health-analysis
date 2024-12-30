
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
file_path = "data/data.xlsx"
sheet_name = 'Outcomes & Factors Rankings'
data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=1)

# Rename columns appropriately
data.columns = [
    'FIPS', 'State', 'County', '# of Ranked Counties',
    'Health Outcomes Rank', 'Health Outcomes Quartile',
    'Health Factors Rank', 'Health Factors Quartile'
]

# Convert relevant columns to numeric types
numeric_columns = [
    'Health Outcomes Rank', 'Health Outcomes Quartile',
    'Health Factors Rank', 'Health Factors Quartile'
]
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Drop rows with non-numeric values in numeric columns
data.dropna(subset=numeric_columns, inplace=True)

# Verify data types and values
print("\nData types after conversion:")
print(data.dtypes)
print("\nSample data after cleaning:")
print(data[numeric_columns].head())

# Select relevant features and target variable
features = ['Health Outcomes Quartile', 'Health Factors Rank', 'Health Factors Quartile']
target = 'Health Outcomes Rank'  # Example target variable

# Verify selected columns
print("\nSelected features and target:")
print(data[features + [target]].head())

# Data preprocessing
X = data[features]
y = data[target]

# Exploratory Data Analysis (EDA)
# Descriptive statistics
print("\nDescriptive statistics:")
print(data.describe())

# Plotting
# Correlation heatmap (select only numeric columns)
plt.figure(figsize=(10, 8))
correlation_matrix = data[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Pairplot for feature relationships (handle potential issues)
try:
    sns.pairplot(data[features + [target]])
    plt.suptitle("Pairplot for Features and Target", y=1.02)
    plt.show()
except ValueError as e:
    print(f"Error in pairplot: {e}")

# Model Training and Evaluation
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'\nMean Squared Error: {mse}')

# Visualization of results
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()
