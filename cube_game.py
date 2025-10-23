import uuid
from random import randrange
player_1 = 0
player_2 = 0

def roll_two_d6() -> tuple[int, int]:
    number_1 = (randrange(1, 7))
    number_2 = (randrange(1, 7))
    result = tuple([number_1,number_2])
    return result


def is_bust(score: int) -> bool:
    if score >= 100 :
        return True
    else:
        return False

def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    if a > b:
        return 1
    elif b > a:
        return 2
    elif a == b:
        return None
def tie_breaker(roller) -> int:



