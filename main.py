from pathlib import Path
from time import sleep
from task_one import (
    this_should_be_true,
    this_should_be_blue,
    this_should_be_three,
    this_should_be_free,
    this_should_be_long,
    this_should_be_one,
    this_should_be_None,
    this_should_be_nine,
    this_should_be_prime,
    this_should_be_fine,
)
from task_two import statements, dementi


def isprime(num):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True


if __name__ == "__main__":
    # init
    proceed = False
    for i in range(1, 6):
        print("." * i)
        sleep(0.1)

    # task 1
    if (
        (this_should_be_true() == True)
        and (this_should_be_blue() == "blue")
        and (this_should_be_three() == 3)
        and (this_should_be_free() == "free")
        and (len(this_should_be_long()) > 10)
        and (this_should_be_one() == 1)
        and (this_should_be_None() == None)
        and (this_should_be_nine() == 9)
        and (isprime(this_should_be_prime()))
        and (this_should_be_fine() or not this_should_be_fine())
    ):
        proceed = True
    else:
        print("hmm.. something isn't quite right, yet :/")

    # task 2
    if proceed:
        for your in Path("contributors").glob("*"):
            try:
                print(
                    f'{your.name} says: "{
                        statements[your.name]
                        if (dementi[your.name] == "")
                        else dementi[your.name]
                    }"\n'
                )
            except KeyError:
                print(f"{your.name} has nothing to say..\n")
            sleep(2)
        print("done!")
