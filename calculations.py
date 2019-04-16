import matplotlib.pyplot as plt
# in case you do not need the feature or do not have
# matplotlib installed, comment out the import and the
# very last line 'print_graph()' to get console output only

# TODO: should change file I/O to with or try catch block!

f = open('matches.txt', 'r')

k_value = 32
starting_elo = 1200

players = []
rating_history = []

# both players and rating_history are not saved on runtime.
# since elo is constantly running saving data ther would be possible.


def init_players():
    line = f.readline()
    while line != '\n':
        # each player is given a own list to save his information
        players.append([line.replace("\n", "")])
        line = f.readline()

    for player in players:
        # the second entry of each individual players list represents his rating
        player.append(starting_elo)
        # furthermore elo is saved to an all time list in order to generate a graph
        rating_history.append([starting_elo])


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
    init_players()
    read_scores()
    print_ratings()
    print_graph()
    #get_players()


def get_winrate(player1_id, player2_id):
    init_players()
    read_scores()
    p1_elo = players[player1_id][1]
    p1_name= players[player1_id][0]
    p2_elo = players[player2_id][1]
    p2_name = players[player2_id][0]
    p1_vs_p2_wr = expected_score(p1_elo,p2_elo)
    nice_result = round(p1_vs_p2_wr * 100, 1)

    print(p1_name + " has a expected winrate of " + str(nice_result) + "% against " + p2_name
          + ".\n")



