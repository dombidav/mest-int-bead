from os import system, name


def choice(switch, unknown_message: str):
    answer = switch(input('Your choice:').strip(' '))
    while answer is None:
        answer = input(unknown_message)
    if answer in ['0', 0]:  # When I run this with debugger answer was string. When I run it from terminal answer was integer...
        exit(0)
    return answer


def clear_output():
    _ = system('cls') if name == 'nt' else system('clear')


def confirm(prompt: str, true_letter: str = 'y', false_letter: str = 'n') -> bool:
    ans = input(f"{prompt}({true_letter}/{false_letter})").strip(' ').lower()
    while ans not in [true_letter, false_letter]:
        clear_output()
        ans = input(f"Unknown option. \n{prompt}({true_letter}/{false_letter})").strip(
            ' ').lower()
    return ans == true_letter


def numeric_input(prompt) -> int:
    clear_output()
    ans = input(prompt).strip(' ').lower()
    while not ans.isnumeric():
        clear_output()
        ans = input(f"Unknown option. \n{prompt}").strip(' ').lower()
    ans = int(ans)
    return ans
