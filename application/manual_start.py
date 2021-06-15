from application.interaction import clear_output, confirm, numeric_input
from models.person import Person
from models.state import State


def ask_for_side(side: str, result: State):
    ans = ask_side_text(result, side)
    while ans != 'y':
        if ans == 'e':
            if side == 'left':
                result.left_side.clear()
            else:
                result.right_side.clear()
        elif ans.isnumeric():
            ans = int(ans)
            if not result.left_side.__contains__(ans) and not result.right_side.__contains__(ans):
                if side == 'left':
                    result.left_side.append(Person(ans))
                else:
                    result.right_side.append(Person(ans))
                clear_output()
            else:
                print('This person was already added')
        else:
            print('Unknown choice')
        ans = ask_side_text(result, side)
    return result


def ask_side_text(result, side):
    clear_output()
    print(f"""
    Setting {side} side. Writing the necessary minutes for the given person to cross the bride.
    Current state: {result}
    Enter - save person, and add another.
    E - Clear side
    Y - Done
    """)
    return input('minutes:').lower().strip(' ')


def init_manual_start():
    result = None
    while result is None:
        clear_output()
        print("""
            Manual initialization of the state.
            Instruction: First you can set the left side of the river. You can add people to each side, by writing the necessary minutes for the given person to cross the bride. Everyone should have different speeds.
            """)
        result = State([])

        ask_for_side('left', result)
        ask_for_side('right', result)

        result.lamp_on_left = confirm('Should the lamp be on the left side or the right side?', 'l', 'r')
        result.remaining_minutes = numeric_input('Remaining minutes:')

        clear_output()
        print(f"State is the following: {result}  | Remaining minutes: {result.remaining_minutes}")
        if not confirm('Is this correct?'):
            result = None
    return result
