#Ayah Kayed
#Version 7 - Programming Next and Previous Job buttons

from tkinter import *
from functools import partial
import re
from itertools import cycle

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
                                             text = "INSERT INSTRUCTIONS HERE INSERT INSTRUCTIONS HERE INSERT INSTRUCTIONS HERE",
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
                                      text = "Distance travelled (km):",
                                      font = "Arial 10 italic",
                                      justify=LEFT,
                                      bg = background_color,
                                      padx=10)
        self.distance_travelled_label.grid(row = 2, column = 0)

        self.distance_travelled_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white",)
        self.distance_travelled_entry.grid(row = 2, column = 1)

        #enables elements based on checkbox inputs
        def configure():
            #enables minutes spent entry once checkbox selected
            if self.virus_checkbox_selected.get() == 0:
                self.virus_protection_minutes_entry.config(state="disabled")
            else:
                self.virus_protection_minutes_entry.config(state="normal")
            #enables enter job button if at least one checkbox selected 
            if (self.virus_checkbox_selected.get() == 0) & (self.wof_checkbox_selected.get() == 0):
                self.enter_job_button.config(state="disabled")
            else:
                self.enter_job_button.config(state="normal")

        #checkbox for virus protection
        self.virus_checkbox_selected = IntVar()
        self.virus_protection_checkbox = Checkbutton(self.label_entries_frame,
                                      text = "Virus protection required",
                                      font = "Arial 10 italic",
                                      justify=LEFT, bg = background_color,
                                      padx=10, variable=self.virus_checkbox_selected,
                                                     command=configure)
        self.virus_protection_checkbox.grid(row = 3, column = 0)

        self.virus_protection_minutes_entry = Entry(self.label_entries_frame, width=25,
                                      font="Arial 12",
                                      bg = "white", state="disabled")
        self.virus_protection_minutes_entry.grid(row = 3, column = 1)

        #checkbox for WOF and tune to minimise errors
        self.wof_checkbox_selected = IntVar()
        self.wof_tune_checkbox = Checkbutton(self.label_entries_frame,
                                             text='WOF and tune required',
                                             font = "Arial 10 italic",
                                             justify=LEFT, bg = background_color,
                                             padx=10, variable=self.wof_checkbox_selected,
                                             command=configure)
        self.wof_tune_checkbox.grid(row = 4, column = 0)

        #frame with buttons
        self.buttons_frame = Frame(self.homepage_frame)
        self.buttons_frame.grid(row = 4)

        self.enter_job_button = Button(self.buttons_frame,
                                       font="Arial 12 bold",
                                       text="Enter Job",width=10,
                                       command=self.calc_charge,
                                       state="disabled")
        self.enter_job_button.grid(row = 0, column = 0)

        #button to show all jobs. doesnt appear until at least one job has been entered
        self.show_jobs_button = Button(self.buttons_frame,
                                       font="Arial 12 bold",
                                       text="Show All Jobs",width=12,
                                       state="disabled",
                                       command=lambda: self.all_jobs(self.total_jobs_list))
        self.show_jobs_button.grid(row = 0, column = 1)

    #function to calculte the job's charge
    def calc_charge(self):
        
        job_number = self.job_number_entry.get()
        customer_name = self.customer_name_entry.get()
        distance_travelled = self.distance_travelled_entry.get()
        minutes_spent = self.virus_protection_minutes_entry.get()
        virus_requirement = self.virus_checkbox_selected.get()
        wof_requirement = self.wof_checkbox_selected.get()

        #assigns a numerical value in order not to create a value error
        if virus_requirement == 0:
            minutes_spent = 0

        #checks for invalid inputs
        try:
            #calculates individual costs and add them together to get total cost
            job_number = float(job_number)
            distance_travelled = float(distance_travelled)
            distance_travelled = round(distance_travelled)
            minutes_spent = float(minutes_spent)
            
            if distance_travelled < 5:
                travel_cost = 10
            else:
                travel_cost = 10 + (distance_travelled - 5) * 0.5
                
            virus_protection_cost = minutes_spent * 0.8
            total_job_cost = travel_cost + virus_protection_cost

            #adds $100 onto total cost if a wof and tune was required
            if wof_requirement == 1:
                total_job_cost+=100

            #returns an error message if blank customer name was entered
            if customer_name == "":
                self.program_explain_label.configure(text="Please enter a customer name!")
            #returns an error message if negative inputs were entered
            elif distance_travelled < 0 or minutes_spent < 0:
                self.program_explain_label.configure(text="Please ensure you have entered valid integers in all numerical fields!")
            #displays correct 
            else:
                job_information = f"This was job number {job_number:.0f}, for customer {customer_name}.\nYou charged ${total_job_cost:.2f} for this job."
                self.total_jobs_list.append(job_information)
                self.program_explain_label.configure(text=job_information)

        #returns an error message if an invalid input was entered
        except ValueError:
            self.program_explain_label.configure(text="Please ensure you have entered valid integers in all numerical fields!")

        if len(self.total_jobs_list) >= 1:
            self.show_jobs_button.config(state="normal")


    def all_jobs(self, total_jobs_list):
        AllJobs(self, total_jobs_list)

