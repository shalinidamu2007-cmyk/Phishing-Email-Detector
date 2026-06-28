# Phishing Email Detector

phishing_keywords = [
    "urgent",
    "verify",
    "click here",
    "account suspended",
    "password",
    "bank",
    "login",
    "winner",
    "prize",
    "free",
    "gift",
    "claim",
    "limited time",
    "security alert",
    "update account",
    "confirm identity"
]


def detect_phishing(message):
    message = message.lower()
    found_keywords = []

    for keyword in phishing_keywords:
        if keyword in message:
            found_keywords.append(keyword)

    return found_keywords


def display_result(found_keywords):
    print("\n========== RESULT ==========")

    if found_keywords:
        print("⚠ Potential Phishing Email Detected")
        print(f"\nSuspicious Keywords Found ({len(found_keywords)}):")

        for keyword in found_keywords:
            print(f"• {keyword}")

        if len(found_keywords) >= 5:
            print("\nRisk Level : HIGH")
        elif len(found_keywords) >= 3:
            print("\nRisk Level : MEDIUM")
        else:
            print("\nRisk Level : LOW")
    else:
        print("✓ No common phishing keywords detected.")
        print("Risk Level : SAFE")

    print("============================")


def main():
    print("=== Phishing Email Detector ===")

    email_message = input("\nPaste Email Message:\n\n")

    detected_keywords = detect_phishing(email_message)

    display_result(detected_keywords)


if __name__ == "__main__":
    main()
