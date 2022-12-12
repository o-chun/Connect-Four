# Connect-Four
Owen Chun
EECE2140: Final Project - Connect Four

# Final Project Report
Summary

This program runs a game of connect four in python using object-oriented programming. Connect four is a two-player game played on a 7 by 6 grid. Each player takes turns dropping a piece into a column with the goal of getting at least four of their own pieces in a row either horizontally, vertically, or diagonally. If the board is filled with no winner, the game ends in a tie. The game is played completely in the terminal. The user inputs their move to the terminal and the updated board is printed each turn. Besides the connect four game itself, the main feature of this program is the bot. The game can be a human user versus another user, a user versus a bot, or even a bot versus another bot. The bot was originally intended to have different difficulty settings, however this feature is still under construction. Since this program is a game, its expected application is to be played to have fun. :)

Overview of the Code

This program includes 6 classes. The first class is the 'Player' class. This is just a base class used for the next 4 classes. It contains attributes for the player's name and the 1 character symbol used to represent the player's pieces. It also contains a method 'print_info' to print this information.
Next is the 'Human' class which inherits the 'Player' class. This has the same initialization method as the 'Player' class, but the 'print_info' method additionaly print the player's type as 'User' to distinguish it from a bot. This class also has a 'make_move' method which prompts the user for their move and inserts their piece into the board, throwing an error if the column is full or the input was invalid.
Next is the 'Bot' class which also inherits the 'Player' class. Similar the 'Human' class, this class also uses the 'Player' class' initialization method and the 'print_info' method prints its type as 'Bot', but the print method for this class also prints the bot's difficulty. There are also some other attributes and methods that are unfinished, but will be used to complete the bot's harder difficulties.
The next three classes are 'Easy', 'Normal', and 'Hard, which all inherit the 'Bot' class. These classes are all initialized the same way as a 'Bot' and print their info with their corresponding difficulties; however, they each have different 'make_move' methods to place a piece. The easy bot just places a piece randomly as long as the move is valid. The normal and hard bots are still deciding how to place their pieces.
The last class is the 'Board' class. This does not inherit any of the other classes, but it uses 2 instances of some type of Player. The Board's attributes are 'data', 'did_p1_start', 'player1', 'player2', 'current', 'status', and 'turn_num'. 'data' is a 7 by 6 array containing the boards pieces with empty spaces being represented by a space. This is updated each turn as pieces are inserted. 'did_p1_start' will used to keep track of who started, so the other player starts the next round; however, this feature is still unfinished and only one game can be played at a time. 'player1' and 'player2' store the player objects. 'current' is assigned to the player object of whose turn it currently is. 'status' represents the status of the game: 'ongoing', 'win', or 'tie'. 'turn_num' is used to keep track of the turn number, which is printed at the start of each turn.
The first method of the 'Board' class is the 'draw_board' method which prints the board to the terminal using the board's 'data'. The next method is 'check_status' which checks for a win or a tie after a piece is played and updates the 'status' accordingly. 'is_column_open' checks if the supplied column is open and returns false if it is full. 'find_open_row' finds the lowest open row in the supplied column. 'insert_piece' takes in a column number and inserts the current player's piece into that column at the lowest empty row using 'find_open_row'. 'run_turn' runs one turn of the game. It prints the turn number and the player's name, takes a move from the player, prints the updated board, and then checks the status. 'set_settings' prints the current game settings and asks the user if they want to change them. The user can then change the settings if wanted. 'run_game' runs a full game of connect four and ends when the status is 'win' or 'tie'.

Instructions

A game automatically starts when the program is run. Follow the directions printed to the terminal. First set the game settings. Then input moves as a single number 0 to 6 each turn and play the game. No additional code is needed to run the program.

Suggestions

Finish the difficulies for the bot. Finish the customization for the player settings. Run the game using pygame to make it look prettier and make it feel more like a game.


--------------------------------------
# Project Proposal
1. Who is on your team?

Just me (Owen Chun). :)

2. An overview of the project similar in scope and length to the example projects listed below.

Connect four is a two-player game. The board is a 7x6 grid. Each player takes turns dropping a piece into a column with the goal of getting four of their own pieces in a row either horizontally, vertically, or diagonally. The game ends in a draw if the board is filled with no winner.

Write a program to run a game of connect four against a bot or another user. To run the game properly, the program must keep track of the pieces placed and update the board each turn. The program must recognize when someone wins by getting four of their pieces in a row horizontally, vertically, or diagonally. The user should be able to select the difficulty of the bot: Genius, Normal, and Noob. With genius, the bot should almost never lose if it goes first. With normal, the bot will won't make obvious mistakes like ignoring a 3-in-a-row or letting the user get a 3-in-row on the bottom with both sides open. With noob, the bot basically plays randomly.

3. A short description of the structure of your project. How many classes will you write? What the methods be for each class? (You can change this if it turns out a better structure would work better once you start writing code and you decide to refactor. Just try to come up with a reasonable one for the proposal.)

There will be a class for the bot with a property for its difficulty and a method to set it. It will also have a method to analyze the board and make a move.
There will be a class for the board with a property that will contain an array of all the board spaces. There will be a method to run a turn that will take in a column where a piece is placed, insert the piece into the array, and check if there is a win. The board will have a boolean property for if the user wants to face a bot or another user. 

4. What libraries and tools will you need to learn to use?

I will use the random and possibly math libraries.
I might learn how to use pygame to run the game instead of just displaying it to the terminal each turn.

5. Identify the highest-priority features, the medium-priority features, and the lowest-priority features for your project.

High-priority:
  - Working connect four game
    - Board updates correctly after each turn
    - Display updated board to console each turn
    - Ends properly
      - Win when someone gets at least 4 in a row
      - Draw when board is full with no winner
  - Working bot the user can play against (that doesn't just place randomly)
  - Different difficulty settings for the bot: Genius, Normal, and Noob

Medium-priority:
 - Different difficulty settings for the bot: Easy, Normal, Hard
  - Allows two users to play against each other
  - Change number of rounds for each game (Win best of 3, 5, etc. instead of just 1 round)

Low-priority:
  - Customizable game (user can change symbols representing the pieces)
  - Fun win message (or loss or draw message)
  - Bot makes comments throughout the game
  - Display the game with pygame
