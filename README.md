# Internship_Assignment_1

# 💻 AI/ML Internship Tasks - DevelopersHub

This repository contains the four core tasks completed during my AI/ML internship at **DevelopersHub**. Each task is focused on real-world datasets and tools, demonstrating practical skills in data analysis, prediction, and interactive AI applications.

---

## 📊 Task 1: Exploring and Visualizing the Iris Dataset

### Objective:

Understand the Iris dataset through data inspection and visualization.

### Dataset:

* Iris dataset (available via Seaborn or CSV format)

### Instructions:

* Load dataset using `pandas`
* Inspect dataset with `.shape`, `.columns`, `.head()`
* View data summary with `.info()` and `.describe()`
* Visualize:

  * Scatter plots to show feature relationships
  * Histograms for value distribution
  * Box plots to identify outliers

### Tools:

* `pandas`, `seaborn`, `matplotlib`

### Skills Demonstrated:

* Data loading and inspection
* Statistical analysis
* Exploratory Data Visualization

📁 File: `Task1_Iris_Visualization.ipynb`

---

## 📈 Task 2: Predicting Future Stock Prices

### Objective:

Use machine learning to predict the next day’s closing price of a stock.

### Dataset:

* Stock data fetched using the `yfinance` API

### Instructions:

* Select a stock (e.g., AAPL, TSLA)
* Load historical stock data
* Use `Open`, `High`, `Low`, `Volume` to predict next `Close`
* Train a **Linear Regression** or **Random Forest** model
* Plot actual vs. predicted prices

### Tools:

* `yfinance`, `pandas`, `sklearn`, `matplotlib`

### Skills Demonstrated:

* Time series handling
* Regression modeling
* API data fetching

📁 File: `Task2_Stock_Price_Prediction.ipynb`

---

## ❤️ Task 3: Heart Disease Prediction

### Objective:

Build a classification model to predict heart disease risk.

### Dataset:

* UCI Heart Disease Dataset (from Kaggle)

### Instructions:

* Clean and preprocess data
* Perform EDA (Exploratory Data Analysis)
* Train a **Logistic Regression** or **Decision Tree** model
* Evaluate using Accuracy, Confusion Matrix, ROC Curve
* Highlight most important features

### Tools:

* `pandas`, `seaborn`, `sklearn`, `matplotlib`

### Skills Demonstrated:

* Binary classification
* Medical data interpretation
* Model evaluation (ROC-AUC, confusion matrix)

📁 File: `Task3_Heart_Disease_Prediction.ipynb`

---

## 🤖 Task 4: General Health Query Chatbot

### Objective:

Create an interactive chatbot using a Large Language Model (LLM) to respond to general health questions.

### Tools:

* `Streamlit` for GUI
* `Hugging Face` API (Zephyr-7B)
* `Lottie` for animation

### Instructions:

* Build a Python chatbot with a user-friendly interface
* Use prompt engineering to ensure safety and clarity
* Filter out harmful or unsafe advice

### Example Queries:

* "What causes a sore throat?"
* "Is paracetamol safe for children?"

### Notes:

* The **API token** is embedded directly in the Python file for testing
* The **Lottie animation file** (`animation.json`) should be placed in the **same folder** as the Python code

### Skills Demonstrated:

* Prompt engineering
* API usage for LLMs
* GUI design with animations

📁 Files:

* `Task4_Health_Chatbot.py`  ← Main Python script
* `animation.json`  ← Lottie animation file (required)

---

## 🚀 How to Run Each Task

### For Notebook Tasks (1–3):

1. Open the `.ipynb` file in Jupyter Notebook, Google Colab, or VSCode
2. Run each cell step-by-step

### For Task 4 Chatbot:

1. Make sure `animation.json` is in the same folder
2. Install requirements:

```bash
pip install streamlit requests streamlit-lottie
```

3. Run the chatbot:

```bash
streamlit run Task4_Health_Chatbot.py
```

---

## 🙌 Acknowledgements

Special thanks to **DevelopersHub Community** for providing mentorship, support, and real-world AI/ML tasks.

---

Feel free to ⭐ the repo if you found it useful!

🧠 *Built with Python · Powered by Open Source Tools · Made with ❤️ by Muhammad Ahsan Kareem*
