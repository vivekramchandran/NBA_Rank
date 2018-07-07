import numpy as np 
import pandas as pd 
import csv
import io
import re
import json
'''
All files are the following:
general_traditional.csv 26 columns of note 0-25
general_advanced.csv 15 columns of note 26-40
general_scoring.csv 15 columns of note 41-55
general_defense.csv 7 columns of note 56-62
general_opponent.csv 21 columns of note 63-83
player_shooting.csv 18 columns of note 84-101
opponent_shooting.csv 18 columns of note 102-119
clutch_traditional.csv 9 columns of note 120-128
hustle.csv 7 columns of note 129-135
P%RBallHandler.csv 13 columns of note 136-148
P%RRollMan.csv 13 columns of note 149-161
Playtype_Isolation.csv 13 columns of note 162-174
Playtype_Post_Up.csv 13 columns of note 175-187
Playtype_Transition.csv 13 columns of note 188-200
Tracking_Catch&Shoot.csv 8 columns of ntoe 201-208
Tracking_Drives.csv 17 columns of note 209-225
Tracking_Passes.csv 8 columns of note 226-233
Tracking_Speed&Distance.csv 7 columns of note 234-240

['PLAYER','TEAM','AGE','GP','W','L','MIN','PTS','FGM','FGA','FG%', '3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','TOV',
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
  'CONT 2PT SHOT', 'CONT 3PT SHOT', 'CONT SHOT', 'P&R BH POSS', 'P&R BH FREQ', 'P&R BH PPP', 'P&R BH  PTS', 'P&R BH FGM', 'P&R BH FGA',
  'P&R BH FG%', 'P&R BH EFG%', 'P&R BH FT', 'P&R BH FT FREQ', 'P&R BH TO FREQ', 'P&R BH SF FREQ', 'P&R BH AND ONE FREQ', 'P&R BH SCORE',
  'P&R RM POSS', 'P&R RM FREQ', 'P&R RM PPP', 'P&R RM PTS', 'P&R RM FGM', 'P&R RM FGA', 'P&R RM FG%', 'P&R RM EFG%', 'P&R RM FT',
  'P&R RM FT FREQ', 'P&R RM TO FREQ', 'P&R RM SF FREQ', 'P&R RM AND ONE FREQ', 'P&R RM SCORE', 'ISO POSS', 'ISO FREQ', 'ISO PPP',
  'ISO PTS', 'ISO FGM', 'ISO FGA', 'ISO FG%', 'ISO EFG%','ISO FT FREQ', 'ISO TO FREQ', 'ISO SF FREQ', 'ISO AND ONE FREQ',
  'ISO SCORE', 'POST UP POSS', 'POST UP FREQ', 'POST UP PPP', 'POST UP PTS', 'POST UP FGM', 'POST UP FGA', 'POST UP FG%', 'IPOST UP EFG%',
  'POST UP FT FREQ', 'POST UP TO FREQ', 'POST UP SF FREQ', 'POST UP AND ONE FREQ', 'POST UP SCORE', 'TRANS POSS', 'TRANS FREQ',
  'TRANS PPP', 'TRANS PTS', 'TRANS FGM', 'TRANS FGA', 'TRANS FG%', 'TRANS EFG%','TRANS FT FREQ', 'TRANSTO FREQ', 'TRANS SF FREQ',
  'TRANS AND ONE FREQ', 'TRANS SCORE','C&S PTS', 'C&S FGM', 'C&S FGA', 'C&S FG%', 'C&S 3PM', 'C&S 3PA', 'C&S 3P%', 'C&S EFG%', 'DRIVE #',
  'DRIVE FGM','DRIVE FGA', 'DRIVE FG%', 'DRIVE FTM','DRIVE FTA', 'DRIVE FT%','DRIVE PTS','DRIVE PTS%','DRIVE PASS','DRIVE PASS%',
  'DRIVE AST','DRIVE AST%','DRIVE TO','DRIVE TOV%','DRIVE PF', 'DRIVE PF%','PASSES MADE', 'PASSES RECEIVED','AST SECONDARY','AST POTENTIAL',
  'AST', 'AST ADJ','AST TO PASS%','AST TO PASS% ADJ','DIST. FEET','DIST. MILES', 'DIST. MILES OFF','DIST. MILES DEF','AVG SPEED',
  'AVG SPEED OFF','AVG SPEED DEF']
'''


def make_matrix():
	# Number of players
	num_players = 540

	# Number of columns describing each player
	num_cols = 241

	data = create_matrix(num_players,num_cols)

	data = pop_gen_stats(data)

	return data


def pop_gen_stats(data):

	data = gen_trad(data)
	data = gen_adv(data)
	data = gen_scor(data)
	data = gen_def(data)
	data = gen_opp(data)
	data = play_shoot(data)
	data = opp_shoot(data)
	data = clutch_trad(data)
	data = hustle(data)
	data = P_RBall_Hand(data)
	data = P_RRoll(data)
	data = Iso(data)
	data = PostUp(data)
	data = transition(data)
	data = catch_shoot(data)
	data = drives(data)
	data = passes(data)
	data = movement(data)

	return data



