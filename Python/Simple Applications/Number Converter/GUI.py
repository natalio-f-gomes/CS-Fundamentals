from tkinter import *
from ConvertNum import ConvertNum

class ConvertNumGUI:
    def __init__(self):
        self.app = Tk()
        self.app.title("Number Converter")
        self.app.geometry("500x300")
        
        # Create label and entry widgets for number and base inputs
        num_label = Label(self.app, text="Enter number:")
        num_label.pack(pady=10)
        self.num_entry = Entry(self.app)
        self.num_entry.pack()

        base_label = Label(self.app, text="Enter base of number:")
        base_label.pack(pady=10)
        self.base_entry = Entry(self.app)
        self.base_entry.pack()

        # Create label and entry widgets for desired base
        to_base_label = Label(self.app, text="Convert to base:")
        to_base_label.pack(pady=10)
        self.to_base_entry = Entry(self.app)
        self.to_base_entry.pack()

        # Create a button to convert the number and display the result
        convert_button = Button(self.app, text="Convert", command=self.convert)
        convert_button.pack(pady=10)

        # Create a label to display the result
        self.result_label = Label(self.app, text="")
        self.result_label.pack(pady=10)

        self.app.mainloop()

    def convert(self):
        # Get the input values from the entry widgets
        num = int(self.num_entry.get())
        num_base = int(self.base_entry.get())
        to_base = int(self.to_base_entry.get())

        # Create a ConvertNum object and convert the number
        converter = ConvertNum(num, num_base, to_base)
        result = converter.result

        # Update the result label
        self.result_label.config(text=str(result))


run = ConvertNumGUI()
