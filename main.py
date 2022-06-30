from question_model import Question
from data import question_data


def main():
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        question_bank.append(Question(question_text, question_answer))


if __name__ == "__main__":
    main()
