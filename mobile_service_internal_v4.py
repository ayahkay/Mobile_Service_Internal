#Ayah Kayed
#Version 4 - Trialling WOF and Tune as checkbox

from tkinter import *
from functools import partial
import re

class Homepage:
    def __init__(self,parent):

        #formatting variables
        background_color = "light gray"

        #creates list to hold total job information
        self.total_jobs_list = []

        #main framework
        self.homepage_frame = Frame(width = 1000,
                                    bg = background_color,
                                    pady=10)
        self.homepage_frame.grid()

        #logo + heading
        #put logo + heading here

        #explanation of program
        self.program_explain_label = Label(self.homepage_frame,
                                             text = "INSERT INSTRUCTIONS HERE INSERT INSTRUCTIONS HERE INSERT INSTRUCTIONS HERE ",
                                                     font="Arial 10 italic",
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
                                      justify=LEFT,
                                      bg = background_color,
                                      padx=10)
        self.virus_protection_minutes_label.grid(row = 3, column = 0)

        self.virus_protection_minutes_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white",)
        self.virus_protection_minutes_entry.grid(row = 3, column = 1)

        self.checkbox_read = IntVar()
        self.wof_tune_checkbox = Checkbutton(self.label_entries_frame,
                                             text='WOF and tune required',
                                             font = "Arial 10 italic",
                                             justify=LEFT, bg = background_color,
                                             padx=10, variable=self.checkbox_read)
        self.wof_tune_checkbox.grid(row = 4, column = 0)

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
        
        job_number = self.job_number_entry.get()
        customer_name = self.customer_name_entry.get()
        distance_travelled = self.distance_travelled_entry.get()
        minutes_spent = self.virus_protection_minutes_entry.get()
        wof_requirement = self.checkbox_read.get()

        #checks for invalid inputs
        try:
            #calculates individual costs and add them together to get total cost
            distance_travelled = float(self.distance_travelled_entry.get())
            distance_travelled = round(distance_travelled)
            minutes_spent = float(self.virus_protection_minutes_entry.get())
            
            if distance_travelled < 5:
                travel_cost = 10
            else:
                travel_cost = 10 + (distance_travelled - 5) * 0.5
                
            virus_protection_cost = minutes_spent * 0.8
            total_job_cost = travel_cost + virus_protection_cost

            #adds $100 onto total cost if a wof and tune was required
            if wof_requirement == 1:
                total_job_cost+=100

            #saves relevant information and informs the user of their latest input
            job_information = f"This was job number {job_number}, for customer {customer_name}.\nYou charged ${total_job_cost:.2f} for this job"
            self.total_jobs_list.append(job_information)
            self.program_explain_label.configure(text=job_information)
            print(self.total_jobs_list)

        #returns an error message if an invalid input was entered
        except ValueError:
            self.program_explain_label.configure(text="Please ensure you have entered valid integers!")

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = Homepage(root)
    root.mainloop()
