from enum import Enum


class Semaphore(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


# def handle_semaphore(light):
#     if light is Semaphore.RED:
#         print("You must stop!")
#     elif light is Semaphore.YELLOW:
#         print("Light will change to red, be careful!")
#     elif light is Semaphore.GREEN:
#         print("You can continue!")


def handle_semaphore(light):
    match light:
        case Semaphore.RED:
            print("You must stop!")
        case Semaphore.YELLOW:
            print("Light will change to red, be careful!")
        case Semaphore.GREEN:
            print("You can continue!")


handle_semaphore(Semaphore.YELLOW)
