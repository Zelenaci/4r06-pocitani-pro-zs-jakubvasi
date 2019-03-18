# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:44:07 2019

@author: Kuba
"""

from random import randint
import tkinter as tk

class App(): 
    def __init__(self, master):        
        self.oper_vals = []
        self.used_operators = []
        
        self.x = 1
        self.y = 1
        self.oper = ""
        self.res = 0
        
        self.formula_labels = ["", "", "", "="]
        self.formula_label_objects = []
        
        self.score = [0, 0]
        self.score_labels = ["Správně: ", self.score[0], "Špatně: ", self.score[1]]
        self.score_label_objects = []
               
        #_________________________________W I D G E T S_________________________________#
        # Operace
        oper_frame = tk.Frame(master)
        oper_frame.grid(row = 0, sticky = "W")
        
        oper_label = tk.Label(oper_frame, text = "Operace:", font = ("Arial Black",16))
        oper_label.grid(row = 0, column = 0, columnspan = 4, sticky = "W")
        
        oper_labels = ["+", "-", "*", "/"]
        oper_cbuts = []
        
        for i in range(len(oper_labels)):
            self.oper_vals.append(tk.BooleanVar())
            oper_cbuts.append(
                    tk.Checkbutton(oper_frame, text = oper_labels[i], 
                                   variable = self.oper_vals[i], height=0, width = 3,
                                   font = ("Arial Black",12),
                                   command = self.oper_update))
            oper_cbuts[i].grid(row = 1, column = i)
            
        # Priklad
        formula_frame = tk.Frame(master)
        formula_frame.grid(row = 1, sticky = "W")
        
        formula_label = tk.Label(formula_frame, text = "Příklad:", font = ("Arial Black",16))
        formula_label.grid(row = 0, column = 0, columnspan = 4, sticky = "W")
        
        for i in range(len(self.formula_labels)):
            self.formula_label_objects.append(
                    tk.Label(formula_frame, text = self.formula_labels[i], width=2, font = ("Arial Black",12)))
            self.formula_label_objects[i].grid(row = 1, column = i, sticky = "W")
            
        self.formula_user_result = tk.Text(formula_frame, height = 1, width = 10)
        self.formula_user_result.grid(row = 1, column = len(self.formula_labels) + 1)
        
        formula_confirm = tk.Button(formula_frame, text = "OK", width = 6, command = self.formula_check_update)
        formula_confirm.grid(row = 1, column = len(self.formula_labels) + 2)
        
        master.bind('<Return>', lambda event: self.formula_check_update())  # Reaguje na stisknuti enteru
        master.bind('<KP_Enter>', lambda event: self.formula_check_update())  # Reaguje na stisknuti enteru
            
        # Skore
        score_frame = tk.Frame(master)
        score_frame.grid(row = 2, sticky = "W")
        
        score_label = tk.Label(score_frame, text = "Skóre:", font = ("Arial Black",16))
        score_label.grid(row = 0, column = 0, columnspan = 4, sticky = "W")
        
        score_label_widths = [7, 4, 7, 2]
        
        for i in range(len(self.score_labels)):
            self.score_label_objects.append(
                    tk.Label(score_frame, text = self.score_labels[i], 
                             width = score_label_widths[i], font = ("Arial",11)))
            self.score_label_objects[i].grid(row = 1, column = i, sticky = "W")
            
    #_________________________________F U N C T I O N S_______________________________#
    def oper_update(self):
        used_operators = self.used_operators                        # Ulozi si pouzita znamenka
        
        operators = [self.plus, self.minus, self.mul, self.div]     # Dostupna znamenka
        self.used_operators = []
        for i in range(len(operators)):
            if self.oper_vals[i].get():
                self.used_operators.append(operators[i])            # Pokud je znamenko zaskrtnute, prida jej do seznamu znamenek
                
        if(not used_operators):                                     # Pokud nebyla doposud pouzita zadna znamenka, vygeneruje priklad
            self.update()
    
    def formula_check_update(self):
        try:
            user_result = int(self.formula_user_result.get("1.0",tk.END))   # Precte a ulozi cislo
        except:
            user_result = "N"                                               # Pokud je cislo neplatne, vrati "N"
        
        if user_result == self.res:                                         # Pokud je vysledek spravny, aktualizuje skore a vygeneruje novy priklad
            self.update()
            self.score[0] += 1
            self.score_label_objects[1].configure(text = self.score[0])
            
        elif user_result == "N":                                            # Pokud je vysledek neplatny, nestane se nic
            pass
            
        else:                                                               # Pokud je vysledek spatne, aktualizuje skore
            self.score[1] += 1
            self.score_label_objects[3].configure(text = self.score[1])
        
        self.formula_user_result.delete("1.0",tk.END)                       # Smaze obsah textoveho pole

    def update(self):
        if(self.used_operators):
            random = randint(0, len(self.used_operators)-1)     
            self.used_operators[random]()                                   # Vybere nahodne znamenko ze senamu
            
            for i in range(len(self.formula_label_objects)):                # Aktualizuje priklad
                self.formula_labels = [self.x, self.oper, self.y, "="]
                self.formula_label_objects[i].configure(text = self.formula_labels[i])
    
    def plus(self):
        self.oper = "+"
        self.x = randint(1, 98)
        self.y = randint(1, 99-self.x)
        self.res = self.x + self.y
    
    def minus(self):
        self.oper = "-"
        self.x = randint(1, 99)
        self.y = randint(1, self.x)
        self.res = self.x - self.y
        
    def mul(self):
        self.oper = "*"
        self.x = randint(2, 10)
        self.y = randint(1, 99 // self.x)
        self.res = self.x * self.y
    
    def div(self):
        self.oper = "/"
        self.y = randint(2, 10)
        self.res = randint(1, 99 // self.y)
        self.x = self.y * self.res
        

root = tk.Tk()
root.title("Pocitani pro ZS")
app = App(root)
app.div()
app.oper_update()
root.mainloop()