# 🚗 Car Price Predictor

A desktop machine learning application that predicts the estimated market price of a used car based on its technical and historical information.

The project combines **Python, Tkinter, Pandas, NumPy, and Scikit-learn** to provide a simple graphical interface where users can enter vehicle information and receive an estimated price.

---

## 📌 Project Overview

**Car Price Predictor** is a machine learning project designed to estimate the price of a used vehicle using several important vehicle features.

The application provides a graphical user interface (GUI) where the user enters:

- 🚗 Mileage
- ⚙️ Engine size
- 💥 Number of accidents
- 🔧 Technical condition score
- 📅 Manufacturing year

After entering the information, the trained machine learning model predicts the estimated price of the vehicle in **USD**.

The application also displays the model's evaluation metrics, including:

- MAE
- MSE
- RMSE

---

## ✨ Features

- 🧠 Machine learning-based price prediction
- 📊 Linear Regression model
- 🖥️ Modern Tkinter graphical interface
- 🚗 Used-car price estimation
- 📈 Model performance evaluation
- 💵 Price displayed in USD
- 🔄 Ability to return to the input page and make another prediction
- ⚠️ Input validation for invalid numerical values
- 📋 Displays the entered vehicle information alongside the prediction

---

## 🖼️ Application Screenshots

### Input Page

The first page allows the user to enter the vehicle's information before making a prediction.

![Car Price Predictor Input](Screenshot%202026-08-29%20173028.png)

---

### Prediction Result

After clicking **Predict Price**, the application displays the estimated vehicle price together with the model's performance metrics and the entered vehicle information.

![Car Price Predictor Result](Screenshot%202026-08-29%20173034.png)

---

## 🧠 Machine Learning Model

The project uses **Linear Regression** from the `scikit-learn` library.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train, y_train)
```

Linear Regression is a supervised machine learning algorithm used to model the relationship between input variables and a continuous target value.

In this project, the target value is the vehicle's price.

### Target Variable

```text
Price_USD
```

The model attempts to learn the relationship between the vehicle features and its price.

---

## 📊 Dataset

The machine learning model uses an Excel dataset:

```text
project1_used_car_data.xlsx
```

The dataset contains information about used vehicles.

### Input Features

| Feature | Description | Example |
|---|---|---:|
| `Mileage_km` | Total distance driven by the vehicle | 50000 |
| `Engine_L` | Engine size in liters | 1.6 |
| `Accident_Count` | Number of recorded accidents | 0 |
| `Technical_Score` | Technical condition score | 8.5 |
| `Year` | Vehicle manufacturing year | 2022 |

### Target

| Column | Description |
|---|---|
| `Price_USD` | Vehicle price in US dollars |

---

## 🔢 Number of Data Samples

The dataset contains approximately:

**80,000 vehicle records**

These records are used to train and evaluate the machine learning model.

> **Note:** The Python source code itself does not hard-code the number of rows. It loads the Excel file directly using Pandas, so the actual number of records depends on the contents of `project1_used_car_data.xlsx`.

---

## 🧪 Training and Testing

The dataset is divided into two parts:

- **70% → Training data**
- **30% → Testing data**

The split is performed using `train_test_split`:

```python
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.3,
    random_state=42
)
```

### Why split the dataset?

The training data is used to teach the model the relationship between vehicle features and price.

The testing data is kept separate and is used to evaluate how well the trained model performs on data it did not use during training.

The `random_state=42` value makes the split reproducible.

---

## 🔄 Machine Learning Workflow

The project follows this general workflow:

```text
Excel Dataset
     │
     ▼
Load Data with Pandas
     │
     ▼
Select Features
     │
     ▼
Select Target (Price_USD)
     │
     ▼
Train / Test Split
     │
     ├───────────────┐
     ▼               ▼
Training Data    Testing Data
     │
     ▼
Linear Regression
     │
     ▼
Train Model
     │
     ▼
Make Predictions
     │
     ▼
Calculate MAE / MSE / RMSE
     │
     ▼
Tkinter GUI
     │
     ▼
Estimated Car Price
```

---

## 📐 Evaluation Metrics

The model is evaluated using three common regression metrics:

- **MAE — Mean Absolute Error**
- **MSE — Mean Squared Error**
- **RMSE — Root Mean Squared Error**

These metrics are calculated after the model predicts the prices of the test data.

```python

MAE = mean_absolute_error(y_test, y_pred)

MSE = mean_squared_error(y_test, y_pred)

RMSE = np.sqrt(MSE)

```

---

## 📊 Metric Formulas

### 1. MAE — Mean Absolute Error

MAE represents the average absolute difference between the actual values and predicted values.

### Formula

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

Where:

- \(n\) = number of test samples
- \(y_i\) = actual price
- \(\hat{y}_i\) = predicted price

A smaller MAE means that, on average, predictions are closer to the actual prices.

---

### 2. MSE — Mean Squared Error

MSE calculates the average squared difference between actual and predicted values.

### Formula

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Because the errors are squared, larger errors have a greater effect on the final value.

---

### 3. RMSE — Root Mean Squared Error

RMSE is the square root of MSE.

### Formula

$$
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

RMSE is expressed in the same unit as the target variable.

Since the target variable is the vehicle price in USD, RMSE is also expressed in USD.

---

## 📋 Evaluation Metrics Summary

| Metric | Full Name | Formula | Unit | Interpretation |
|---|---|---|---|---|
| **MAE** | Mean Absolute Error | `1/n × Σ\|yᵢ − ŷᵢ\|` | USD | Average absolute prediction error |
| **MSE** | Mean Squared Error | `1/n × Σ(yᵢ − ŷᵢ)²` | USD² | Penalizes larger errors more strongly |
| **RMSE** | Root Mean Squared Error | `√MSE` | USD | Typical prediction error magnitude |

---

## 🖥️ Graphical User Interface

The application was created using **Tkinter**.

The interface contains two main pages.

### Page 1 — Vehicle Information

The user enters:

```text
Mileage_km
Engine_L
Accident_Count
Technical_Score
Year
```

The application then creates a Pandas DataFrame containing these values and passes them to the trained model.

---

### Page 2 — Prediction Result

The result page displays:

### 💰 Estimated Price

The predicted price is shown in USD.

Example:

```text
$25,450.32
```

The application also displays:

```text
Model Performance

MAE
MSE
RMSE
```

and a summary of the vehicle information entered by the user.

---

## 🎨 User Interface

The application uses a dark-themed interface with:

- Dark background
- Card-based layout
- Modern input fields
- Prediction button
- Highlighted estimated price
- Model performance cards
- Vehicle information summary

The window is configured as:

```text
720 × 700
```

and is not resizable.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **Tkinter** | Graphical User Interface |
| **Pandas** | Data loading and DataFrame processing |
| **NumPy** | Numerical calculations |
| **Scikit-learn** | Machine learning and evaluation |
| **Excel** | Dataset storage |

---

## 📦 Libraries

The project uses the following Python libraries:

```python
import tkinter as tk
from tkinter import messagebox

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)
```

---

## ⚙️ Installation

### 1. Install Python

Make sure Python is installed on your computer.

You can check the installation with:

```bash
python --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/Amironix785/Car-Price-.git
```

Then enter the project directory:

```bash
cd Car-Price-
```

---

### 3. Install Required Libraries

Install the required Python packages:

```bash
pip install pandas numpy scikit-learn openpyxl
```

`openpyxl` is required because the project reads the Excel dataset.

---

## 📁 Project Structure

A typical project structure is:

```text
Car-Price-/
│
├── main.py
├── project1_used_car_data.xlsx
├── Screenshot 2026-08-29 173034.png
├── Screenshot 2026-08-29 173028.png
└── README.md
```

### File Descriptions

| File | Purpose |
|---|---|
| `main.py` | Main Python application |
| `project1_used_car_data.xlsx` | Machine learning dataset |
| `Screenshot 2026-08-29 173034.png` | Application input screenshot |
| `Screenshot 2026-08-29 173028.png` | Prediction/result screenshot |
| `README.md` | Project documentation |

---

## ▶️ Running the Project

Make sure the Python file and Excel dataset are located in the correct directory.

Then run:

```bash
python main.py
```

The graphical application should open.

---

## 🧑‍💻 How to Use

### Step 1

Open the application.

### Step 2

Enter the vehicle's information:

```text
Mileage_km
Engine_L
Accident_Count
Technical_Score
Year
```

### Step 3

Click:

```text
Predict Price →
```

### Step 4

The application will calculate the estimated price.

### Step 5

The result page will display:

- Estimated vehicle price
- MAE
- MSE
- RMSE
- Entered vehicle information

### Step 6

Click:

```text
← Back
```

to return to the input page and make another prediction.

---

## 🔍 Input Validation

The application checks whether numerical values can be converted into the required data types.

For example:

- Mileage → `float`
- Engine size → `float`
- Accident count → `int`
- Technical score → `float`
- Year → `int`

If an invalid value is entered, the application displays:

```text
Invalid Input

