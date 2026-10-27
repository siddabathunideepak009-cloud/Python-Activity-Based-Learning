answer_key = input("Enter answer key (use only A, B, C, D): ").strip().upper()

if not answer_key or any(ch not in "ABCD" for ch in answer_key):
    print("Invalid answer key. Use only A, B, C, or D.")
    exit()

students = int(input("Number of students: "))

correct_mark = 4
negative_mark = 1

for _ in range(students):
    name = input("\nStudent name: ").strip()
    answers = input("Student answers: ").strip().upper()

    correct = 0
    incorrect = 0
    unanswered = 0

    for i, key in enumerate(answer_key):
        response = answers[i] if i < len(answers) else ""

        if response == "":
            unanswered += 1
        elif response == key:
            correct += 1
        else:
            incorrect += 1

    score = correct * correct_mark - incorrect * negative_mark
    maximum = len(answer_key) * correct_mark
    percentage = score / maximum * 100

    print("\n----- EXAM RESULT -----")
    print("Student:", name)
    print("Correct:", correct)
    print("Incorrect:", incorrect)
    print("Unanswered:", unanswered)
    print(f"Score: {score}/{maximum}")
    print(f"Percentage: {percentage:.2f}%")