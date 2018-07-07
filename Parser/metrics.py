import numpy as np
import pandas as pd
import math
from itertools import islice
import csv
from operator import itemgetter, attrgetter

'''
Metrics:
Total Movement -
Passing -
Attacking Basket -
Spacing -
Transition -
Post Shot Creation -
Isolation Ability - 
P&R Ball Handler -
P&R Roll Man -
Screening -
Help Defense(/Defensive Cheating) -
Shot Contest - 
Clutch Factor -
Interior Scoring -
Mid Range Scoring -
3 Point Scoring - 
Points - 
Rebounding - 
Net_Rating - 
Pace - 
Plus_Minus_Aggregate - 
Usage Rate -
Defensive_stats -


Things needed - Switchability
'''


def make_metrics(data):
	# Key of Metric Names
	Metric_Names = ["Player", "Team", "Movement", "Passing", "Attack_Basket", "CASSpacing", "Transition", 
					"Post_Up", "Isolation", "Roll_Man", "PARBall_Handler", "Screen", "Help_Def", "Shot_Contest",
					"Clutch", "Interior_Score", "Midrange", "Long_Range", "Points", "Rebounds", "Net_Rating", "Pace",
					"Plus_Minus", "Usage", "Defense_Aggregate"]
	# Metric Values to be filled up
	Met_Dat = []
	# Set the first column to be the player names
	Met_Dat.append(data[0])

	# Set the second column to be the player TEAMS
	Met_Dat.append(data[1])

	data.append(min_minutes(data))
	
	# Movement Column
	Met_Dat.append(movement(data))

	# Passing Column
	Met_Dat.append(passing(data))

	# Attack Basket 
	Met_Dat.append(attack_basket(data))

	# C&S Spacing
	Met_Dat.append(casspacing(data))

	# Transition
	Met_Dat.append(transition(data))

	# Post Up
	Met_Dat.append(postup(data))

	# Isolation
	Met_Dat.append(isolation(data))

	# Pick and Roll Roll Man
	Met_Dat.append(roll_man(data))

	# Pick and Roll Ball Handler
	Met_Dat.append(ball_handler(data))

	# Screen
	Met_Dat.append(screen(data))

	# Help_Defense
	Met_Dat.append(Help_Def(data))

	# Contesting Shots
	Met_Dat.append(Shot_Contest(data))

	# Clutch
	Met_Dat.append(Clutch(data))

	# Interior Scoring
	Met_Dat.append(Interior(data))

	# Mid Range Scoring
	Met_Dat.append(midrange(data))

	# Deep Scoring
	Met_Dat.append(long_range(data))

	# Points
	Met_Dat.append(points(data))

	# Rebounds
	Met_Dat.append(rebounds(data))

	# Net Rating
	Met_Dat.append(netrtg(data))

	# Pace Rating
	Met_Dat.append(pace(data))

	# Plus_Minus
	Met_Dat.append(plus_minus(data))

	# Usage
	Met_Dat.append(usage(data))

	# Defensive Stats Aggregate
	Met_Dat.append(defense_aggregate(data))
	
	#test_metric(Met_Dat[0], Met_Dat[23])

	my_dict = dict(zip(Metric_Names, Met_Dat))
	df = pd.DataFrame(my_dict, columns = Metric_Names)
	df.to_csv('metrics.csv')

	# print(len(Met_Dat), len(Metric_Names))
	# my_dict = dict(zip(Metric_Names, Met_Dat))

	# print(my_dict)
	# with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
	#     w = csv.DictWriter(f, my_dict.keys())
	#     w.writeheader()
	#     for i in range (0, len(Met_Dat))
	#     w.writerow(my_dict)

'''
Defensive Stats
Formula: Win_Shares * (STL + BLOCK)
'''
def defense_aggregate(data):
	def_aggr = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			def_aggr.append(-1)
		else:
			ws = float(data[62][i])
			if (ws < 0):
				ws = .0001
			ws *= 100
			temp = (float(data[22][i]) + float(data[23][i])) * ws
			def_aggr.append(temp)

	return def_aggr



