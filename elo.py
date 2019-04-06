import matplotlib.pyplot as plt
# in case you do not need the feature or do not have
# matplotlib installed, comment out the import and the
# very last line 'print_graph()' to get console output only

k_value = 32
starting_elo = 1200

players = []
rating_history = []


def init_players():
    line = f.readline()
    while line != '\n':
        players.append([line.replace("\n", "")])
        line = f.readline()
    for player in players:
        player.append(starting_elo)
        rating_history.append([starting_elo])
    print(rating_history)


def read_scores():
    line = f.readline()
    while line != '':
        calc_new_elo(line.split(", ")[0], line.split(", ")[1].replace("\n", ""))
        line = f.readline()

        # add updated ratings to rating_history
        for x in range(len(rating_history)):
            rating_history[x].append(players[x][1])


def print_players():
    sorted_list = sorted(players, key=lambda l: l[1], reverse=True)
    print("The current Elo ratings are:")
    for p in range(len(sorted_list)):
        print(sorted_list[p][0].ljust(12) +
              str(round(sorted_list[p][1])).rjust(4))


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
    for x in range(len(players)):
        plt.plot(rating_history[x], label=players[x][0])
    plt.legend()
    plt.xlabel("# of games")
    plt.ylabel("Elo")
    plt.title("Elo progress")
    plt.show()


if __name__ == '__main__':
    with open('matches.txt', 'r') as f:
        init_players()
        read_scores()
        print_players()
        print_graph()

