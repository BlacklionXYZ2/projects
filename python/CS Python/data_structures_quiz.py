import tkinter as tk

root = tk.Tk()
root.title('Data Structures Quiz')
questions = {'what is a queue based off?': [{'A: LIFO': False, 'B: FIFO': True}, ], 
             'what data structure stores data in layers?': [{'A: Queues': False, 'B: Stacks': False, 'C: Trees': True}, '2x2']}
buttons = []

width, height = 300, 400
root.geometry(f'{width}x{height}')
root.minsize(width, height)
root.maxsize(width, height)

buttonArea = tk.Frame(root, width = int((2 * width) / 3), height = int(height / 3))
buttonArea.pack_propagate(False)
buttonArea.pack(pady = 20)

def showQuestion(question):
    global buttonArea, buttons, btn
    buttons = []
    for x in buttonArea.winfo_children():
        x.destroy()

    for x, text in enumerate(question[0]):
        btn = tk.Button(buttonArea, text = text)
        buttons.append([x, text])
        if len(question[0]) == 2:
            btn.grid(row = 0, column = x, sticky ='nsew')
        elif 2 < len(question[0]) <= 4:
            btn.grid(row = x // 2, column = x % 2, sticky = 'nsew')

    for r in range(2):
        buttonArea.grid_rowconfigure(r, weight = 1)
    for c in range(2):
        buttonArea.grid_columnconfigure(c, weight = 1)

    print(buttons)

showQuestion(questions['what is a queue based off?'])
showQuestion(questions['what data structure stores data in layers?'])

root.mainloop()