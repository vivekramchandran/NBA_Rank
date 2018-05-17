# Project Outline

This project's goal is to be able to do Win Probability estimates for a given game, potentially rank players,
determine players that will compliment each others' strengths, as well as answer difficult specific questions
about the importance of different parts of the game.

## Steps

### Pick Different Statistics/Features

The data that will be used will include all public statistical information such as Basketball-Reference.com
and nbastuffer.com, as well as the player tracking data provided by STATS LLC.  This data should be available
in the next couple of  days, and the list of features that can be modelled can be finalized then.  Until then,
I am not entirely sure which of my desired features will be able to be successfully modelled, but below is a
tentative list:

Scoring

Passing

Fouls Created

Attacking with Numbers

Range/Defensive Gravity

Screening Quality

Off-Ball Movement

Ability to Create Space

Defensive Pull

Offesnive Rebounding

Transition Offense

Success Attacking Switches

Transition Defense

Ability to Switch

Rim Protection

One-on-one defense

Rebounding/Boxing Out

Win Score (Wins Produced)

True Shooting Percentage

Usage Percentage

Note that some of these are just basic statistics that can be found anywhere, others will be weighted combinations
of common statistics and player movement data, and some are solely based on the player movement data.

### Create Graphs for each statistic/feature

Each one of these statistics will have their own graph for each team.  Each player will be represented as a node,
with the node containing a value taht will represent each players' value in that statistic.  Weighted edges will
represent the ranking and relationship between each player in terms of that given statistic.  The weights of these
graphs will need to be trained over the course of at least one seasons worth of data.  The connectivity of each of
these graphs will be represented as an adjacency matrix.  If the matrix is too dense, then techniques to sparcify
the graphs will occur.

### Visualize each player and each Team

This step will require that all of the nodes representing a player be combined into a single graph.  This might require
the use of Graph Embedding to map the graph to a vector space in order to work with the data more easily.  It is likely
that a 3-D Space representing different statistics will need to be used as a benchmark for each of the individual player
graphs.  Once each of the player graphs are created, a general team graph will need to be created.  Each players visualized
graph will dictate how the team fits together, and the graph will hopefully show what players result in which specific 
team aspects.

### Perform Further Tasks

When this step is reached, the model will be well equipped to start testing.  Game by Game win Probabilities and Predictions
will certainly be one thing that is tested.  The goal will be to be more accurate than high level predictions shown on Five
Thirty Eight's NBA Statistical model.  Player ranking will likely occur, but instead of straight forward ranking, it will be more of a comparison of strengths and weaknesses.  Different questions about the NBA could be answered:  What players are built to thrive in the Playoffs vs. the regular season, or what are statistics that correlate with high contracts, etc.  Furthermore, this model will be perfect for an NBA General Manager to visualize how to improve and maximize a team.  Potentially, an ideal team set up could be created, defining the exact type of players to surround different players with to
optimize a team.
