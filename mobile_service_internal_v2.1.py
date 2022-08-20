#Ayah Kayed
#Version 1.1 - Calculate Job Cost

from tkinter import *
from functools import partial
import re

#function to calculte the job's charge
def calc_charge():
    distance_travelled = float(input("What is your distance travelled? "))
    #rounds the distance travelled to the nearest km
    distance_travelled = round(distance_travelled)
    
    minutes_spent = float(input("How many minutes were spent? "))
    
    wof_requirement = input("Was a WOF and tune required? yes/no ")

    #calculate individual costs and add them together to get total cost
    if distance_travelled < 5:
        travel_cost = 10
    else:
        travel_cost = 10 + (distance_travelled - 5) * 0.5
        
    virus_protection_cost = minutes_spent * 0.8

    #calculates wof cost
    if wof_requirement == "yes":
        wof_cost = 100
    else:
        wof_cost = 0

    total_job_cost = travel_cost + virus_protection_cost + wof_cost

    #temporary print to check if function is working properly
    print(f"The travel cost is {travel_cost}")
    print(f"The virus protection cost is {virus_protection_cost}")
    print(f"The WOF and tune cost is {wof_cost}")
    print(f"The total job cost is {total_job_cost}")

    

#main routine
calc_charge()
