# deflfe.py
from random import choice
#print 'hello world'

#def nck(*args)
#    name = args
#    if name=

strAck = ('Not you~,input again!', 'Error,do it again','Time is money,friend','Try again,never give up!')
strMatch = ('Joise','luoqiong','JoiseJJ','joise','jj','JJ')
strkw=('Love you forever!','Right,It\'s you', 'Happy everyday, baby!', 'yeah,right answer') 
'''
def lfe():
	name = raw_input('Input your name:')
	if name=='Joise':
		print 'love you'
	else: print ''
'''
#class tid:
def name_match(name):
	for n in strMatch:
		if n==name:
			return 1
	return 0

def lfe():
	while 1:
		name = raw_input('Input your name:')
		if name_match(name):
			print choice(strkw)
		else:
			print choice(strAck)
    
if '__main__' == __name__:
	lfe()   
