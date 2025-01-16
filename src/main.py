from cli import show_menu
from difficulty import select_level
from game_logic import attempts

option: int = show_menu()

level: int = select_level(option)

attempts(level, option)
