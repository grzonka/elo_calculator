import calculations as calc


def get_players():
    with open("matches.txt", "r") as f:
        player_names = []
        f.seek(0)
        line = f.readline()
        while line != '\n':
            player_names.append(line.replace("\n", ""))
            line = f.readline()
        for x in range(len(player_names)):
                print("ID: " + str(x) + ") " + player_names[x])
        return player_names


def get_user_id_input(min_val, max_val):
    user_input = int(input())
    if min_val <= user_input <= max_val:
        return user_input
    else:
        return -1


def add_match():
    with open("matches.txt", "a") as f:
        match_result = ""
        player_names = get_players()
        print("Please enter the ID of the winning player:")
        winner_input = get_user_id_input(0, len(player_names)-1)
        print("Please enter the ID of the loosing player:")
        looser_input = get_user_id_input(0, len(player_names)-1)
        if winner_input != -1 and looser_input != -1 and winner_input != looser_input:
            match_result = match_result + \
                           player_names[winner_input] + ", " + \
                           player_names[looser_input] + "\n"
            f.write(match_result)
            f.close()
            print("Match successfully added!")
            print(" ")
        else:
            print("That was not a valid input. \n"
                  "Do you want to try again? (y/n)")
            if input() == "n":
                quit()
            else:
                add_match()


def get_expected_winrate():
    player_names = get_players()
    print("Please enter the ID of the winning player:")
    winner_input = get_user_id_input(0, len(player_names) - 1)
    print("Please enter the ID of the loosing player:")
    looser_input = get_user_id_input(0, len(player_names) - 1)
    if winner_input != -1 and looser_input != -1 and winner_input != looser_input:
        # print("P1 is: " + str(winner_input) + ", P2 is: " + str(looser_input))
        calc.get_winrate(winner_input, looser_input)








