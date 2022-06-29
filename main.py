import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

#funcion de botones, por lo pronto esta funcion es para que no hagan nada.
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text='Do nothing')
    button.pack()
    
def textCompare():
    input1 = text1.get('1.0', END)
    input2 = text2.get('1.0', END)
    rev1 = input1.split()
    rev2 = input2.split()    
    finalText = ''   
    for x in range(len(rev1)):        
        if rev1[x] == rev2[x]:
            finalText=finalText+(rev1[x]+" ")
        else:
            finalText = finalText+(f'!!!!!!1stDoc:{rev1[x]} / 2ndDoc:{rev2[x]}!!!!!! ')
    result.configure(state="normal")
    result.insert('end', finalText)
    result.configure(state='disabled')
    print (finalText)   
    
root = tk.Tk()
root.geometry('1000x500')
root.title("Text Compare")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(2, weight=1)

#Frames for content acomodation
frame1 = Frame(root, height=5)
frame2 = LabelFrame(root, text='Texto 1', highlightbackground='lightgrey', highlightthickness=2)
frame2.grid(column=0, row=1, sticky='we')
frame3 = LabelFrame(root, text='Texto 2',highlightbackground='lightgrey', highlightthickness=2)
frame3.grid(column=1, row=1)
frame4 = LabelFrame(root, text='Result',highlightbackground='lightgreen', highlightthickness=2)
frame4.grid(column=2, row=1)
frame5 = Frame(root)
frame5.grid(row=3)

#Menus
menubar= Menu(frame1)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open File", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label='exit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)



######### COMPONENTES DE LA VENTANA ###########

#Editable textbox
text1 = scrolledtext.ScrolledText(frame2)
text1.pack()
text2 = scrolledtext.ScrolledText(frame3)
text2.pack()

#Textbox for revised Text 
result = Text(frame4, state='disabled')

#Boton de Comparacion
buttonComp = Button(frame5, text="Compare", command=textCompare)
buttonComp.pack()


result.pack()

root.config(menu=menubar)
root.mainloop()