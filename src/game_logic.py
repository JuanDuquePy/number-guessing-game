# Lógica principal del juego (generar número, evaluar intentos)
import random
from cli import guess


def random_number() -> int:
    """Genera un npumero random

    Returns:
        int: Restorna un número randon entre 1 y 100
    """
    computer_number: int = random.randrange(1, 100)

    return computer_number


def attempts(level: int, option_user: int):
    """Cuenta los intentos hasta que no tengas más cuando esto pasa
    el programa finaliza.
    """
    pc_number = random_number()
    user_guess = guess()

    max_attempts = 0

    if option_user == 1:
        max_attempts += level
    elif option_user == 2:
        max_attempts += level
    elif option_user == 3:
        max_attempts += level
    else:
        print('Opción incorrecta')

    user_attempts = 1

    while user_attempts < max_attempts:
        if user_guess == pc_number:
            print(
                'Congratulation! You guessed the correct number in '
                f'{user_attempts} attempts.\n'
            )
            break
        elif user_guess < pc_number:
            print(f'Incorrect! The number is less than {user_guess}.\n')

            user_guess = guess()
        elif user_guess > pc_number:
            print(f'Incorrect! The number is greater than 3 {user_guess}.\n')

            user_guess = guess()
        else:
            break

        user_attempts += 1

    if user_attempts == max_attempts and user_guess != pc_number:
        print(
            f'You failed to guess the correct number {pc_number} in '
            f'{user_attempts} attempts. Better luck next time!\n'
        )
