import scraper as scr
import metrics as met
import numpy as np
import math


'''

All files are the following:
general_traditional.csv
general_advanced.csv
general_scoring.csv
general_defense.csv
general_opponent.csv
player_shooting.csv
opponent_shooting.csv
clutch_traditional.csv
hustle.csv
P%RBallHandler.csv
P%RRollMan.csv
Playtype_Isolation.csv
Playtype_Post_Up.csv
Playtype_Transition.csv
Tracking_Catch&Shoot.csv
Tracking_Drives.csv
Tracking_Passes.csv
Tracking_Speed&Distance.csv

'''
headers = ['PLAYER','TEAM','AGE','GP','W','L','MIN','PTS','FGM','FGA','FG%', '3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','TOV',
 'STL','BLK','PF','+/-', 'OFFRTG', 'DEFRTG', 'NETRTG', 'AST%', 'AST/TO', 'AST RATIO', 'OREB%', 'DREB%', 'REB%', 'TO RATIO', 'EFG%', 'TS%',
 'USG%', 'PACE', 'PIE','%FGA 2PT','%FGA 3PT','%PTS 2PT', '%PTS 2PT MR', '%PTS 3PT', '%PTS FBPS', '%PTS FT', '%PTS OFFTO', '%PTS PITP',
 '2FGM %AST','2FGM %UAST', '3FGM %AST', '3FGM %UAST', 'FGM %AST', 'FGM %UAST', 'STL%', '%BLK', 'OPP PTS OFF TOV', 'OPP PTS 2ND CHANCE',
  'OPP PTS FB', 'OPP PTS PAINT', 'DEF WS', 'OPP FGM', 'OPP FGA', 'OPP FG%', 'OPP 3PM', 'OPP 3PA', 'OPP 3P%', 'OPP FTM', 'OPP FTA', 'OPP FT%',
  'OPP OREB', 'OPP DREB', 'OPP REB', 'OPP AST', 'OPP TOV', 'OPP STL', 'OPP BLK', 'OPP BLKA', 'OPP PF', 'OPP PFD', 'OPP PTS', 'OPP +/-',
  '<5 FGM', '<5 FGA', '<5 FG%', '5-9 FGM', '5-9 FGA', '5-9 FG%', '10-14 FGM', '10-14 FGA', '10-14 FG%', '15-19 FGM', '15-19 FGA', '15-10 FG%',
  '20-24 FGM', '20-24 FGA', '20-24 FG%', '25-29 FGM', '25-29 FGA', '25-29 FG%','OPP <5 FGM', 'OPP <5 FGA', 'OPP <5 FG%', 'OPP 5-9 FGM',
  'OPP 5-9 FGA', 'OPP 5-9 FG%', 'OPP 10-14 FGM', 'OPP 10-14 FGA', 'OPP 10-14 FG%', 'OPP 15-19 FGM', 'OPP 15-19 FGA', 'OPP 15-10 FG%',
  'OPP 20-24 FGM', 'OPP 20-24 FGA', 'OPP 20-24 FG%', 'OPP 25-29 FGM', 'OPP 25-29 FGA', 'OPP 25-29 FG%', 'CLU GP', 'CLU MIN', 'CLU PTS', 
  'CLU FGA', 'CLU FG%', 'CLU 3PA', 'CLU 3P%', 'CLU FTA', 'CLU FT%', 'SCREEN ASSISTS', 'DEFLECTIONS', 'LOOSE BALL REC', 'CHARGES DRAWN',
  'CONT 2PT SHOT', 'CONT 3PT SHOT', 'CONT SHOT', 'P&R BH POSS', 'P&R BH FREQ', 'P&R BH PPP', 'P&R BH PTS', 'P&R BH FGM', 'P&R BH FGA',
  'P&R BH FG%', 'P&R BH EFG%', 'P&R BH FT FREQ', 'P&R BH TO FREQ', 'P&R BH SF FREQ', 'P&R BH AND ONE FREQ', 'P&R BH SCORE',
  'P&R RM POSS', 'P&R RM FREQ', 'P&R RM PPP', 'P&R RM PTS', 'P&R RM FGM', 'P&R RM FGA', 'P&R RM FG%', 'P&R RM EFG%',
  'P&R RM FT FREQ', 'P&R RM TO FREQ', 'P&R RM SF FREQ', 'P&R RM AND ONE FREQ', 'P&R RM SCORE', 'ISO POSS', 'ISO FREQ', 'ISO PPP',
  'ISO PTS', 'ISO FGM', 'ISO FGA', 'ISO FG%', 'ISO EFG%','ISO FT FREQ', 'ISO TO FREQ', 'ISO SF FREQ', 'ISO AND ONE FREQ',
  'ISO SCORE', 'POST UP POSS', 'POST UP FREQ', 'POST UP PPP', 'POST UP PTS', 'POST UP FGM', 'POST UP FGA', 'POST UP FG%', 'IPOST UP EFG%',
  'POST UP FT FREQ', 'POST UP TO FREQ', 'POST UP SF FREQ', 'POST UP AND ONE FREQ', 'POST UP SCORE', 'TRANS POSS', 'TRANS FREQ',
  'TRANS PPP', 'TRANS PTS', 'TRANS FGM', 'TRANS FGA', 'TRANS FG%', 'TRANS EFG%','TRANS FT FREQ', 'TRANSTO FREQ', 'TRANS SF FREQ',
  'TRANS AND ONE FREQ', 'TRANS SCORE','C&S PTS', 'C&S FGM', 'C&S FGA', 'C&S FG%', 'C&S 3PM', 'C&S 3PA', 'C&S 3P%', 'C&S EFG%', 'DRIVE #',
  'DRIVE FGM','DRIVE FGA', 'DRIVE FG%', 'DRIVE FTM','DRIVE FTA', 'DRIVE FT%','DRIVE PTS','DRIVE PTS%','DRIVE PASS','DRIVE PASS%',
  'DRIVE AST','DRIVE AST%','DRIVE TO','DRIVE TOV%','DRIVE PF', 'DRIVE PF%','PASSES MADE', 'PASSES RECEIVED','AST','AST SECONDARY','AST POTENTIAL',
  'AST ADJ','AST TO PASS%','AST TO PASS% ADJ','DIST. FEET','DIST. MILES', 'DIST. MILES OFF','DIST. MILES DEF','AVG SPEED',
  'AVG SPEED OFF','AVG SPEED DEF']

data = scr.make_matrix()

met.make_metrics(data)


def find_player(play_name):
	index = scr.find_player(play_name, data)
	return scr.player_row(data, index)




















