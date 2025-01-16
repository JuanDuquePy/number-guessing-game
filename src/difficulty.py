# \u2764 | Emoji de corazón


def select_level(option_user: int) -> int:

    number_lives = 0

    if option_user == 1:
        print(
            '\nGreat! You have selected the \U0001F414Easy difficulty level.\n'
            'Let\'s start the game!\n'
        )
        number_lives += 10
    elif option_user == 2:
        print(
            '\nGreat! You have selected the \U0001F98AMedium difficulty level.\n'
            'Let\'s start the game!\n'
        )
        number_lives += 5
    elif option_user == 3:
        print(
            '\nGreat! You have selected the \U0001F480Hard difficulty level.\n'
            'Let\'s start the game!\n'
        )
        number_lives += 3
    else:
        print('Error')

    return number_lives
