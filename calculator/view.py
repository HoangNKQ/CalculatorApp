import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.controller = controller

        self.title ('Calculator')
        self.geometry('400x500')
        self.tk.call("source", "theme\sun-valley.tcl")
        self.tk.call("set_theme", "light")

        self.button_text = ''
        self.expression_text = ''
        self.setup_frame()
        self.init_frame()
        

    def setup_frame(self):
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 6)
        self.columnconfigure(0, weight = 1)
        #self.columnconfigure(1, weight = 1)


    def init_frame(self):
        expression = self.create_expression_frame(self)
        expression.grid(row= 0, column = 0, sticky= 'nsew', padx= 5, pady= 5)
        button = self.create_button_frame(self)
        button.grid(row= 1, column = 0, sticky= 'nsew', padx= 5, pady= 5)


    def create_expression_frame(self, parent):
        expression_frame = ttk.Frame(parent)
        expression_frame.rowconfigure(0, weight = 1)
        expression_frame.rowconfigure(1, weight = 4)
        expression_frame.columnconfigure(0, weight = 1)

        self.equation_label = ttk.Label(expression_frame, text= "equation", font=('Arial', 10))
        self.equation_label.grid(row= 0, column= 0, sticky= 'e', padx= 5, pady= 5)

        self.result_label = ttk.Label(expression_frame, text= "Result", font=('Arial', 30))
        self.result_label.grid(row= 1, column= 0, sticky = 'e', padx= 5, pady= 5)

        return expression_frame

    def history(self):
        pass

    def insert_expression(self, expression_text):
        self.equation_label.configure(text= expression_text)

    def insert_result(self, result_text):
        self.result_label.configure(text= result_text)



    def create_button_frame(self, parent):
        # Variables
        self.buttons = []
        button_text = [
            '(',')','C','+',
            '7','8','9','-',
            '4','5','6','*',
            '1','2','3','/',
            '+/-','0','.','='
            ]
        button_count = -1
        rows = 5

        # Button Frame
        button_frame = ttk.Frame(parent) 
        s = ttk.Style()
        s.configure('TButton', font=('Arial', 14))

        # Grid management
        for i in range(rows):
            if i < 4:
                button_frame.columnconfigure(i, weight = 1)
            button_frame.rowconfigure(i, weight = 1)
        
        #Create button and save to list 'buttons'
        for i in range(5):
            for j in range(4):
                button_count += 1
                self.buttons.append(ttk.Button(button_frame, text= button_text[button_count]))
                self.buttons[button_count].grid(row = i, column = j, sticky='nsew', padx= 2, pady= 2)

        return button_frame



    def init_display(self):
        self.mainloop()


def main():
    view = View()
    view.init_display()
    view.button_trigger()

if __name__ == '__main__':
    main()