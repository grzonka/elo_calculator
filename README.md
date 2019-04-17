# elo_calculator

This command line tool can manage 1vs1 based game data for as many players as needed based on an Elo-system.
Currently implemented features are:
```
- display player ratings in terminal
- add game results
- plot player ratings over time
- calculate expected winrate for a match between 2 players
```

### Prerequisites

Python 3 installed on your system (Version 3.7.2 was used at the time of writing).
matplotlib needs to be installed in order to show a graph of elo progression over time. This is usually done via 'pip install matplotlib' in the terminal but can vary based on python install.
You can still use the script for command line output only which does not neeed matplotlib installed. Just comment out the very first and last lines in the 'calculations.py' script if you do not want a graph to be generated.

## Getting Started

Cloning the project into a desired location or download the files as zip and extract them. 
All competing players need to be added at the top of 'players.txt' with each player in a separate line. 
See example below: 

###### players.txt
```
Marry
Susan
David
Richard
```

The starting elo for each player is 1200. The k-value determining the maximum elo gains is set to 32. Both numbers can be edited at the beginning of elo.py


## Running the script

If you have 'players.txt', 'matches.txt' and 'elo.py' all in the same folder use the script by running

```
python elo.py
```
in a terminal.

## License

This project is licensed under the [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) License 

