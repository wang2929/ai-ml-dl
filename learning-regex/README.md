# 🧠 Regex Fundamentals Assignment

Welcome to your Regex reinforcement assignment! This exercise is designed to help you **practice pattern recognition** and apply your knowledge of **Python regular expressions** in real-world scenarios.


## 📂 Assignment Structure

This repo contains two files:

### 1. `main.py`
You will find 15 functions, each of which takes a single string input and must return `True` if the string matches a specific pattern, or `False` otherwise.  
Inside each function, you'll find a clear description of what your regular expression needs to match.  
Your task is to write an appropriate regex and implement it using Python’s `re` module.

### 2. `test.py`
This is a **pytest test suite** that contains **3 test cases per function** (for a total of 45 tests). Use this file to verify that your implementations work correctly.

To run the tests, make sure you have `pytest` installed and run:

```bash
pytest test.py
```

## 🛠 Skills You’ll Practice

* Character classes (e.g., `[a-z]`, `\\d`, `\\w`)
* Anchors (`^`, `$`)
* Quantifiers (`*`, `+`, `?`, `{min,max}`)
* Grouping and alternation (`()`, `|`)
* Real-world matching (emails, phone numbers, dates, IPs, passwords)


## ✅ Completion Criteria

You are finished with this assignment when:

* All 15 functions are correctly implemented with valid regex.
* All tests in `test.py` pass.
* Your code is clean, readable, and follows Python conventions.

## 💡 Tips

* Use [regex101.com](https://regex101.com) or [pythex.org](https://pythex.org) to test patterns before writing them in Python.
* Start simple and iterate: write a small regex, then add conditions gradually.
* Use raw strings in Python (`r\"pattern\"`) to avoid escaping backslashes.


## 🚀 Stretch Goals

If you finish early, try these optional challenges:

* Write your own regex challenges and test them.
* Modify `test.py` to include edge cases or unexpected input.
* Explore regex lookaheads, lookbehinds, or multiline flags.


Happy matching! 🧩
