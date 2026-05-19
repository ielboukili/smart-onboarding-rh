from src.assistant import answer_question


def main():
    print("Smart Onboarding RH")
    print("Pose une question RH simple. Tape 'quit' pour sortir.\n")

    while True:
        question = input("Question: ").strip()
        if question.lower() in {"quit", "exit", "q"}:
            print("Fin du prototype.")
            break

        response = answer_question(question)
        print(f"\nReponse: {response}\n")


if __name__ == "__main__":
    main()
