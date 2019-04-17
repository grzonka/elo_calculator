# import calculations as calc
# import importlib
# import player_management as pm
import matplotlib.pyplot as plt

k_value = 32
starting_elo = 1200
players_initialized = False

players = []
rating_history = []

f = open('matches.txt', 'r')
p = open('players.txt', 'r')


def init_players():
    line = p.readline()
    while line != '\n' and line !='':
        # each player is given a own list to save his information
        players.append([line.replace("\n", "")])
        line = p.readline()
    # print(players)
    for player in players:
        # the second entry of each individual players list represents his rating
        player.append(starting_elo)
        # furthermore elo is saved to an all time list in order to generate a graph
        rating_history.append([starting_elo])
    global players_initialized
    players_initialized = True


def read_scores():
    line = f.readline()
    # TODO: improve handling of empty lines at the end of file.
    while line != '':
        line_split = line.replace("\n", "").split(", ")
        calc_new_elo(line_split[0], line_split[1])
        line = f.readline()

        # adding updated ratings to rating_history
        for x in range(len(rating_history)):
            rating_history[x].append(players[x][1])


def print_ratings():
    sorted_list = sorted(players, key=lambda l: l[1], reverse=True)
    print("The current Elo ratings are:")
    for p in range(len(sorted_list)):
        print(sorted_list[p][0].ljust(12) +
              str(round(sorted_list[p][1])).rjust(4))
    print("")


def calc_new_elo(winner, looser):
    """
    :param winner: string
    :param looser: string
    :return: nothing, changes winner and looser elo
    """
    for x in range(len(players)):
        if winner == players[x][0]:
            p1_elo = players[x][1]
            p1_index = x
        if looser == players[x][0]:
            p2_elo = players[x][1]
            p2_index = x

    rating_change = k_value*(1-expected_score(p1_elo, p2_elo))
    p1_elo = p1_elo + rating_change
    p2_elo = p2_elo - rating_change

    players[p1_index][1] = p1_elo
    players[p2_index][1] = p2_elo


def expected_score(rating1, rating2):
    ea = 1/(1+10**((rating2-rating1)/400))
    return ea


def print_graph():
    # print(players)
    # print(len(players))
    for x in range(len(players)):
        plt.plot(rating_history[x], label=players[x][0])
        # print("PRINTING: " +  str(x))
    plt.legend()
    plt.xlabel("# of games")
    plt.ylabel("Elo")
    plt.title("Elo progress")
    # uncomment one or both of the following lines to determine how the graph is shown at runtime
    # plt.show(dpi=300)                         # pop-ups the graph
    plt.savefig("graph_of_elo.png", dpi=300)    # saves/updates the graph in main directory
    # clearing matplotlib cache which is not done automaticly.
    plt.clf()


def do_all():
    if not players_initialized:
        init_players()
    read_scores()
    print_ratings()
    print_graph()
    #get_players()


def get_win_rate(player1_id, player2_id):
    #if not players_initialized:
    #     init_players()
    read_scores()
    p1_elo = players[player1_id][1]
    p1_name= players[player1_id][0]
    p2_elo = players[player2_id][1]
    p2_name = players[player2_id][0]
    p1_vs_p2_wr = expected_score(p1_elo,p2_elo)
    nice_result = round(p1_vs_p2_wr * 100, 1)

    print(p1_name + " has a expected win_rate of " + str(nice_result) + "% against " + p2_name
          + ".\n")


def get_user_id_input(min_val, max_val):
    user_input = int(input())
    if min_val <= user_input <= max_val:
        return user_input
    else:
        return -1


def add_match():
    with open("matches.txt", "a") as f:
        match_result = ""
        player_names = players
        # print(player_names)
        for x in range(len(player_names)):
                print("ID: " + str(x) + ") " + player_names[x][0])
        print("Please enter the ID of the winning player:")
        winner_input = get_user_id_input(0, len(player_names) - 1)
        print("Please enter the ID of the loosing player:")
        looser_input = get_user_id_input(0, len(player_names) - 1)
        if winner_input != -1 and looser_input != -1 and winner_input != looser_input:
            match_result = match_result + \
                           player_names[winner_input][0] + ", " + \
                           player_names[looser_input][0] + "\n"
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


def get_expected_win_rate():
    if not players_initialized:
        init_players()
    player_names = players
    for x in range(len(player_names)):
        print("ID: " + str(x) + ") " + player_names[x][0])
    print("Please enter the ID of the first player:")
    winner_input = get_user_id_input(0, len(player_names) - 1)
    print("Please enter the ID of the second player:")
    looser_input = get_user_id_input(0, len(player_names) - 1)
    if winner_input != -1 and looser_input != -1 and winner_input != looser_input:
        # print("P1 is: " + str(winner_input) + ", P2 is: " + str(looser_input))
        get_win_rate(winner_input, looser_input)


def show_menu():
    # importlib.reload(calc)
    print("Use the number for your desired option:\n"
          "1) Check players ratings.\n"
          "2) Add match results.\n"
          "3) Get expected winrate.\n"
          "4) Or any other key to exit.\n")
    user_input = input()
    if user_input == "1":
        do_all()
        # f.seek(0)
        show_menu()
    elif user_input == "2":
        add_match()
        show_menu()
    elif user_input == "3":
        get_expected_win_rate()
        show_menu()
    else:
        quit()


def set_saved_players(input_player_list):
    global saved_players
    saved_players = input_player_list


if __name__ == '__main__':
    show_menu()
