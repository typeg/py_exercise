#!/usr/bin/python
#file: lucky.py

userNum = int(raw_input('gimme a number: '))
logicStat = '''
if userNum > 7 :
    print 'Over'
elif userNum < 7 :
    print 'Under'
else :
    print 'LUCKY'
'''
exec logicStat
