#!/usr/bin/python3

from array import *

def populate():
   puzzle_input = []
   f = open("puzzle_input.txt", "r")

   for line in f:
      puzzle_input.append(int(line))

   f.close()

   #print (puzzle_input)

   return puzzle_input

def calculateFuelRequirements(puzzle_input):
    sumFuel = 0

    for i in range(0, len(puzzle_input)):
        mass = puzzle_input[i]
        fuelRequirement = (mass//3) - 2
        totalFuelRequirement = fuelRequirement
        #print("Mass: " + str(mass) + " , fuel requirement: " + str(fuelRequirement))
        while fuelRequirement > 0:
            fuelRequirement = (fuelRequirement//3) - 2
            #print("Inner fuel requirement: " + str(fuelRequirement))
            if fuelRequirement < 0:
                break
            else:
                totalFuelRequirement += fuelRequirement

        sumFuel += totalFuelRequirement 

    return sumFuel    

def main():
   puzzle_input = populate()

   sumFuel = calculateFuelRequirements(puzzle_input)

   print("Fuel required: " + str(sumFuel))

if __name__ == "__main__":
   main()
