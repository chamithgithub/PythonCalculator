import tkinter as tk

calculation = ""
def add_to_calculation(symbol):
    pass
def evoluatr_calculation():
    pass
def clear_field():
    pass

root =tk.Tk()
root.geometry("500x375")
root.title("calculator")

text_result =tk.Text(root, height=2,width=30,font=("Arial",24))
text_result.grid(columnspan=5)
root.mainloop()