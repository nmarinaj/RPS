
from random import choice
computer_score = 0
human_score = 0

print "Hi, I'm Doug the computer.  Let's play 3 games of Rock-Paper-Scissors!"


def rock_paper_scissors(s, computer_score, human_score):
	

	
	x = choice("rps")
		

	if input1 == "r" and x == "r":		
		print "I play Rock."
		print "It's a tie!"
		return computer_score, human_score	
	elif input1 == "r" and x == "p":
		print "I play Paper."
		print "I win!"
		return computer_score + 1, human_score
	elif input1 == "r" and x == "s":
		print "I play Scissors."
		print "You win!"
		return computer_score, human_score + 1
	elif input1 == "p" and x == "r":
		print "I play Rock"
		print "You win!"
		return computer_score, human_score + 1
	elif input1 == "p" and x == "p":
		print "I play Paper."
		print "It's a tie!"
		return computer_score, human_score
	elif input1 == "p" and x == "s":
		print "I play Scissors."
		print "I win!"
		return computer_score + 1, human_score
	elif input1 == "s" and x == "r":
		print "I play Rock."
		print "I win!"
		return computer_score + 1, human_score
	elif input1 == "s" and x == "p":
		print "I play Paper"		
		print "You win!"
		return computer_score, human_score + 1
	elif input1 == "s" and x == "s":
		print "I play Scissors."
		print "It's a tie!"
		return computer_score, human_score

		
input1 = raw_input("Make your move. (r, p, s) or q to quit: ")
while input1 != "q":
	computer_score, human_score = rock_paper_scissors(input1, computer_score, human_score)
	print computer_score, human_score
	input1 = raw_input("Make your move. (r, p, s) or q to quit: ")
print "Final Score is Computer: %d, You: %d" % (computer_score, human_score)

print "Good game!"





