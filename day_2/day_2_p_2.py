#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   return_input = []
   f = open("puzzle_input.txt", "r")

   for line in f:
      puzzle_input.append(line)

   f.close()

   puzzle_input = puzzle_input[0].split(",")
   for i in range(0, len(puzzle_input)):
       puzzle_input[i] = puzzle_input[i].replace("\n","")
       return_input.append(int(puzzle_input[i]))


   print (str(len(return_input)))

   return return_input 

def executeIntCode(puzzle_input, noun, verb):
    puzzle_input[1] = noun 
    puzzle_input[2] = verb  
    #print("Noun: " + str(noun) + ", Verb:" + str(verb))

    i = 0
    while i < len(puzzle_input):
        opCode = puzzle_input[i]
        if opCode == 99:
            break
        if opCode == 1:
            positionInput1 = puzzle_input[i+1]
            positionInput2 = puzzle_input[i+2]
            overwriteValueAtPos = puzzle_input[i+3]
            #print("Position input 1: " + str(positionInput1) + ", Position input 2: " + str(positionInput2) + " Overwrite position: " + str(overwriteValueAtPos))
            if overwriteValueAtPos < len(puzzle_input):
                puzzle_input[overwriteValueAtPos] = puzzle_input[positionInput1] + puzzle_input[positionInput2]
        if opCode == 2:    
            positionInput1 = puzzle_input[i+1]
            positionInput2 = puzzle_input[i+2]
            overwriteValueAtPos = puzzle_input[i+3]
            #print("Position input 1: " + str(positionInput1) + ", Position input 2: " + str(positionInput2) + " Overwrite position: " + str(overwriteValueAtPos))
            if overwriteValueAtPos < len(puzzle_input):
                puzzle_input[overwriteValueAtPos] = puzzle_input[positionInput1] * puzzle_input[positionInput2]

        i += 4    
            

    return puzzle_input[0]

def main():
   puzzle_input = populate()

   for noun in range(0,100):
       for verb in range(0,100):
           copyIntCode = puzzle_input.copy()
           valuePosZero = executeIntCode(copyIntCode, noun, verb)
           if valuePosZero == 19690720:
               print("Noun: " + str(noun) + ", Verb: " + str(verb))
               print("Value: " + str(100*noun+verb))
               break


if __name__ == "__main__":
   main()
