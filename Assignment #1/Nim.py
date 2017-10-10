
import random
import math

def Nim():
    size = random.randrange(10, 101)
    print ("The size of the pile is {} marbles.".format(size))
    if random.randrange(0, 2) == 0:
        first = "computer"
        next = "human"
        print ("The computer will go first.")
    else: 
        first = "human"
        second = "computer"
        print ("The human will go first.")
    if random.randrange(0, 2) == 0:
        computer = "smart"
    else:
        computer = "stupid"
        
    while size >= 1:
        if first == "human" and computer == "stupid":
            take = input("How many marbles will you take?  ")
            take = int(take)
            while (isinstance(take, int) == False or take > math.floor(size/2) or take == 0) and take != 1:
                take = input("How many marbles will you take? Must be half or less than half and more than 0... :  ")
                take = int(take)
            size = size - take
            if size == 0:
                print ("Zero marbles left. Human loses.")
                break
            print ("The size of the pile is {} marbles.".format(size))
            comp_take = random.randrange(1, math.ceil((size/2) + 1))
            size = size - comp_take
            print ("The computer took {} marbles. \nThe size of the pile is {} marbles.".format(comp_take, size))
            if size == 0:
                print ("Zero marbles left. Computer loses.")
                break;
        elif first == "human" and computer == "smart":
            take = input("How many marbles will you take?  ")
            take = int(take)
            while isinstance(take, int) == False or take > math.floor(size/2) and take != 1:
                take = input("How many marbles will you take? Must be half or less than half... :  ")
                take = int(take)
            size = size - take
            if size == 0:
                print ("Zero marbles left. Human loses.")
                break
            print ("The size of the pile is {} marbles.".format(size))
            if size - 3 <= math.floor(size/2) and size - 3 > 0:
                comp_take = size - 3
            elif size - 7 <= math.floor(size/2) and size - 7 > 0:
                comp_take = size - 7
            elif size - 15 <= math.floor(size/2) and size - 15 > 0:
                comp_take = size - 15
            elif size - 31 <= math.floor(size/2) and size - 31 > 0:
                comp_take = size - 31
            elif size - 63 <= math.floor(size/2) and size - 63 > 0:
                comp_take = size - 63
            else: 
                comp_take = 1
            size = size - comp_take
            print ("The computer took {} marbles. \nThe size of the pile is {} marbles.".format(comp_take, size))
            if size == 0:
                print ("Zero marbles left. Computer loses.")
                break;

        elif first == "computer" and computer == "stupid":
            comp_take = random.randrange(1, math.ceil((size/2) + 1))
            size = size - comp_take
            print ("The computer took {} marbles. \nThe size of the pile is {} marbles.".format(comp_take, size))
            if size == 0:
                print ("Zero marbles left. Computer loses.")
                break;
            take = input("How many marbles will you take?  ")
            take = int(take)
            while (isinstance(take, int) == False or take > math.floor(size/2) or take == 0) and take != 1:
                take = input("How many marbles will you take? Must be half or less than half and more than 0... :  ")
                take = int(take)
            size = size - take
            if size == 0:
                print ("Zero marbles left. Human loses.")
                break
        else:
            if size - 3 <= math.floor(size/2) and size - 3 > 0:
                comp_take = size - 3
            elif size - 7 <= math.floor(size/2) and size - 7 > 0:
                comp_take = size - 7
            elif size - 15 <= math.floor(size/2) and size - 15 > 0:
                comp_take = size - 15
            elif size - 31 <= math.floor(size/2) and size - 31 > 0:
                comp_take = size - 31
            elif size - 63 <= math.floor(size/2) and size - 63 > 0:
                comp_take = size - 63
            else: 
                comp_take = 1
            size = size - comp_take
            print ("The computer took {} marbles. \nThe size of the pile is {} marbles.".format(comp_take, size))
            if size == 0:
                print ("Zero marbles left. Computer loses.")
                break;
            take = input("How many marbles will you take?  ")
            take = int(take)
            while (isinstance(take, int) == False or take > math.floor(size/2) or take == 0) and take != 1:
                take = input("How many marbles will you take? Must be half or less than half and more than 0... :  ")
                take = int(take)
            size = size - take
            if size == 0:
                print ("Zero marbles left. Human loses.")
                break



        
        

Nim()