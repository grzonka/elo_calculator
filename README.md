# elo_calculator

This calculator can be used to calculate the elo of players based on previously documented games.

### Prerequisites

Python 3 installed on your system (Version 3.7.2 was used at the time of writing).
matplotlib needs to be installed in order to show a graph of elo progression over time. This is usually done via 'pip install matplotlib' in the terminal but can vary based on python install.
You can still use the script for command line output only which does not neeed matplotlib installed. Just comment out the very first and last lines in the 'calculations.py' script if you do not want a graph to be generated.

## Getting Started

cloning the project into a desired location or downloade the files as zip and extract them. 
All competing players need to be added at the top of 'matches.txt'. Seperating all players from the following matches via a blank line and manually adding the very first result in the format <winning_player>, <loosing_player> might still be needed in order for the script to properly run. (All consequent match results can simply be added via the command line when running the script. Note the whitespace between the comma and the loosing player. See example below: 

```
Marry
Susan
David
Richard

Marry, David
Richard, Susan
etc...

```

The starting elo for each player is 1200. The k-value determining the maximum elo gains is set to 32. Both numbers can be edited at the beginning of elo.py


## Running the script

If you have 'calculations.py', 'player_management.py', 'elo.py' and 'matches.txt' all in the same folder use the script by running:

```
python elo.py
```
in a terminal.

## License

This project is licensed under the [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) License 

