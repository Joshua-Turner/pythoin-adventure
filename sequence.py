def create_next_step_id(current_step_id, next_step_name):
    step_ids = current_step_id.split(".")
    step_ids.pop()
    new_step_id = ""

    def get_separator():
        nonlocal new_step_id
        return "." if new_step_id else ""

    for step in step_ids:
        new_step_id += get_separator() + step
    return new_step_id + get_separator() + next_step_name


def enter(character, step_id):
    print("You enter a large cave.")
    print("Before you are two pathways.")
    direction = input(character.name + ": Do you go left(L) or right(R)?").lower()
    next_step_name = "start_left" if direction == "l" else "start_right"
    print(
        'You choose "'
        + direction
        + '" so next step is: '
        + create_next_step_id(step_id, next_step_name)
    )
    return create_next_step_id(step_id, next_step_name)


def end(**args):
    print("You come to the end of the cave.")
    return True


def start_left(**args):
    print("You choose to go left.")
    print("You enter a narrow, winding pathway.")
    answer = input("You find a coin. Do you pick it up? (y/n)").lower()

    if answer == "y":
        args["character"].inventory.add_item("Coin", 1)

    return True


def continue_left(**args):
    print("You continue down the pathway.")
    return True


def continue_left_2(**args):
    print("You continue down the pathway even further then exit.")
    return end_id


def start_right(**args):
    print("You choose to go right.")
    print("You enter a wide, straight pathway.")
    answer = input("You find a some coins. Do you pick it up? (y/n)").lower()

    if answer == "y":
        print("Adding 10 coind to inventory.")
        args["character"].inventory.add_item("Coin", 10)

    return True


def continue_right(**args):
    print("You continue down the pathway.")
    return True


def continue_right_2(**args):
    print("You continue down the pathway even further then exit.")
    return end_id


end_id = "cave_01.end"

start_left_path = [
    {"name": "start_left", "action": start_left},
    {"name": "continue_left", "action": continue_left},
    {"name": "continue_left_2", "action": continue_left_2},
]

start_right_path = [
    {"name": "start_right", "action": start_right},
    {"name": "continue_right", "action": continue_right},
    {"name": "continue_right_2", "action": continue_right_2},
]

cave = {
    "name": "cave_01",
    "action": [
        {"name": "enter", "action": enter},
        {"name": "start_left", "action": start_left_path},
        {"name": "start_right", "action": start_right_path},
        {"name": "end", "action": end},
    ],
}
