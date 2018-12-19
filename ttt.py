#Husain Shaikh
#1-11-18
#Tic tac toe game
#Wants to add ML for computer

import time
from random import randint

def board(poslist):
	#first row
	print("     ",end='')
	print("|",end='')
	print("     ",end='')
	print("|",end='')
	print("     ")
	#second row
	print("  {}  ".format(poslist[0]),end='')
	print("|",end='')
	print("  {}  ".format(poslist[1]),end='')
	print("|",end='')
	print("  {}  ".format(poslist[2]))
	#third row
	print("_____",end='')
	print("|",end='')
	print("_____",end='')
	print("|",end='')
	print("_____")
	#first row
	print("     ",end='')
	print("|",end='')
	print("     ",end='')
	print("|",end='')
	print("     ")
	#second row
	print("  {}  ".format(poslist[3]),end='')
	print("|",end='')
	print("  {}  ".format(poslist[4]),end='')
	print("|",end='')
	print("  {}  ".format(poslist[5]))
	#third row
	print("_____",end='')
	print("|",end='')
	print("_____",end='')
	print("|",end='')
	print("_____")
	#first row
	print("     ",end='')
	print("|",end='')
	print("     ",end='')
	print("|",end='')
	print("     ")
	#second row
	print("  {}  ".format(poslist[6]),end='')
	print("|",end='')
	print("  {}  ".format(poslist[7]),end='')
	print("|",end='')
	print("  {}  ".format(poslist[8]))
	#third row
	print("     ",end='')
	print("|",end='')
	print("     ",end='')
	print("|",end='')
	print("     ")

poslist=["-","-","-","-","-","-","-","-","-"]
while(True):
	
	posuser=int(input("Enter the pos(1-9) you want to cross: "))
	while(poslist[posuser-1]=="X" or poslist[posuser-1]=="O"):
		posuser=int(input("------Please Enter it again : "))
	poslist[posuser-1]="X"
	board(poslist)
	time.sleep(1)
	if((poslist[0]=="X" and poslist[1]=="X" and poslist[2]=="X") or (poslist[3]=="X" and poslist[4]=="X" and poslist[5]=="X") or (poslist[6]=="X" and poslist[7]=="X" and poslist[8]=="X")):
		print("Congrats you won!!!")
		break
	if((poslist[0]=="X" and poslist[3]=="X" and poslist[6]=="X") or (poslist[1]=="X" and poslist[4]=="X" and poslist[7]=="X") or (poslist[2]=="X" and poslist[5]=="X" and poslist[8]=="X")):
		print("Congrats you won!!!")
		break
	if((poslist[0]=="X" and poslist[4]=="X" and poslist[8]=="X") or (poslist[2]=="X" and poslist[4]=="X" and poslist[6]=="X")):
		print("Congrats you won!!!")
		break
	print("------------------------------------------------")
	poscomp=randint(0,8)
	while(poslist[poscomp]=="X"):
		poscomp=randint(0,8)
	print("Computer : ",poscomp+1)
	poslist[poscomp]="O"
	board(poslist)

	if((poslist[0]=="O" and poslist[1]=="O" and poslist[2]=="O") or (poslist[3]=="O" and poslist[4]=="O" and poslist[5]=="O") or (poslist[6]=="O" and poslist[7]=="O" and poslist[8]=="O")):
		print("Computer won!!!")
		break
	if((poslist[0]=="O" and poslist[3]=="O" and poslist[6]=="O") or (poslist[1]=="O" and poslist[4]=="O" and poslist[7]=="O") or (poslist[2]=="O" and poslist[5]=="O" and poslist[8]=="O")):
		print("Computer won!!!")
		break
	if((poslist[0]=="O" and poslist[4]=="O" and poslist[8]=="O") or (poslist[2]=="O" and poslist[4]=="O" and poslist[6]=="O")):
		print("Computer won!!!")
		break
	