'''
Tracking_Speed&Distance.csv
'''
def movement(data):
	filename = all_files(17)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))

	factor = 228
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (6, 13):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data

'''
Tracking_Passes.csv
'''
def passes(data):
	filename = all_files(16)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))

	factor = 220
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (6, 14):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data



'''
Tracking_Drives.csv
'''
def drives(data):
	filename = all_files(15)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))

	factor = 203
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (6, 23):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data


'''
Tracking_Catch&Shoot.csv
'''
def catch_shoot(data):
	filename = all_files(14)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))

	factor = 197
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (4, 12):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data



'''
Playtype_Transition.csv
'''
def transition(data):
	filename = all_files(13)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))

	factor = 185
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (3, 16):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data


'''
Playtype_Post_Up.csv
'''
def PostUp(data):
	filename = all_files(12)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))

	factor = 172
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (3, 16):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data

'''
Playtype_Isolation.csv
'''
def Iso(data):
	filename = all_files(11)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))
	
	factor = 159
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (3, 16):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data
	



'''
P&RRollMan.csv
'''
def P_RRoll(data):
	filename = all_files(10)
	temp_data = np.array(pd.read_csv(filename, encoding = 'latin1'))

	factor = 146
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (3, 16):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data




'''
P&RBallHandler.csv

'''
def P_RBall_Hand(data):
	filename = all_files(9)
	temp_data = [['Jeremy Lin','BKN',1, 14, .778, 1.14, 16.0, 4.0, 9.0, 44.0, 50.0, .214, .143, .071, 0, .5]]
	size = len(temp_data[0])
	reader = np.array(pd.read_csv(filename, encoding = 'latin1'))
	for row in reader:
		temp_data.append(row)

	temp_data[25][0] = "D'Angelo Russell"
	temp_data[30][0] = "De'Aaron Fox"
	temp_data[34][0] = 'Zach LaVine'
	temp_data[55][0] = "D.J. Augustin"
	temp_data[122][0] = "DeAndre' Bembry"

	factor = 133
	for i in range (0, len(temp_data)):
		temp_ind = find_player(temp_data[i][0], data)
		for j in range (3, 16):
			data[j + factor][temp_ind] = temp_data[i][j]
	
	return data	





'''
hustle.csv
'''
def hustle(data):
	filename = all_files(8)
	temp_data = read_in_ind(filename)
	factor = 124

	for i in range (1, len(temp_data[0])):
		temp_ind = find_player(temp_data[0][i], data)
		for j in range (5, 12):
			data[j + factor][temp_ind] = temp_data[j][i]
	
	return data




'''
clutch_traditional.csv
'''
def clutch_trad(data):
	filename = all_files(7)
	temp_data = read_in_ind(filename)
	for i in range (1, len(temp_data[0])):
		temp_ind = find_player(temp_data[1][i], data)
		# GP
		data[120][temp_ind] = temp_data[4][i]
		# MIN
		data[121][temp_ind] = temp_data[7][i]
		# PTS
		data[122][temp_ind] = temp_data[8][i]
		# FGA
		data[123][temp_ind] = temp_data[10][i]
		# FG%
		data[124][temp_ind] = temp_data[11][i]
		# 3PA
		data[125][temp_ind] = temp_data[13][i]
		# 3P%
		data[126][temp_ind] = temp_data[14][i]
		# FTA
		data[127][temp_ind] = temp_data[16][i]
		# FT%
		data[128][temp_ind] = temp_data[17][i]

	return data



'''
Opponent_Shooting.csv
'''
def opp_shoot(data):
	filename = all_files(6)
	temp_data = read_in_ind(filename)
	factor = 99

	for i in range (1, len(temp_data[0])):
		temp_ind = find_player(temp_data[0][i], data)
		for j in range (3, 21):
			data[j + factor][temp_ind] = temp_data[j][i]
	
	return data

'''
Player_Shooting.csv
'''
def play_shoot(data):
	filename = all_files(5)
	temp_data = read_in_ind(filename)
	factor = 81

	for i in range (1, len(temp_data[0])):
		temp_ind = find_player(temp_data[0][i], data)
		for j in range (3, 21):
			data[j + factor][temp_ind] = temp_data[j][i]
	
	return data

'''
general_opponent.csv
'''
def gen_opp(data):
	filename = all_files(4)
	temp_data = check_dup(read_in_ind(filename))
	factor = 56
	for i in range (1, len(temp_data)):
		play_name = conv_name(temp_data[i][1])
		temp_ind = find_player(play_name, data)
		for j in range (7, 28):
			data[j + factor][temp_ind] = temp_data[i][j]

	return data
			

