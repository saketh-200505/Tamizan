import tkinter as tk
import re
import nltk
from nltk.corpus import words

# Ensure nltk words list is available
nltk.download("words")
word_list = set(words.words())

def check_password_strength(password):
    strength = "Weak"
    suggestions = []

    # Length check
    if len(password) >= 12:
        strength = "Medium"
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password) and re.search(r"\W", password):
        strength = "Strong"
    else:
        if not re.search(r"[A-Z]", password):
            suggestions.append("Add an uppercase letter.")
        if not re.search(r"[a-z]", password):
            suggestions.append("Add a lowercase letter.")
        if not re.search(r"\d", password):
            suggestions.append("Include a number.")
        if not re.search(r"\W", password):
            suggestions.append("Use special characters (!, @, #, etc.).")

    # Dictionary word detection
    if any(word.lower() in word_list for word in re.findall(r'\b\w+\b', password)):
        strength = "Weak"
        suggestions.append("Avoid dictionary words in your password.")

    return strength, suggestions

def analyze_password():
    password = entry.get()
    strength, suggestions = check_password_strength(password)
    result_label.config(text=f"Strength: {strength}")
    suggestions_label.config(text="\n".join(suggestions))

# GUI setup
root = tk.Tk()
root.title("Password Strength Analyzer")

tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Analyze", command=analyze_password).pack()

result_label = tk.Label(root, text="")
result_label.pack()
suggestions_label = tk.Label(root, text="")
suggestions_label.pack()

root.mainloop()