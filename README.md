# minesweep
Simple Python3 implementation of a minesweeper game.

# How to Play

First download the python script like so:

```bash
$ curl https://raw.githubusercontent.com/redcricket/minesweep/master/minesweeper.py > ms.py
```

Next run it:

```bash
python3 ms.py
```

You should see this:

```bash
Enter size of field:
```

Enter something like 10. Then you'll see:

```bash
Enter number of mines [default=10]: 
```

You can just hit enter for 10 mines or enter some other integer greater than 0 but less than field size squared.  I entered 15 for this example.  Once you have entered something for the number of mines the game starts and you will see something like this:

```bash
0 1 2 3 4 5 6 7 8 9
_|_|_|_|_|_|_|_|_|_| 0
_|_|_|_|_|_|_|_|_|_| 1
_|_|_|_|_|_|_|_|_|_| 2
_|_|_|_|_|_|_|_|_|_| 3
_|_|_|_|_|_|_|_|_|_| 4
_|_|_|_|_|_|_|_|_|_| 5
_|_|_|_|_|_|_|_|_|_| 6
_|_|_|_|_|_|_|_|_|_| 7
_|_|_|_|_|_|_|_|_|_| 8
_|_|_|_|_|_|_|_|_|_| 9
Enter i,j:
```

Here you will enter your move.  For example enter `4,6` and you will see this:

```bash
0 1 2 3 4 5 6 7 8 9
_|_|_|_|_|_|_|_|_|_| 0
_|_|_|_|_|_|_|_|_|_| 1
_|_|_|_|_|_|_|_|_|_| 2
_|_|_|_|_|_|_|_|_|_| 3
_|_|_|_|_|_|_|_|_|_| 4
_|_|_|_|_|_|_|_|_|_| 5
_|_|_|_|3|_|_|_|_|_| 6
_|_|_|_|_|_|_|_|_|_| 7
_|_|_|_|_|_|_|_|_|_| 8
_|_|_|_|_|_|_|_|_|_| 9
Enter i,j:
```

Watch out now! Square 4,6 has 3 mines next to it.  Enter 2,9 and you will see:

```bash
Enter i,j: 2,9
0 1 2 3 4 5 6 7 8 9
_|_|_|_|_|_|_|_|_|_| 0
_|_|_|_|_|_|_|_|_|_| 1
_|_|_|_|_|_|_|_|_|_| 2
_|_|_|_|_|_|_|_|_|_| 3
_|_|_|_|_|_|_|_|_|_| 4
_|_|_|_|_|_|_|_|_|_| 5
_|_|_|_|3|_|_|_|_|_| 6
_|_|_|_|_|_|_|_|_|_| 7
_|1|1|2|_|_|_|_|_|_| 8
_|1|0|1|_|_|_|_|_|_| 9
Enter i,j:
```

And so on ...

```bash
Enter i,j: 4,4
0 1 2 3 4 5 6 7 8 9
_|_|_|_|_|_|_|_|_|_| 0
_|_|_|_|_|_|_|_|_|_| 1
_|_|_|_|_|_|_|_|_|_| 2
_|_|_|3|2|2|_|_|_|_| 3
_|_|_|1|0|1|_|_|_|_| 4
_|_|_|2|2|2|_|_|_|_| 5
_|_|_|_|3|_|_|_|_|_| 6
_|_|_|_|_|_|_|_|_|_| 7
_|1|1|2|_|_|_|_|_|_| 8
_|1|0|1|_|_|_|_|_|_| 9
Enter i,j: 2,4
BOOM!
0 1 2 3 4 5 6 7 8 9
_|_|_|_|_|_|_|_|_|_| 0
_|_|_|_|_|_|_|_|_|_| 1
_|_|_|_|_|_|_|_|_|_| 2
_|_|_|3|2|2|_|_|_|_| 3
_|_|*|1|0|1|_|_|_|_| 4
_|_|_|2|2|2|_|_|_|_| 5
_|_|_|_|3|_|_|_|_|_| 6
_|_|_|_|_|_|_|_|_|_| 7
_|1|1|2|_|_|_|_|_|_| 8
_|1|0|1|_|_|_|_|_|_| 9

0 1 2 3 4 5 6 7 8 9
1|1|1|1|2|2|2|*|2|1| 0
2|*|2|3|*|*|3|3|*|1| 1
*|2|2|*|*|4|*|2|1|1| 2
2|3|3|3|2|2|1|2|2|2| 3
1|*|*|1|0|1|1|2|*|*| 4
2|3|4|2|2|2|*|2|2|2| 5
1|*|3|*|3|*|3|3|1|1| 6
2|2|3|*|4|3|*|4|*|2| 7
*|1|1|2|*|3|3|*|*|2| 8
1|1|0|1|1|2|*|3|2|1| 9

```

# Project Origin

https://stackoverflow.com/questions/53510965/python-minesweeper-game-creating-function-that-returns-2d-grid-with-randomly-p
