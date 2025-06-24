import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
from tkinter import messagebox

# Load and preprocess dataset for ML approach
df = pd.read_csv("urls.csv")
X = df["url"]
y = df["label"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

clf = RandomForestClassifier()
clf.fit(X_vec, y)

# Rule-based detection function
def is_suspicious(url):
    phishing_patterns = [r"login", r"verify", r"update", r"\d{4,}", r"free", r"cheap", r"secure", r"account"]
    return any(re.search(pattern, url, re.IGNORECASE) for pattern in phishing_patterns)

# ML-based detection function
def classify_url(url):
    url_vec = vectorizer.transform([url])
    return clf.predict(url_vec)[0]

# Unified detection function
def detect_url(url):
    rule_based_label = "phishing" if is_suspicious(url) else "legitimate"
    ml_label = classify_url(url)
    return f"Rule-based: {rule_based_label} | ML: {ml_label}"

# Tkinter GUI
def check_url():
    url = entry.get()
    result = detect_url(url)
    messagebox.showinfo("URL Classification", result)

root = tk.Tk()
root.title("Real-Time URL Detector")

tk.Label(root, text="Enter URL:").pack()
entry = tk.Entry(root, width=50)
entry.pack()
tk.Button(root, text="Check", command=check_url).pack()

root.mainloop()