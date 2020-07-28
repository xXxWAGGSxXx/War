import random, time


print('WAR!')


#Define what happens when a war is started
def war(warCount):
	for i in range(3):

		print(str(len(p1Hand)).center(5,'|'),' '.center(3,'|'),' '*3,' '.center(3,'|'),str(len(p2Hand)).center(5,'|'))
		print(str(len(p1Win)).center(5,'|'),' '*11,str(len(p2Win)).center(5,'|'))
		time.sleep(1)
	

	print(str(len(p1Hand)).center(5,'|'),str(p1Hand[warCount*4]).center(3,'|'),' '*3,str(p2Hand[warCount*4]).center(3,'|'),str(len(p2Hand)).center(5,'|'))
	print(str(len(p1Win)).center(5,'|'),' '*11,str(len(p2Win)).center(5,'|'))
	time.sleep(2)


	#Check if p1 won the war
	if p1Hand[warCount*4] > p2Hand[warCount*4]:
		p1Win.extend(p1Hand[:(warCount*4)+1])
		p1Win.extend(p2Hand[:(warCount*4)+1])
		print('Player 1 Won the War!')


	#Check if p2 won the war
	elif p1Hand[warCount*4] < p2Hand[warCount*4]:
		p2Win.extend(p1Hand[:warCount*4+1])
		p2Win.extend(p2Hand[:warCount*4+1])
		print('Player 2 Won the War!')


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


		print("It's another War!")
		warCount += 1
		war(warCount)
		return


	#Delete the cards won in the war from the players hands
	del p1Hand[:warCount*4+1]
	del p2Hand[:warCount*4+1]
	print('War Streak: ' + str(warCount))


# Set up the Deck
deck = list(range(1,14))*4
random.shuffle(deck)


# Give half of the Cards to Player 1
p1Hand = deck[:int(len(deck)/2)]


#Give the other half of the Cards to Player 2
p2Hand = deck[int(len(deck)/2):]


#Give the players Winning piles
p1Win = []
p2Win = []


#Track the number of Rounds in a game
totalRounds = 0

print(str(len(p1Hand)).center(5,'|'),str(p1Hand[0]).center(3,'|'),' '*3,str(p2Hand[0]).center(3,'|'),str(len(p2Hand)).center(5,'|'))
print(str(len(p1Win)).center(5,'|'),' '*11,str(len(p2Win)).center(5,'|'))
time.sleep(1)

#As long as both players have cards, the game continues
while len(p1Hand + p1Win) > 0 and len(p2Hand + p2Win) > 0:


	#Make sure there is enough cards for a round
	try:

		
		#Check if p1 won the round
		if p1Hand[0] > p2Hand[0]:
			p1Win.append(p1Hand.pop(0))
			p1Win.append(p2Hand.pop(0))
			print('Player 1 Won the Round!')


		#Check if p2 won the round
		elif p1Hand[0] < p2Hand[0]:
			p2Win.append(p1Hand.pop(0))
			p2Win.append(p2Hand.pop(0))
			print('Player 2 Won the Round!')

	
		#If both cards are the same, then a war starts
		else:

			#If one of the players doesn't have enough cards to finish the war, they lose the game
			if len(p1Hand + p1Win) < 5:
				p2Win.extend(p1Hand[:5])
				p1Hand.clear()

			elif len(p2Hand + p2Win) < 5:
				p1Win.extend(p2Hand[:5])
				p2Hand.clear()


			print("It's a War!")
			war(1)

		time.sleep(1)
		print(str(len(p1Hand)).center(5,'|'),str(p1Hand[0]).center(3,'|'),' '*3,str(p2Hand[0]).center(3,'|'),str(len(p2Hand)).center(5,'|'))
		print(str(len(p1Win)).center(5,'|'),' '*11,str(len(p2Win)).center(5,'|'))
		time.sleep(2)
		
			
	#If one of the player's hands runs out of cards, reshuffle their winnings into their hand	
	except IndexError:
		print('Shuffling...')
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

	totalRounds += 1


print('Game Over: ',end = '')

if len(p1Hand + p1Win) == 0:
	print('P2 Wins')

elif len(p2Hand + p2Win) == 0:
	print('P1 Wins')

print('That game lasted ' + str(totalRounds) + ' rounds!')
