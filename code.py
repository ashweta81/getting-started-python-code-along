# --------------
import yaml

# Read the data of the format .yaml type
with open(path) as f:
    data=yaml.load(f)
# Find data type of the file
print('Type of file is',(type(data)))

# In which city, and at which venue the match was played and where was it played ?
print(data.keys())
print(data['info'])
city = (data['info']['city'])
venue = (data['info']['venue'])
print('The match was played at ',city,venue)
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams=data['info']['teams']
print('The teams were',teams)
# Which team won the toss and what was the decision of toss winner ?
teamtosswin=data['info']['toss']['winner']
teamtossdec=data['info']['toss']['decision']
print('The team that won the toss and their decision is', teamtosswin, teamtossdec)
# Find the first bowler and first batsman who played the first ball of the first inning
print("_"*40)
print('The first batsman is',data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman'])
print('The first bowler is',data['innings'][0]['1st innings']['deliveries'][0][0.1]['bowler'])
# How many deliveries were delivered in first inning ?
print("_"*40)
print('The total deliveries in the first innings are ', len(data['innings'][0]['1st innings']['deliveries']))

# How many deliveries were delivered in second inning ?
print("_"*40)
print('The total deliveries in the second innings are ',len(data['innings'][1]['2nd innings']['deliveries']))
# Which team won and how ?
print('The team that won is',data['info']['outcome']['winner'],'and they won by',data['info']['outcome']['by']['runs'],'runs')





