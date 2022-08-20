#Ayah Kayed
#Version 7.1 - Programming Next/Previous Job Buttons

from tkinter import *
from functools import partial
import re
from itertools import cycle

#new class for new window that will display all jobs
class AllJobs:
    def __init__(self,parent):

        #initialising temporary list for testing purposes
        self.total_jobs_list=["Job One","Job Two","Job Three","Job Four"]

        #formatting variables
        background_color = "light blue"
        self.i = 0
        
        #new window's main framework
        self.all_jobs_frame = Frame(bg = background_color)
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
                                           text = self.total_jobs_list[self.i] + "\n",
                                           bg = background_color,
                                           justify=LEFT)
        self.display_history_label.grid(row=3)

        #next/previous buttons
        self.next_previous_frame = Frame(self.all_jobs_frame)
        self.next_previous_frame.grid(row = 5)

        self.next_button = Button(self.next_previous_frame,
                                       font="Arial 12 bold",
                                       text="Next Job",width=10,
                                  command = lambda: self.next_job(),
                                  state="normal")
        self.next_button.grid(row = 0, column = 1)

        if len(self.total_jobs_list) == 1:
            self.next_button.config(state="disabled")
        
        self.previous_button = Button(self.next_previous_frame,
                                       font="Arial 12 bold",
                                       text="Previous Job",width=12,
                                      command = lambda: self.previous_job(),
                                      state="disabled")
        self.previous_button.grid(row = 0, column = 0)

    def previous_job(self):
        self.i -= 1
        self.display_history_label.config(text = self.total_jobs_list[self.i])
        self.check_button(self.total_jobs_list)

    def next_job(self):
        self.i += 1
        self.display_history_label.config(text = self.total_jobs_list[self.i])
        self.check_button(self.total_jobs_list)

    def check_button(self, total_jobs_list):
        if self.i < len(self.total_jobs_list) - 1:
            self.next_button.config(state="normal")
        if self.i == len(self.total_jobs_list) - 1:
            self.next_button.config(state="disabled")
        if self.i > 0:
            self.previous_button.config(state="normal")
        if self.i == 0:
            self.previous_button.config(state="disabled")

#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Mobile Service")
    something = AllJobs(root)
    root.mainloop()
