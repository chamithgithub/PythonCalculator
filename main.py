import tkinter as tk
calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation +=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evoluatr_calculation():
    global calculation



def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")    


root =tk.Tk()
root.geometry("500x375")
root.title("calculator")

text_result =tk.Text(root, height=2,width=30,font=("Arial",24))
text_result.grid(columnspan=5)

btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation(1),width=5,font=("Arial",14))
btn_1.grid(row=1,column=1)

btn_2=tk.Button(root,text="2",command=lambda:add_to_calculation(2),width=5,font=("Arial",14))
btn_2.grid(row=1,column=2)

btn_3=tk.Button(root,text="3",command=lambda:add_to_calculation(3),width=5,font=("Arial",14))
btn_3.grid(row=1,column=3)


root.mainloop()