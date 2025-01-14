'''
Program:    Southwest Pilot Flight Program 
Developer:  Sam BrownIzaak Dittrich, Viviance
Date:       April 21, 2022
Purpose:    This application allows Southwest pilots to clock-in and clock-out of their flight, along with including monthly 
            hour totals and corresponding wage based on those hours.
'''

import tkinter
from tkinter import *
import tkinter as tkr
from time import strftime
import datetime
import timeit
from tkinter import messagebox
from turtle import width


class App():
    def __init__(self):
        self.create_app()

    # create_app -> goback
    # create_login

    # if goback : -> call create_login

    def create_app(self):
        root = tkr.Tk()
        root.geometry('900x600')
        root.configure(bg='blue')
        root.title('Southwest Clock-in')

        photoLabel_frame = tkr.Frame(root)
        photoLabel_frame.pack()

        # Pass the path to the photo in your local computer here.
        photo = PhotoImage(file='/Users/izaakdittrich/Downloads/help_linhtrang/labelxx.png')
        tkr.Label(photoLabel_frame, image=photo).grid(row=1, column=1)

        def time():
            x = datetime.datetime.now().strftime(("%d/%m/%Y \n%H:%M:%S %p"))
            clock.config(text=x, bg='blue', fg='white', font='times 20 bold')
            clock.after(1000, time)

        time_frame = tkr.Frame(root, bg='blue')
        time_frame.pack()

        clock = tkr.Label(time_frame, pady=30, padx=30)
        time()
        clock.grid(row=0, column=0)

        # create a label widget
        main_frame = tkr.Frame(root, bg='blue')
        main_frame.pack()

        tkr.Label(main_frame, text="Team", bg='blue', fg='white', font='times 20 bold').grid(row=0, column=0, sticky=W)
        tkr.Label(main_frame, text="Name", bg='blue', fg='white', font='times 20 bold').grid(row=1, column=0, pady=10,
                                                                                             sticky=W)
        tkr.Label(main_frame, text="ID", bg='blue', fg='white', font='times 20 bold').grid(row=2, column=0, pady=10,
                                                                                           sticky=W)
        tkr.Label(main_frame, text="Month", bg='blue', fg='white', font='times 20 bold').grid(row=3, column=0, pady=10,
                                                                                           sticky=W)

        # team number drop list
        options = [
            "Domestic Pilot",
            "Domestic Co-Pilot",
            "Regional Pilot",
            "Regional Co-Pilot",
            "International Pilot",
            "International Co-Pilot",
             ]
        clicked = IntVar()
        clicked.set("Select your team number")
        optionMenu = tkr.OptionMenu(main_frame, clicked, *options)
        optionMenu.config(width="30")
        optionMenu.grid(row=0, column=1)

        # name droplist
        pilot = [
            "John Rosenberry",
            "Viviance Nguyen",
            "Izaak Ditrich",
            "Patrick Bauer",
            
        ]
        clicked = StringVar()
        clicked.set("Chose your name")
        pilot = tkr.OptionMenu(main_frame, clicked, *pilot)
        pilot.config(width="30")
        pilot.grid(row=1, column=1)

        # entry widgets, used to take entry from user
        month = tkr.StringVar
        month= Entry(main_frame, width=34, bg="white", textvariable=month).grid (row=3, column=1)
        monthSel = ['January','February','March','April','May','June','July','August','September','October','November','December']
        clicked = StringVar()
        clicked.set("Select your month")
        monthSel = tkr.OptionMenu(main_frame, clicked, *monthSel)
        monthSel.config(width="30")
        monthSel.grid(row=3, column=1)


        # tkr.Entry(main_frame, id_numb)

        id = tkr.StringVar()
        id_numb = Entry(main_frame, width=34, bg="white", textvariable=id)
        id_numb.grid(row=2, column=1)

        def validation():
            id = id_numb.get()
            if len(id) == 0:
                msg = 'Field can\'t be empty'
            else:
                try:
                    if len(id) == 4:
                        msg = 'Clock-In Operation Successfully'
                    else:
                        msg = 'Try Again With 4 Digit ID'
                except:
                    msg = 'Enter Numbers Only'

            messagebox.showinfo('info', msg)

        # validation()

        # button widget
        tkr.Button(main_frame, text="Go Back", fg='black', bg='blue', highlightbackground='orange',
                   font='times 18 bold').grid(row=4, column=1, pady=28, sticky=W)
        tkr.Button(main_frame, text="Clock In", command=validation, fg='black', bg='blue',
                   highlightbackground='orange', font='times 18 bold').grid(row=4, column=1, pady=28, sticky=E)
        tkr.Button(main_frame, text="Need help?", bg='blue', fg='black', highlightbackground='blue',
                   font='times 15 bold').grid(row=5, column=2, pady=40, padx=15, sticky=E)

        # This helps to remain the app opened until the user close it
        root.mainloop()

        # TODO: you should still implement what happens after users click the buttons, right?


if __name__ == '__main__':
    App()