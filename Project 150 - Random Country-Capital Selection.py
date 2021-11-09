# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 12:51:13 2021

@author: taru_
"""

#basic tkinter template 
from tkinter import *
import random
root=Tk()
root.title("Random County-Captial Selection - Project 150")
root.geometry("400x400")
root.configure(bg="cyan4")

enter_country = Entry(root)
enter_capital = Entry(root)
enter_country.insert(0, "Enter country.")
enter_capital.insert(0, "Enter capital.")
enter_country.configure(state=DISABLED)
enter_capital.configure(state=DISABLED)
#to def onclick event for placeholder ----
def on_click(event):
    enter_country.configure(state=NORMAL)
    enter_capital.configure(state=NORMAL)
    enter_country.delete(0, END)
    enter_capital.delete(0, END)
    
    enter_country.unbind("<Button-1>", on_click_id)
    enter_capital.unbind("<Button-1>", on_click_id)
    #end onclick here

#to bind button onclick
on_click_id = enter_country.bind("<Button-1>", on_click)
on_click_id = enter_capital.bind("<Button-1>", on_click)
#start placing entry here
enter_country.place(relx=0.5, rely=0.15, anchor=CENTER)
enter_capital.place(relx=0.5, rely=0.2, anchor=CENTER)
#-----------------------------------------------------------------------------
countrylist = Label(root)
capitallist = Label(root)
randomcountry = Label(root)
randomcity = Label(root)
#------------------------------
listcountry = []
listcity = []
#-------------------------------------
def appendfunc():
    countryname = enter_country.get()
    listcountry.append(countryname)
    countrylist["text"]=str(listcountry)
    #get capital name ----
    capitalname = enter_capital.get()
    listcity.append(capitalname)
    capitallist["text"]=str(listcity)
#appendfunc() ends here
def generate_randnum():
    len1 = len(listcountry)
    rand_num = random.randint(0, len1-1)
    country_index = listcountry[rand_num]
    randomcountry["text"]="Random country: " + str(country_index)
    #----------------------------
    len2 = len(listcity)
    rand_num2 = random.randint(0, len2-1)
    city_index = listcity[rand_num2]
    randomcity["text"]="Random city: " + str(city_index)
#-------------------------------- func end ---------------------------------
appendButton = Button(root, text = "Add country and city to list", command=appendfunc)
appendButton.place(relx=0.5, rely=0.3, anchor=CENTER)
countrylist.place(relx=0.5, rely=0.4, anchor=CENTER)
capitallist.place(relx=0.5, rely=0.5, anchor=CENTER)
gen_button = Button(root, text = "Generate 1 country and 1 city.", command=generate_randnum)
gen_button.place(relx=0.5, rely=0.6, anchor=CENTER)
#=======================================================================
randomcountry.place(relx=0.5, rely=0.7, anchor=CENTER)
randomcity.place(relx=0.5, rely=0.8, anchor=CENTER)
#end basic template
root.mainloop()