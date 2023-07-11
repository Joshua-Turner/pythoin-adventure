def test_func():
    arr = [1, 2, 3]


test_func()


def print_choice_answers(answers):
    valid_answers = "Valid answers: "
    for answer in answers:
        valid_answers += answer[0] + ","
    print(valid_answers.rstrip(","))


# any amount of answers
# if input invalid repeat question and propose answers
def create_choice(question: str, answers: list[tuple]):
    def ask(print_answers=False):
        if print_answers:
            print_choice_answers(answers)

        input_answer = input(question).lower()

        for answer in answers:
            if input_answer == answer[0].lower():
                if callable(answer[1]):
                    answer[1]()
                return True

        return False

    return ask


ask_for_money = create_choice(
    "You find money. Do you pick it up?",
    [
        ("Yes", lambda: print("Adding 10 Coins")),
        ("No", False),
        ("Run", lambda: print("You die")),
    ],
)


def ask_question(question, offer_hints_after=3, ask_times=None):
    asking = False
    i = 1
    while not asking:
        if isinstance(ask_times, int) and i > ask_times:
            break
        offer_hints = (
            True if offer_hints_after is not None and i > offer_hints_after else False
        )
        asking = question(offer_hints)
        i += 1


ask_question(ask_for_money, 1, 3)
