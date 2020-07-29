import random
import shelve
import statistics
from collections import defaultdict

#Define what happens when a war is started
def war(warCount):


	#Check if p1 won the war
	if p1Hand[warCount*4] > p2Hand[warCount*4]:
		p1Win.extend(p1Hand[:(warCount*4)+1])
		p1Win.extend(p2Hand[:(warCount*4)+1])
		p1Stats['Wars Won'][-1] += 1
		p1WarWinLength.append(warCount)


	#Check if p2 won the war
	elif p1Hand[warCount*4] < p2Hand[warCount*4]:
		p2Win.extend(p1Hand[:warCount*4+1])
		p2Win.extend(p2Hand[:warCount*4+1])
		p2Stats['Wars Won'][-1] += 1
		p2WarWinLength.append(warCount)


	#If neither p1 or p2 won the war then it's another war
	else:

		if len(p1Hand + p1Win) < (warCount+1)*4+1:
			p2Win.extend(p1Hand + p1Win)
			p1Hand.clear()
			p1Win.clear()
		elif len(p2Hand + p2Win) < (warCount+1)*4+1:
			p1Win.extend(p2Hand + p2Win)
			p2Hand.clear()
			p2Win.clear()


		warCount += 1
		war(warCount)
		return


	#Delete the cards won in the war from the players hands
	del p1Hand[:warCount*4+1]
	del p2Hand[:warCount*4+1]

