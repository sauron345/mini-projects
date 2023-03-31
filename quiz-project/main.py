import json
from color_message import Message as msg


def get_quiz():
    with open('quiz.json') as f:
        return json.load(f)


def main(quiz: list) -> None:
    i = 0
    correct_answers = ['d', 'b', 'b', 'd', 'a']
    myCorrAnswers = 0
    myWrongAnswers = 0
    question_num = 1
    allowed_letters = ['a', 'b', 'c', 'd']

    while i < len(quiz):
        print(f"Question {question_num}: {quiz[i]['question']}")
        print(f"a: {quiz[i]['a']}")
        print(f"b: {quiz[i]['b']}")
        print(f"c: {quiz[i]['c']}")
        print(f"d: {quiz[i]['d']}")

        response = input('Your response: ')

        if not response.isnumeric() and response in allowed_letters:
            if response.lower() == correct_answers[i]:
                print(msg.success(f"Correct answer! '{correct_answers[i]}' is a good answer"))
                myCorrAnswers += 1
            else:
                print(msg.error(f"'{response}' is wrong. Correct is '{correct_answers[i]}'"))
                myWrongAnswers += 1

            question_num += 1
            i += 1
        else:
            print(msg.error(f"Only {allowed_letters} are allowed, not digits or other characters"))

    print(msg.info("\nResults:"))
    print(msg.info(f"Good answers: {myCorrAnswers}"))
    print(msg.info(f"Wrong answers: {myWrongAnswers}"))


if __name__ == '__main__':
    quiz = get_quiz()
    try:
        main(quiz)
    except KeyboardInterrupt:
        print(msg.error('\nKeyboard interrupted and finished the program'))
