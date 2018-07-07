This is a short explanation for the process of parsing and setting up the metrics.

First, a number of different webpages at stats,nba/... were parsed and saved by reusing the code at the following link:
https://github.com/royh21k/royh21k.github.io/tree/master/nbawebscrape%20and%20analysis/scraper%20and%20data%20cleaning.  There were some slight modifications to each of the scripts to account for the different webpages as well as some changes that have been made to the stats.nba webpage.  All of the CSV files were saved in the folder.
 
From the CSV's, certain statistical columns were read in for each player.  Those statistics were then combined to form metrics.  Some metrics are just statistics (points, pace, etc), while others are weighted combinations of different advanced statistics.  Those metrics were then written to metrics.csv.