def main():
	
	while True:
		try:
			iterations = int(input('How many Games would you like to play?\n'))
		except ValueError:
			print("That's not a number")
		else:
			break

	# Using a list of players makes more sense than creating new variables
	player_stats = [
		defaultdict(list), # Player 1
		defaultdict(list), # Player 2
		# ...
	]
	game_stats = defaultdict(list)
	
	# The above parts replace the code below, though since I didn't convert everything myself the above code doesn't do anything yet
	p1Stats = {'Total Cards': [], 'Cards in Hand': [], 'Cards in Winnings': [], 'Percentage of Deck': [], 'Weighted Percentage of Deck': [], 'Aces Dealt': [], 'Wins': 0, 'Rounds Won': [], 'Wars Won': [], 'Longest War Won': []}
	p2Stats = {'Total Cards': [], 'Cards in Hand': [], 'Cards in Winnings': [], 'Percentage of Deck': [], 'Weighted Percentage of Deck': [], 'Aces Dealt': [], 'Wins': 0, 'Rounds Won': [], 'Wars Won': [], 'Longest War Won': []}
	gameStats = {'Games Played': 0, 'Winner': [], 'Rounds': [], 'Wars': []}
	
	#Start the Game!
	for _ in range(iterations): # We don't need the values, so using an underscore makes that clear


		# Set up the Deck
		deck = list(range(1,14)) * 4
		random.shuffle(deck)

		# Give half of the Cards to Player 1
		p1Hand = deck[:int(len(deck)/2)] # Prefer the approach below instead, no reason to create a variable if you're just going to add it to the dict anyway
		# player_stats[0]['hand'].append(deck[:len(deck)//2]) # Why not just directly put the data in the dictionary?


		#Give the other half of the Cards to Player 2
		p2Hand = deck[int(len(deck)/2):]
		# player_stats[0]['hand'].append(deck[len(deck)//2:])


		#Give the players Winning piles
		p1Win = []
		p2Win = []
		# player_stats[0]['wins'] = [] and so on


		#Track the number of Rounds in a game
		totalRounds = 0
	

		p1WarWinLength = [0]
		p2WarWinLength = [0]


		p1Stats['Total Cards'].append([])
		p1Stats['Total Cards'][-1].append(len(p1Hand + p1Win))
		p1Stats['Cards in Hand'].append([])
		p1Stats['Cards in Hand'][-1].append(len(p1Hand))
		p1Stats['Cards in Winnings'].append([])
		p1Stats['Cards in Winnings'][-1].append(len(p1Win))
		p1Stats['Percentage of Deck'].append([])
		p1Stats['Percentage of Deck'][-1].append(len(p1Hand + p1Win)/len(deck))
		p1Stats['Weighted Percentage of Deck'].append([])
		p1Stats['Weighted Percentage of Deck'][-1].append(sum(p1Hand + p1Win)/sum(deck))
		p1Stats['Aces Dealt'].append(p1Hand.count(13))
		p1Stats['Rounds Won'].append(0)
		p1Stats['Wars Won'].append(0)

		p2Stats['Total Cards'].append([])
		p2Stats['Total Cards'][-1].append(len(p2Hand + p2Win))
		p2Stats['Cards in Hand'].append([])
		p2Stats['Cards in Hand'][-1].append(len(p2Hand))
		p2Stats['Cards in Winnings'].append([])
		p2Stats['Cards in Winnings'][-1].append(len(p2Win))
		p2Stats['Percentage of Deck'].append([])
		p2Stats['Percentage of Deck'][-1].append(len(p2Hand + p2Win)/len(deck))
		p2Stats['Weighted Percentage of Deck'].append([])
		p2Stats['Weighted Percentage of Deck'][-1].append(sum(p2Hand + p2Win)/sum(deck))
		p2Stats['Aces Dealt'].append(p2Hand.count(13))
		p2Stats['Rounds Won'].append(0)
		p2Stats['Wars Won'].append(0)

		#As long as both players have cards, the game continues
		while len(p1Hand + p1Win) > 0 and len(p2Hand + p2Win) > 0:


			#Make sure there is enough cards for a round
			try:

		
				#Check if p1 won the round
				if p1Hand[0] > p2Hand[0]:
					p1Win.append(p1Hand.pop(0))
					p1Win.append(p2Hand.pop(0))
					p1Stats['Rounds Won'][-1] += 1


				#Check if p2 won the round
				elif p1Hand[0] < p2Hand[0]:
					p2Win.append(p1Hand.pop(0))
					p2Win.append(p2Hand.pop(0))
					p2Stats['Rounds Won'][-1] += 1

	
				#If both cards are the same, then a war starts
				else:

					#If one of the players doesn't have enough cards to finish the war, they lose the game
					if len(p1Hand + p1Win) < 5:
						p2Win.extend(p1Hand[:5])
						p1Hand.clear()

					elif len(p2Hand + p2Win) < 5:
						p1Win.extend(p2Hand[:5])
						p2Hand.clear()


					war(1)
	
		
			
			#If one of the player's hands runs out of cards, reshuffle their winnings into their hand	
			except IndexError:
				if len(p1Hand) < len(p2Hand):
					p1Hand.extend(random.sample(p1Win,len(p1Win)))
					p1Win.clear()
				elif len(p2Hand) < len(p1Hand):
					p2Hand.extend(random.sample(p2Win,len(p2Win)))
					p2Win.clear()
				else:
					p1Hand.extend(random.sample(p1Win,len(p1Win)))
					p2Hand.extend(random.sample(p2Win,len(p2Win)))
					p1Win.clear()
					p2Win.clear()
	
				continue
	

			p1Stats['Total Cards'][-1].append(len(p1Hand + p1Win))
			p1Stats['Cards in Hand'][-1].append(len(p1Hand))
			p1Stats['Cards in Winnings'][-1].append(len(p1Win))
			p1Stats['Percentage of Deck'][-1].append(len(p1Hand + p1Win)/len(deck))
			p1Stats['Weighted Percentage of Deck'][-1].append(sum(p1Hand + p1Win)/sum(deck))

			p2Stats['Total Cards'][-1].append(len(p2Hand + p2Win))
			p2Stats['Cards in Hand'][-1].append(len(p2Hand))
			p2Stats['Cards in Winnings'][-1].append(len(p2Win))
			p2Stats['Percentage of Deck'][-1].append(len(p2Hand + p2Win)/len(deck))
			p2Stats['Weighted Percentage of Deck'][-1].append(sum(p2Hand + p2Win)/sum(deck))

			totalRounds += 1


		if len(p1Hand + p1Win) == 0: 
			p2Stats['Wins'] += 1
			gameStats['Winner'].append(2)
		

		elif len(p2Hand + p2Win) == 0:
			p1Stats['Wins'] += 1
			gameStats['Winner'].append(1)


		p1Stats['Longest War Won'].append(max(p1WarWinLength))
		p2Stats['Longest War Won'].append(max(p2WarWinLength))
		gameStats['Rounds'].append(totalRounds)
		gameStats['Wars'].append(p1Stats['Wars Won'][-1] + p2Stats['Wars Won'][-1])
		gameStats['Games Played'] += 1
		print('Done')


	with shelve.open('War Stats') as WarStats:
		WarStats['p1Stats'] = p1Stats
		WarStats['p2Stats'] = p2Stats
		WarStats['gameStats'] = gameStats

if __name__ == '__main__':
	main()