Please enter valid numbers in all fields.
```

---

## 📈 Prediction Process

When the user clicks the prediction button, the application:

1. Reads the entered values.
2. Converts them to the appropriate numerical types.
3. Creates a Pandas DataFrame.
4. Arranges the columns in the same order used to train the model.
5. Sends the data to the trained Linear Regression model.
6. Generates the predicted price.
7. Displays the result on the result page.

The prediction is generated using:

```python
prediction = model.predict(input_data)[0]
```

---

## 🔐 Reproducibility

The project uses:

```python
random_state=42
```

during the train/test split.

This ensures that the same dataset produces the same train/test split when the project is run again, assuming the dataset and environment remain unchanged.

---

## ⚠️ Limitations

This project is an educational machine learning application and the predicted price should be considered an **estimate**, not a guaranteed market price.

The prediction depends on the quality and characteristics of the dataset.

The current model uses only five input features:

- Mileage
- Engine size
- Accident count
- Technical score
- Manufacturing year

Real-world vehicle prices can also depend on many other factors, such as:

- Brand
- Model
- Trim level
- Location
- Supply and demand
- Vehicle options
- Service history
- Number of previous owners
- Fuel type
- Transmission
- Exterior and interior condition

These factors are not included in the current model.

---

## 🚀 Possible Future Improvements

Possible improvements for future versions include:

- Add more vehicle features
- Compare multiple regression algorithms
- Add data visualization
- Add a larger and more diverse dataset
- Add cross-validation
- Add R² score
- Add prediction confidence or uncertainty information
- Improve input validation
- Add automatic dataset statistics
- Save prediction history
- Export predictions to Excel or CSV
- Create charts comparing actual and predicted prices
- Add model training and evaluation as a separate module
- Save the trained model using `joblib`
- Improve the GUI with additional themes and animations

---

## 📊 Model Evaluation

The application calculates the evaluation metrics dynamically from the test set.

The relevant part of the program is:

```python
y_pred = model.predict(x_test)

MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
```

This means the values displayed by the application are calculated from the current dataset and train/test split rather than being manually entered.

---

## 📚 Project Learning Goals

This project demonstrates several important concepts in Python and machine learning:

- Loading data from Excel
- Working with Pandas DataFrames
- Selecting machine learning features
- Separating features and target variables
- Splitting data into training and testing sets
- Training a Linear Regression model
- Generating predictions
- Evaluating regression models
- Building a graphical interface with Tkinter
- Connecting a machine learning model to a desktop application
- Handling invalid user input

---

## 👨‍💻 Author

**Amironix785**

GitHub:

**https://github.com/Amironix785**

Project:

**Car Price Predictor**

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is provided for educational and development purposes.

You are free to study, modify, and improve the project according to your needs.
