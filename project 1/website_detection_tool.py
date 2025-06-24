import re
import pandas as pd # type: ignore
import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset (CSV format: URL, Label 0=Legitimate, 1=Phishing)
df = pd.read_csv('phishing_dataset.csv')

X_train, X_test, y_train, y_test = train_test_split(df['URL'], df['Label'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = RandomForestClassifier()
model.fit(X_train_vec, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test_vec)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Suspicious patterns for rule-based detection
suspicious_patterns = [
    r'https?://\d+\.\d+\.\d+\.\d+',  
    r'https?://.*\-.*\-.*\.',        
    r'https?://.*\bfree\b.*',        
    r'https?://.*\blogin\b.*',       
    r'https?://.*\bverify\b.*'       
]

def rule_based_detection(url):
    return any(re.search(pattern, url) for pattern in suspicious_patterns)

def predict_url(url):
    # Rule-based detection
    if rule_based_detection(url):
        return "Phishing (Detected by Rules)"
    
    # Machine Learning-based detection
    url_vec = vectorizer.transform([url])
    return "Phishing" if model.predict(url_vec)[0] == 1 else "Legitimate"

# GUI Implementation (Tkinter)
def check_url():
    url = entry.get()
    result = predict_url(url)
    messagebox.showinfo("Result", f"URL Classification: {result}")

# Tkinter UI
root = tk.Tk()
root.title("Phishing URL Detector")
root.geometry("400x200")

tk.Label(root, text="Enter URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Check URL", command=check_url).pack(pady=10)

root.mainloop()