'''
Usage Rate Metric
Formula: Usage
'''
def usage(data):
	usage = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			usage.append(-1)
		else:
			temp = float(data[38][i])
			usage.append(temp)

	return usage

'''
Plus_Minus
Formula: +/- - (Opp +/-)
'''
def plus_minus(data):
	plus_minus = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			plus_minus.append(-1)
		else:
			temp = float(data[25][i]) - float(data[83][i])
			plus_minus.append(temp)

	return plus_minus	

'''
Pace Metric
Formula: Pace
'''
def pace(data):
	pace = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			pace.append(-1)
		else:
			temp = float(data[39][i])
			pace.append(temp)

	return pace	




'''
Net Rating Metric
Formula: Net Rating (OFF RTG - DEF RTG)

'''
def netrtg(data):
	netrtg = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			netrtg.append(-1)
		else:
			temp = float(data[28][i])
			netrtg.append(temp)

	return netrtg





'''
Rebounds Metric
Formula: (.9 * OREB) + (REB) + (.25 * REB%)
'''
def rebounds(data):
	rebounds = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			rebounds.append(-1)
		else:
			temp = (.9 * float(data[17][i])) + (float(data[18][i])) + \
				   (.25*float(data[34][i]))
			rebounds.append(temp)

	return rebounds




'''
Points Metric
Formula: PPG
'''
def points(data):
	points = []
	num_play = len(data[0])

	for i in range (0, num_play):
		temp = float(data[7][i])
		points.append(temp)

	return points


'''
Long Range Scoring 84-101
Formula is: (.1 * FGA * FG%) + (.1 * FGA * FG%) (for 20-24 and 25-29)
'''
def long_range(data):
	long = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			long.append(-1)
		else:
			temp = (.1 * float(data[97][i]) * float(data[98][i])) + \
				   (.1 * float(data[100][i]) * float(data[101][i]))
			long.append(temp)
	return long



'''
Mid Range Scoring 84-101
Formula is: (.1 * FGA * FG%) + (.1 * FGA * FG%) (for 10-14 and 15-19)
'''
def midrange(data):
	midrange = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			midrange.append(-1)
		else:
			temp = (.1 * float(data[91][i]) * float(data[92][i])) + \
				   (.1 * float(data[94][i]) * float(data[95][i]))
			midrange.append(temp)
	return midrange


'''
Interior Scoring 84-101

Formula is: (.1 * FGA * FG%) + (.1 * FGA * FG%) (for 5-9 and <5)

'''
def Interior(data):
	interior = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			interior.append(-1)
		else:
			temp = (.1 * float(data[85][i]) * float(data[86][i])) + \
				   (.1 * float(data[88][i]) * float(data[89][i]))
			interior.append(temp)
	return interior	





'''
Clutch
Formula is:
(PTS) + (.05 * FG%)
'''
def Clutch(data):
	clutch = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			clutch.append(-1)
		elif ((float(data[120][i]) * float(data[121][i])) < 30):
			clutch.append(-1)
		else:
			temp = float(data[122][i]) + (.05 * float(data[124][i]))
			clutch.append(temp)
	return clutch


'''
Contesting Shots
Formula is: ((1.25 * Contested 2 Point Shots) + 
			(1.5 * Contested 3 Point Shots)) / (minutes ^ 3)
'''
def Shot_Contest(data):
	shot_cont = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			shot_cont.append(-1)
		else:
			temp = ((1.25 * float(data[133][i])) + \
					(1.5 * float(data[134][i])))/((np.cbrt(float(data[6][i]))))
			shot_cont.append(temp)
	return shot_cont





'''
Help_Defense
Formula is: (1.2 * Deflections) + (1.5 * Loose Balls) + (Charges Drawn)
'''
def Help_Def(data):
	help_def = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			help_def.append(-1)
		else:
			temp = (1.2 * float(data[130][i])) + (1.5 * float(data[131][i])) + float(data[132][i])
			help_def.append(temp)

	return help_def		