'''
Find Duplicates and Merge them data wise
'''
def check_dup(data):

	new_data = [row(data, 0)]
	cnt = 0
	cnt2 = 0
	for i in range (1, len(data)):
		temp_line = row(data, i)
		for j in range (i+1, len(data)):
			if data[1][i] == data[1][j]:
				cnt += 1
				temp_line = comb_lines(temp_line,row(data,j))
				data[0][j] = -1

		#print(data)
		if data[0][i] != -1:
			cnt2 += 1
			new_data.append(temp_line)

	return new_data

'''
Combines two data points in a weighted fashion
'''
def comb_lines(dp1, dp2):
	new_line = dp1
	raw1 = float(dp1[3])*float(dp1[6])
	raw2 = float(dp2[3])*float(dp2[6])

	w1 = raw1/(raw1+raw2)
	w2 = 1 - w1


	# Reset the games played and minutes values
	new_line[3] = int(dp1[3]) + int(dp2[3])
	new_line[6] = w1*float(dp1[6]) + w2*float(dp2[6])

	for j in range (7, 28):
		new_line[j] = w1*float(dp1[j]) + w2*float(dp2[j])

	return new_line





'''
Convert Name Format
'''
def conv_name(name):
	last_first = [x.strip() for x in name.split(',')]
	if len(last_first) == 2:
		new_name = last_first[1]+' '+last_first[0]
	else:
		new_name = last_first[0]
	return new_name

'''
general_defense,csv
'''
def gen_def(data):
	filename = all_files(3)
	temp_data = read_in_ind(filename)
	for i in range (1, len(temp_data[1])):
		temp_ind = find_player(temp_data[1][i], data)
		j = 13
		factor = 43
		while (j < 21):
			if (j == 14):
				j += 1
				factor -= 1
			data[j + factor][temp_ind] = temp_data[j][i]
			j = j + 1
	return data


'''
general_scoring.csv
'''
def gen_scor(data):
	filename = all_files(2)
	temp_data = read_in_ind(filename)
	factor = 33

	for i in range (1, len(temp_data[1])):
		temp_ind = find_player(temp_data[1][i], data)
		for j in range (8, 23):
			data[j + factor][temp_ind] = temp_data[j][i]
	

	return data


'''
general_advanced.csv
'''
def gen_adv(data):
	filename = all_files(1)
	temp_data = read_in_ind(filename)
	factor = 18

	# No duplicate names
	for i in range (1, len(temp_data[1])):
		temp_ind = find_player(temp_data[1][i], data)
		for j in range (8, 23):
			data[j + factor][temp_ind] = temp_data[j][i]
	
	return data


'''
general_traditional.csv 
'''
def gen_trad(data):
	filename = all_files(0) 
	temp_data = read_in_ind(filename)
	i = 1
	factor = 1
	while (i < 30):
		if (i == 26):
			i += 3
			factor += 3
		for j in range (1, len(temp_data[i])):
			data[i-factor][j - 1] = temp_data[i][j]
		i += 1
	return data


'''
Returns the index in data where a player is
'''
def find_player(play_name, data):

	# Try to match names
	for i in range (0, len(data[0])):
		if (play_name == data[0][i]):
			return i
	
	# If cannot find the name
	exit_msg = f"{play_name} cannot be found in previous data"
	print(exit_msg)
	exit()

'''
Creates empty matrix populated with -1 of the correct size
'''
def create_matrix(num_players, num_cols):
	matrix_data = []

	# populate data with -1
	for i in range (0, num_cols):
		matrix_data.append([])
		for j in range (0, num_players):
			matrix_data[i].append(-1)
	
	return matrix_data

'''
Returns specific file to be read in
'''
def all_files(i):
	all_filenames = ['general_traditional.csv', 'general_advanced.csv', 'general_scoring.csv', 'general_defense.csv',
				 'general_opponent.csv', 'Player_Shooting.csv', 'Opponent_Shooting.csv', 'clutch_traditional.csv',
				 'hustle.csv', 'P&RBallHandler.csv', 'P&RRollMan.csv', 'Playtype_Isolation.csv', 'Playtype_Post_Up.csv',
				 'Playtype_Transition.csv', 'Tracking_Catch&Shoot.csv', 'Tracking_Drives.csv', 'Tracking_Passes.csv',
				 'Tracking_Speed&Distance.csv']

	if 0 <= i < 18:
		return all_filenames[i]
	else:
		print("File is out of range")
		exit()
	

def read_in_ind(filename):
	data = pd.read_csv(filename, header=None)
	return data

'''
Row used to find player
'''
def player_row(data, index):
	temp_play = []
	for i in range (0, len(data)):
		temp_play.append(data[i][index])
	return temp_play

'''
Row used in specific format to find duplicates
'''
def row(data, j):
	row = []
	num_cols = int(np.size(data)/len(data))
	for i in range (0, num_cols):
		row.append(data[i][j])
	return row

