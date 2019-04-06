# elo_calculator

This calculator can be used to calculate the elo of players based on previously documented games.

### Prerequisites

Python 3 installed on your system (Version 3.7.2 was used at the time of writing).
matplotlib needs to be installed in order to show a graph of elo progression over time.
You can still use the script for command line output only which does not neeed matplotlib installed. Just comment out the very first and last lines in the script if you do not want a graph to be generated.

## Getting Started

cloning the project into a desired location. You can then edit the matches.txt file to add the names of all competitors first, then after an empty line add the match results in the format <winning_player>, <loosing_player>. Note the whitespace between the comma and the loosing player. See example below: 

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

In the directory where 'elo.py' and 'matches.txt' are located run:

```
python elo.py
```

## License

This project is licensed under the [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) License 