'''
Screening
Formula is: Screen Assists
'''
def screen(data):
	screen = []
	num_play = len(data[0])

	for i in range (0, num_play):
		if (data[241][i] == -1):
			screen.append(-1)
		else:
			temp = float(data[129][i])
			screen.append(temp)
	return screen

'''
PaRBall_Handler 149-161
Formula is:
	((POSS * PPP) + (.015 * EFG%) - (.075 * TOV) + (.01 * SF DRAWN)) + (.025 * SCORE)
'''
def ball_handler(data):
	ballh = []
	num_play = len(data[0])


	for i in range (0, num_play):
		#print(i)
		if (data[241][i] == -1):
			ballh.append(-1)
		elif (data[145][i] == -1):
			ballh.append(-1)
		elif (((data[138][i]) > 1.7) or (float(data[148][i]) >= 95)):
			ballh.append(-1)
		else:
			temp = ((data[136][i] * data[138][i]) + (.015*data[143][i]) - (7.5 * float(data[145][i])) + \
				   (float((data[146][i])))) + (2.5 * float(data[148][i]))

			ballh.append(temp)
	
	return ballh



'''
PaRRollMan 149-161
Formula is:
	((POSS * PPP) + (.015 * EFG%) - (.075 * TOV) + (.01 * SF DRAWN)) + (.025 * SCORE)

'''
def roll_man(data):
	rollm = []
	num_play = len(data[0])

	for i in range (0, num_play):
		#print(i)
		if (data[241][i] == -1):
			rollm.append(-1)
		elif (data[158][i] == -1):
			rollm.append(-1)
		elif ((data[151][i]) > 1.7 or (float(data[161][i][:-1])) >= 95):
			rollm.append(-1)
		else:
			temp = ((data[149][i] * data[151][i]) + (.015*data[156][i]) - (.075 * float(data[158][i][:-1])) + \
				   (.01*float((data[159][i][:-1])))) + (.025 * float(data[161][i][:-1]))

			rollm.append(temp)
	
	return rollm




'''
Isolation Metric 162-174
Formula is:
	((POSS * PPP) + (.015 * EFG%) - (.075 * TOV) + (.01 * SF DRAWN)) + (.025 * SCORE)

'''
def isolation(data):
	iso = []
	num_play = len(data[0])

	for i in range (0, num_play):
		#print(i)
		if (data[241][i] == -1):
			iso.append(-1)
		elif (data[171][i] == -1):
			iso.append(-1)
		elif ((data[164][i]) > 1.7 or (float(data[174][i][:-1])) >= 95):
			iso.append(-1)
		else:
			temp = ((data[162][i] * data[164][i]) + (.015*data[169][i]) - (.075 * float(data[171][i][:-1])) + \
				   (.01*float((data[172][i][:-1])))) + (.025 * float(data[174][i][:-1]))

			iso.append(temp)
	
	return iso


'''
Post Up Metric
Formula is:
	((POSS * PPP) + (.015 * EFG%) - (.075 * TOV) + (.01 * SF DRAWN)) + (.025 * SCORE)
'''
def postup(data):
	postup = []
	num_play = len(data[0])

	for i in range (0, num_play):
		#print(i)
		if (data[241][i] == -1):
			postup.append(-1)
		elif (data[184][i] == -1):
			postup.append(-1)
		elif ((data[177][i]) > 1.7 or (float(data[187][i][:-1])) >= 95):
			postup.append(-1)
		else:
			temp = ((data[175][i] * data[177][i]) + (.015*data[182][i]) - (.075 * float(data[184][i][:-1])) + \
				   (.01*float((data[185][i][:-1])))) + (.025 * float(data[187][i][:-1]))

			postup.append(temp)
	
	return postup





