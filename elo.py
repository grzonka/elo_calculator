import calculations as calc
import importlib
import player_management as pm


def show_menu():
    importlib.reload(calc)
    print("Use the number for your desired option:\n"
          "1) Check players ratings.\n"
          "2) Add match results.\n"
          "3) Or any other key to exit.\n")
    user_input = input()
    if user_input == "1":
        calc.main()
        show_menu()
    elif user_input == "2":
        pm.add_match()
        show_menu()
    else:               # user_input == "3" or "n" or "no":
        quit()


if __name__ == '__main__':
    show_menu()
