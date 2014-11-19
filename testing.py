#! /bin/bash/python2

letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#question = ["Which Answer is <20?",2,1,2,25,30] #csv format - question, number of correct answers, answers (correct first)
import sys
import getopt
import csv
import random


class Question:
	def __init__(self,q,rand):
		self.ask = q[0]
		self.anum = int(q[1])
		self.alist = []
		y = 0
		for x in q[2:]:
			if x:
				try:
					self.alist.append(x)
				except IndexError:
					print "Too many answers! 26 max!"
					sys.exit(2)
		self.corrlist = self.alist[:self.anum]
		#print self.corrlist
		if rand:
			random.shuffle(self.alist)


def testQ(q):
	print q.ask
	numanswers = q.anum
	#random.shuffle(q.alist)
	#print q.alist
	i = 1
	j = 0
	answers = []
	for x in q.alist:
		if x:
			print "{}: {} ".format(letterlist[j],q.alist[j])
			j += 1
		else:
			break
	while i <= numanswers:
		try:
			a = raw_input("Select answer {} of {}:".format(i,numanswers))
			anum = letterlist.index(a)
			ans = q.alist[anum]
			#if ans in answers:
				#print "You already said that!"
			answers.append(ans)
		except (IndexError,ValueError):
			print "Not a valid answer!"
			continue
		i += 1
	return answers
	
def  checkA(q,a,train):
	#correct = q[1]
	#correctans = q[1][:correct]   ---wtf?
	#ec = int(q.anum)+2
	#correctans = q.alist[:int(q.anum)]
	#print correctans, sorted(correctans)
	#print a, sorted(a)
	if not train:
		if sorted(a) == sorted(q.corrlist):
			#print "Right!"
			return True
		else:
			#print "Wrong!"
			return False
	else:
		if sorted(a) == sorted(q.corrlist):
			print "Right!"
			return True
		else:
			if len(q.corrlist) == 1:
				print "Sorry, the correct answer was {}.".format(q.corrlist[0])
			else:
				print "Sorry, the correct answers were:"
				for x in q.corrlist:
					print x
			return False

	
		
#print letterlist[1]
#print question[1][0]
#checkA(question,testQ(question))

def usage():
	print "This testing software accepts a csv file of questions and answers. Please enter the command as:"
	print "testing.py [-ht] [--help] [--training] [--nonrandom] filename.csv"
	print "-h, --help : Display these messages."
	print "-t, --training : Training mode: Correct answers will be shown after incorrect attempts."
	print "--nonrandom : Do not randomize answer order"
	print "\n"


def main(argv):
	totalQ = 0
	correctQ = 0
	correctList = []
	incorrectList = []
	flags = {'train':False,'rand':True}
	
	
	try:
		#print argv
		opts, args = getopt.getopt(argv,"ht",["help","training","nonrandom"])
		#print opts, args
		for opt, arg in opts:
			if opt in ("-h","--help"):
				usage()
			if opt in ("-t","--training"):
				print "Training mode enabled! Correct answers will be shown after incorrect attempts.\n"
				flags['train'] = True
			if opt in ("--nonrandom"):
				flags['rand'] = False
		if len(args) != 1:
			print "Please call a single test file."
			sys.exit(2)
	except getopt.GetoptError:
		print "Please call a single test file."
		sys.exit(2)
		
	with open(args[0], 'rb') as csvfile:
		test = csv.reader(csvfile, dialect='excel')
		#testlist = list(test)   ---   can end with here, since iterable is exhausted (check if can access variable), then can shuffle this
		for row in test:
			#print row
			q = Question(row,flags['rand'])
			totalQ += 1
			print "Question {}".format(totalQ)
			if checkA(q,testQ(q),flags['train']):
				correctQ += 1
				correctList.append(q)
			else:
				incorrectList.append(q)
		print "Number Correct: {}/{}".format(correctQ,totalQ)
			
	
if __name__ == "__main__":
	main(sys.argv[1:])
	

		
#import questions from csv (https://docs.python.org/2/library/csv.html ) one q per row?, multiple answer possibilities, etc.