#new class for new window that will display all jobs
class AllJobs:
    def __init__(self, partner, total_jobs_list):

        partner.show_jobs_button.config(state="disabled")

        #formatting variables
        background_color = "light blue"
        self.i = 0
        
        self.all_jobs_box=Toplevel()
        
        self.all_jobs_box.protocol('WM_DELETE_WINDOW',partial(self.close_all_jobs, partner))

        #new window's main framework
        self.all_jobs_frame = Frame(self.all_jobs_box,
                                    bg = background_color)
        self.all_jobs_frame.grid()

        #logo + heading
        #put logo + heading here

        #explanation of new window
        self.window_explain_label = Label(self.all_jobs_frame,
                                             text = "INSERT INSTRUCTIONS HERE INSERT INSTRUCTIONS HERE INSERT INSTRUCTIONS HERE",
                                                     justify=LEFT, bg=background_color,
                                                     padx=10, pady=10)
        self.window_explain_label.grid(row=1)

        #display of job history
        self.display_history_label = Label(self.all_jobs_frame,
                                           text = total_jobs_list[self.i] + "\n",
                                           bg = background_color,
                                           justify=LEFT)
        self.display_history_label.grid(row=3)

        #next/previous buttons
        self.next_previous_frame = Frame(self.all_jobs_frame)
        self.next_previous_frame.grid(row = 5)

        self.next_button = Button(self.next_previous_frame,
                                       font="Arial 12 bold",
                                       text="Next Job",width=10,
                                  command = lambda: self.next_job(total_jobs_list),
                                  state="normal")
        self.next_button.grid(row = 0, column = 1)

        if len(total_jobs_list) == 1:
            self.next_button.config(state="disabled")
        
        self.previous_button = Button(self.next_previous_frame,
                                       font="Arial 12 bold",
                                       text="Previous Job",width=12,
                                      command = lambda: self.previous_job(total_jobs_list),
                                      state="disabled")
        self.previous_button.grid(row = 0, column = 0)

    def previous_job(self, total_jobs_list):
        self.i -= 1
        self.display_history_label.config(text = total_jobs_list[self.i])
        self.check_button(total_jobs_list)

    def next_job(self, total_jobs_list):
        self.i += 1
        self.display_history_label.config(text = total_jobs_list[self.i])
        self.check_button(total_jobs_list)

    def check_button(self, total_jobs_list):
        if self.i < len(total_jobs_list) - 1:
            self.next_button.config(state="normal")
        if self.i == len(total_jobs_list) - 1:
            self.next_button.config(state="disabled")
        if self.i > 0:
            self.previous_button.config(state="normal")
        if self.i == 0:
            self.previous_button.config(state="disabled")
        
    def close_all_jobs(self, partner):
        partner.show_jobs_button.config(state="normal")
        self.all_jobs_box.destroy()

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = Homepage(root)
    root.mainloop()
