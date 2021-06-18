def find_person(needle: str, haystack):
    return [person for person in (haystack.left_side + haystack.right_side) if person.minutes == int(needle)][0] or None


class Person:
    def __init__(self, minutes: int):
        self.minutes = minutes

    def __str__(self):
        return str(self.minutes)