'''
Transition Metric
Formula is: 
	((POSS * PPP) + (.015 * EFG%) - (.075 * TOV) + (.01 * SF DRAWN)) + (.025 * SCORE)
'''
def transition(data):
	transition = []
	num_play = len(data[0])

	for i in range (0, num_play):
		#print(i)
		if (data[241][i] == -1):
			transition.append(-1)
		elif (data[197][i] == -1):
			transition.append(-1)
		elif ((data[190][i]) > 1.7 or (float(data[200][i][:-1])) >= 95):
			transition.append(-1)
		else:
			temp = ((data[188][i] * data[190][i]) + (.015*data[195][i]) - (.075 * float(data[197][i][:-1])) + \
				   (.01*float((data[198][i][:-1])))) + (.025 * float(data[200][i][:-1]))

			transition.append(temp)
	
	return transition


'''
Spacing Metric
Formula is: (.6 * Points) + (.015 * (3P% * 3PM)) + (.1 * EFG%)
'''
def casspacing(data):
	space = []
	num_play = len(data[0])
	for i in range (0, num_play):
		if (data[241][i] == -1):
			space.append(-1)
		else:
			temp = (.6 * data[201][i]) + (.015 * data[206][i]*data[207][i]) \
					+ (.1*data[208][i])
			space.append(temp)
	
	return space






'''
Attack Basket Metric:
Formula is 
	((Drives * .35) + (.075 * (DRIVE FGA)(DRIVE FG% - 46)) +
	(1.25 * AST) - (TOV + PF)) / ((MIN ^ 2) / 10)
'''
def attack_basket(data):
	drives = []
	drive_cutoff = 46
	num_play = len(data[0])
	for i in range (0, num_play):
		if (data[241][i] == -1):
			drives.append(-1)
		else:
			temp = ((.35 * data[209][i]/2) + (.075 * data[211][i]*(data[212][i] - drive_cutoff)) + \
					(1.25 * data[220][i]) - (data[222][i] + data[224][i]))/((math.sqrt(float(data[6][i])))/10)
			drives.append(temp)
	
	return drives


'''
Passing Metric:
Formula is ((Pot_Ast * .15) + (Ast * .6) + 
			(3 * Sec_Ast) + (.2 * Ast_Adj))/ ((Minutes ^ 2) / 10 )
'''
def passing(data):
	passing = []
	num_play = len(data[0])
	for i in range (0, num_play):
		if (data[241][i] == -1):
			passing.append(-1)
		else:
			temp = ((.15*data[230][i]) + (.6*data[228][i]) + \
				    (3*data[229][i]) + (.2 * float(data[231][i]))) / \
					((math.sqrt(float(data[6][i])))/10)
			passing.append(temp)
	return passing


	
'''
Movement Metric:
Formula is ((1.2 * AVG SPEED OFF) + AVG SPEED DEF) *
  		   ((1.2 * DIST MILES OFF) + DIST MILES DEF)
'''
def movement(data):
	movement = []
	num_play = len(data[0])
	for i in range (0, num_play):
		if (data[241][i] == -1):
			movement.append(-1)
		else:
			temp = (((1.2*data[239][i]) + data[240][i]) * \
				   ((1.2*data[236][i]) + data[237][i]))
			movement.append(temp)

	return movement

'''
This function sets the cutoff of minutes played.  If
a player has not played more than the minimum amount
of minutes, his statistics will be discarded
'''
def min_minutes(data):
	eligible = []
	min_minutes = 100
	for i in range (len(data[0])):
		temp = float(data[3][i]) * float(data[6][i])
		if temp > min_minutes:
			eligible.append(1)
		else:
			eligible.append(-1)

	return eligible


'''
This function is to test metrics
'''
def test_metric(players, metric):

	test_dict = dict(zip(players, metric))
	#print(test_dict)
	reverse = [(k, test_dict[k]) for k in sorted(test_dict, key=test_dict.get, reverse=True)]
	for i in range (0, 35):
		print(reverse[i])
#	print(reverse[:35])






