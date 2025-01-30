def quiz():
    questions = {
        "What is the capital of France?": "a",
        "What is 2 + 2?": "b",
        "What is the color of the sky?": "c"
    }

    options = {
        "What is the capital of France?": ["a) Paris", "b) London", "c) Berlin"],
        "What is 2 + 2?": ["a) 3", "b) 4", "c) 5"],
        "What is the color of the sky?": ["a) Blue", "b) Green", "c) Red"]
    }

    score = 0

    for question in questions:
        print(question)
        for option in options[question]:
            print(option)
        answer = input("Your answer (a/b/c): ").lower()

        if answer == questions[question]:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")

    print(f"Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()