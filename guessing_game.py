import random


def start_game(name, runtime, maximum):
    print('Hello {name}.'.format(name=name))

    try:
        guess = int(input('I am thinking of a number from 1 to {maximum}. Please guess the correct number.\n'
                          .format(maximum=maximum)))
    except ValueError:
        print('Sorry, your input needed to be an number. I do not wish to play this game anymore.')
        return

    number = random.randint(1, maximum)

    for i in range(0, runtime):
        if guess == number:
            print('You got it correct! The number was {number}.'.format(number=number))
            break
        else:
            try:
                guess = int(input('Sorry, that was incorrect, please try again. You have {remaining} tries left.\n'
                                  .format(remaining=runtime - i)))
            except ValueError:
                print('Sorry, your input needs to be a number. You lost one attempt. Try better on the next guess.')
    else:
        print('Sorry, you ran out of attempts. The correct number was {number}.'.format(number=number))


start_game('Zaid', 6, 20)
