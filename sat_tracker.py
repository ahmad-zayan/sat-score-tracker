scores = []

while True:
    print("\n=== SAT Tracker ===")
    print("1. Add score")
    print("2. View scores")
    print("3. Best score")
    print("4. Average score")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        score = int(input("Enter SAT score: "))
        scores.append(score)
        print("Score added!")

    elif choice == "2":
        print("Scores:", scores)

    elif choice == "3":
        if scores:
            print("Best score:", max(scores))
        else:
            print("No scores yet")

    elif choice == "4":
        if scores:
            print("Average:", sum(scores) / len(scores))
        else:
            print("No scores yet")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")