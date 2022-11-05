# Connect-Four
EECE2140: Final Project - Connect Four

Project Proposal
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
  - Allows two users to play against each other
  - Change number of rounds for each game (Win best of 3, 5, etc. instead of just 1 round)

Low-priority:
  - Customizable game (user can change symbols representing the pieces)
  - Fun win message (or loss or draw message)
  - Bot makes comments throughtout the game
  - Display the game with pygame
