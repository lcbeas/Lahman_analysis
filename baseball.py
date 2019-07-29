import matplotlib as plt
import pandas as pd
import csv
import statistics

data = pd.read_csv('data/Lahman_batting_2000_2018.csv')
print("Shape: ", data.shape)
print("\nColumns: ", data.columns)

data['AVG'] = data['H']/data['AB']
data['OBP'] = (data['H'] + data['BB'] + data['IBB'] + data['HBP'])/ (data['AB'] + data['BB'] + data['HBP'] + data['IBB'] + data['SF'])
data['SLG'] = ((data['H'])+ (data['2B']) + (data['3B']*2) + (data['HR']*3)) / data['AB']
data['OPS'] = data['OBP'] + data['SLG']

yearly_OPS = {}
change_OPS = {}
leaderboard_OPS ={}
final_board ={'Name' : [] , 'AVG Improvement' : []}

for index, row in data[data.AB > 300].iterrows():
	if row['playerID'] in yearly_OPS:
		yearly_OPS[row['playerID']].append(row['OPS'])
		try:
			change = row['OPS']/yearly_OPS[row['playerID']][-2]
		except:
			change = 0
		change_OPS[row['playerID']].append(change)
	else:
		yearly_OPS[row['playerID']] = [row['OPS']]
		change_OPS[row['playerID']] = []

print(data.head())
x =0
y=0
for name, ops in yearly_OPS.items():
	print(f"\n{name} OPS was:")
	for each in ops:
		print(f"\t{each}")
	x = x +1
	if x>20:
		break
m=0
player = ''
for name, change in change_OPS.items():
	total = 0
	for each in change:
		total = total + each
	try:
		average = total/len(change_OPS[name])
	except:
		average = 0
	if (average > m):
		m = average
		player = name
	if (average != 0) and (len(change_OPS[name])>7):
		leaderboard_OPS[name] = average
		print(f"\t{name} OPS average improvement was {average}")

peopleData = pd.read_csv('data\Lahman_2018\People.csv')
df2 = pd.DataFrame(peopleData)

def getName(pID):
	"""return player name"""
	row = df2.loc[df2['playerID']==pID]
	first = row.iloc[0, 13]
	last = row.iloc[0, 14]
	return f"{first} {last}"

z=1

for k,v in sorted(leaderboard_OPS.items(), key=lambda x: x[1], reverse = True):
	name = getName(k)
	imp = round((v-1)*100,5)
	print(f"{z}: {name} with an average improvement of {imp}%")
	final_board['Name'].append(name)
	final_board['AVG Improvement'].append(imp)
	z= z+1
	if z>50:
		break

newDF = pd.DataFrame(final_board, columns = ['Name', 'AVG Improvement'])
newDF.to_csv(r'C:\Users\Luke\Desktop\python_work\improvement.csv')