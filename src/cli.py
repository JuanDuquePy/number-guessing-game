# Manejo de la interacción en la línea de comandosimport click
def show_menu() -> int:
    menu_welcome: list[str] = [
        'Welcome to the Number Guessing Game!',
        'I\'m thinking if a number between 1 and 100.',
    ]
    # \u2764 | Emoji de corazón
    menu_options: dict = {
        1: '\U0001F414Easy (10 chances)',
        2: '\U0001F98AMedium (5 chances)',
        3: '\U0001F480Hard (3 chances)',
    }

    for i in menu_welcome:
        print(i)

    print('')

    for i, a in enumerate(menu_options, 1):
        print(f'{i}. {menu_options[a]}')

    try:
        option_user: int = int(input('\nEnter your choice: ').strip())
        return option_user
    except ValueError as e:
        print(f'La opción debe ser un número | {e}')
        return 0


def guess() -> int:
    """Ingresa el número que cree que es el correcto para adivinar
    el que tiene el computador

    Returns:
        int: number guess
    """
    user_guess = int(input('Enter your guess: ').strip())
    return user_guess
