emails = [
    {
        "message": "Your bank account has been suspended. Click here immediately to verify your account.",
        "answer": "phishing"
    },
    {
        "message": "College notice: Semester exams start from July 10.",
        "answer": "legitimate"
    },
    {
        "message": "Congratulations! You won ₹50,000. Share your OTP to claim the prize.",
        "answer": "phishing"
    }
]

score = 0

print("===== Phishing Email Awareness Simulator =====")

for i, email in enumerate(emails, 1):
    print(f"\nEmail {i}:")
    print(email["message"])

    user = input("\nIs this 'phishing' or 'legitimate'? ").lower()

    if user == email["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("\n===== Result =====")
print("Score:", score, "/", len(emails))

if score == len(emails):
    print("Excellent phishing awareness!")
elif score >= 2:
    print("Good awareness. Keep practicing.")
else:
    print("You should improve your phishing detection skills.")
