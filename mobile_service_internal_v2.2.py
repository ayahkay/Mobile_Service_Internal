#Ayah Kayed
#Version 2 - Integrating Calculation

from tkinter import *
from functools import partial
import re

class Homepage:
    def __init__(self,parent):

        #formatting variables
        background_color = "light gray"

        #main framework
        self.homepage_frame = Frame(width = 1000,
                                    bg = background_color,
                                    pady=10)
        self.homepage_frame.grid()

        #logo + heading
        #put logo + heading here

        #explanation of program
        self.program_explain_label = Label(self.homepage_frame,
                                             text = "INSERT INSTRUCTIONS HERE "
                                                     "INSERT INSTRUCTIONS HERE "
                                                     "INSERT INSTRUCTIONS HERE ",
                                                     font="Arial 10 italic", wrap=250,
                                                     justify=LEFT, bg=background_color,
                                                     padx=10, pady=10)
        self.program_explain_label.grid(row=1)

        #frame including labels and entries
        self.label_entries_frame = Frame(self.homepage_frame,
                                         pady=10,
                                         bg=background_color)
        self.label_entries_frame.grid(row = 3)
        
        self.job_number_label = Label(self.label_entries_frame,
                                      text = "Job number:",
                                      font = "Arial 10 italic",
                                      wrap = 250,
                                      justify=LEFT,
                                      bg = background_color,
                                      padx=10)
        self.job_number_label.grid(row = 0, column = 0)

        self.job_number_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white",)
        self.job_number_entry.grid(row = 0, column = 1)
        
        self.customer_name_label = Label(self.label_entries_frame,
                                      text = "Customer name:",
                                      font = "Arial 10 italic",
                                      wrap = 250,
                                      justify=LEFT,
                                      bg = background_color,
                                      padx=10)
        self.customer_name_label.grid(row = 1, column = 0)

        self.customer_name_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white",)
        self.customer_name_entry.grid(row = 1, column = 1)

        self.distance_travelled_label = Label(self.label_entries_frame,
                                      text = "Distance travelled:",
                                      font = "Arial 10 italic",
                                      wrap = 250,
                                      justify=LEFT,
                                      bg = background_color,
                                      padx=10)
        self.distance_travelled_label.grid(row = 2, column = 0)

        self.distance_travelled_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white",)
        self.distance_travelled_entry.grid(row = 2, column = 1)

        self.virus_protection_minutes_label = Label(self.label_entries_frame,
                                      text = "Minutes spent on virus protection:",
                                      font = "Arial 10 italic",
                                      wrap = 250,
                                      justify=LEFT,
                                      bg = background_color,
                                      padx=10)
        self.virus_protection_minutes_label.grid(row = 3, column = 0)

        self.virus_protection_minutes_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white",)
        self.virus_protection_minutes_entry.grid(row = 3, column = 1)

        self.wof_tune_label = Label(self.label_entries_frame,
                                      text = "WOF and tune (yes/no):",
                                      font = "Arial 10 italic",
                                      wrap = 250,
                                      justify=LEFT,
                                      bg = background_color,
                                      padx=10)
        self.wof_tune_label.grid(row = 4, column = 0)

        self.wof_tune_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white",)
        self.wof_tune_entry.grid(row = 4, column = 1)

        #frame with buttons
        self.buttons_frame = Frame(self.homepage_frame)
        self.buttons_frame.grid(row = 4)

        self.enter_job_button = Button(self.buttons_frame,
                                       font="Arial 12 bold",
                                       text="Enter Job",width=10,
                                       command=self.calc_charge)
        self.enter_job_button.grid(row = 0, column = 0)

        self.show_jobs_button = Button(self.buttons_frame,
                                       font="Arial 12 bold",
                                       text="Show All Jobs",width=12)
        self.show_jobs_button.grid(row = 0, column = 1)

    #function to calculte the job's charge
    def calc_charge(self):
        distance_travelled = float(self.distance_travelled_entry.get())
        #rounds the distance travelled to the nearest km
        distance_travelled = round(distance_travelled)
        
        minutes_spent = float(self.virus_protection_minutes_entry.get())
        
        wof_requirement = self.wof_tune_entry.get()

        #calculate individual costs and add them together to get total cost
        if distance_travelled < 5:
            travel_cost = 10
        else:
            travel_cost = 10 + (distance_travelled - 5) * 0.5
            
        virus_protection_cost = minutes_spent * 0.8
        total_job_cost = travel_cost + virus_protection_cost

        #adds $100 onto total cost if a wof and tune was required
        if wof_requirement == "yes":
            total_job_cost+=100

        #temporary print to check if function is working properly
        print(total_job_cost)

    

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = Homepage(root)
    root.mainloop()
