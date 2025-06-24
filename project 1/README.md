#Phishing Website Detection Tool
🛡️ Real-Time URL Detector
A Python-based application that detects phishing URLs using a hybrid approach: rule-based heuristics combined with a machine learning model trained on TF-IDF features and a Random Forest Classifier. The interface is built with Tkinter for real-time interaction.

🚀 Features
- ✅ Rule-Based Detection
Uses pattern matching to flag suspicious keywords and numeric patterns in URLs.
- 🤖 Machine Learning Detection
Classifies URLs using TF-IDF vectorization and a trained Random Forest model.
- 🖥️ User-Friendly Interface
Simple GUI with Tkinter for real-time URL input and feedback.

🧠 How It Works
- Loads labeled URL dataset from urls.csv with url and label columns.
- Trains a machine learning model using TF-IDF and Random Forest.
- Checks input URLs against:
- Common phishing patterns (rule-based)
- Trained ML model predictions
- Displays both results in a message box.



