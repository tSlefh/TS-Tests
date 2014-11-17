#! /bin/bash/python2

letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
question = ["Which Answer is <20?",["17","8","20","25"],2] #filler until csv - question, answer list, how many answers, (correct(s) are first x)


def testQ(q):
	print q[0]
	possanswers = q[1]
	numanswers = q[2]
	i = 1
	j = 0
	answers = []
	for x in possanswers:
		print "{}: {} ".format(letterlist[j],q[1][j])
		j += 1
	while i <= numanswers:
		a = raw_input("Select answer {} of {}:".format(i,numanswers))
		anum = letterlist.index(a)
		answers.append(possanswers[anum])
		i += 1
	return answers
	
def  checkA(q,a):
	correct = q[2]
	correctans = q[1][:correct]
	print correctans
	print a
	if a.sort() == correctans.sort():
		print "Right!"
	else:
		print "Wrong!"

	
		
print letterlist[1]
print question[1][0]
checkA(question,testQ(question))
		
#import questions from csv (https://docs.python.org/2/library/csv.html ) one q per row?, multiple answer possibilities, etc.