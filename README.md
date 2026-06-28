# 🛡️ Phishing Email Detector

## Overview

The **Phishing Email Detector** is a Python-based cybersecurity project that identifies potentially malicious emails by scanning email content for commonly used phishing keywords. This project demonstrates the fundamentals of phishing detection and serves as an educational tool for learning Python and basic cybersecurity concepts.

---

## Features

* Detects common phishing-related keywords.
* Displays suspicious keywords found in the email.
* Assigns a basic risk level (Low, Medium, High).
* User-friendly command-line interface.
* Modular and easy-to-understand Python code.
* Easy to customize by adding new phishing keywords.

---

## Technologies Used

* Python 3
* Standard Python Libraries

---

## Project Structure

```text
Phishing-Email-Detector/
│── phishing_detector.py
│── README.md
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/Phishing-Email-Detector.git
```

2. Navigate to the project directory:

```bash
cd Phishing-Email-Detector
```

3. Run the program:

```bash
python phishing_detector.py
```

---

## Sample Input

```text
Urgent! Your account has been suspended.
Click here to verify your bank login password and claim your prize.
```

## Sample Output

```text
⚠ Potential Phishing Email Detected

Suspicious Keywords Found:
• urgent
• verify
• click here
• account suspended
• password
• bank
• login

Risk Level: HIGH
```

---

## How It Works

1. Accepts an email message from the user.
2. Converts the message to lowercase.
3. Searches for predefined phishing keywords.
4. Displays detected keywords.
5. Determines the risk level based on the number of keyword matches.

---

## Applications

* Cybersecurity education
* Phishing awareness training
* Python programming practice
* Academic mini projects
* Basic email security analysis

---

## Future Enhancements

* Machine learning-based phishing detection.
* URL and attachment analysis.
* Graphical User Interface (GUI).
* Real-time email scanning.
* Email API integration.
* Larger phishing keyword database.

---

## Learning Outcomes

* Python programming fundamentals
* String manipulation
* Functions and modular programming
* Keyword-based text analysis
* Basic cybersecurity principles

---

## 👩‍💻 Author

**Shalini D**

Cyber Security Intern

DecodeLabs Industrial Training Program

---

## License

This project is licensed under the **MIT License**. It is intended for educational and learning purposes.
