import tkinter as tk
import random
window = tk.Tk()
window.geometry('800x600')

canv = tk.Canvas(window, height = 600, width = 800)
canv.pack()
colors = ['red','orange','yellow','green','blue']
score = 0

def new_ball():
    #clears screen, draws a random ball at a random place
    global x,y,r, canv
    x = random.randrange(100,700)
    y = random.randrange(100,500)
    r = random.randrange(30,50)
    color = random.choice(colors)
    for i in range(1000):
        ball = canv.create_oval(x+i-r,y+i-r,x+i+r,y+i+r,fill = color, width=0)#drawing a circle
        ball.pack()
        canv.delete(ball)
    #canv.after(1000,new_ball)#waits until repeating; neverending loop

def screamer(event):
    spooky_window = tk.Tk()
    boo = tk.Label(spooky_window, text='BOO!!!')
    boo.pack()

def add_points(event):
    global score
    if ((event.x-x)**2+(event.y-y)**2)**0.5 <= r:
        score += 1

def click(event):
    print('you just clicked at point', event.x, event.y)
    add_points(event)
    
def score_window(event):
    global score
    new_window = tk.Tk()
    new_window.geometry('400x300')
    tk.Label(new_window, text=str(score)).pack()

new_ball()
window.bind('<Button-1>', click)
window.bind_all('<Double-Button-1>', score_window)

mainloop()
'''b = tk.Button(window, text='c ur score', bg = 'magenta')
b.pack()
b.bind('<Button-1>', screamer)'''
"""b = tk.Button(window, text='c ur score', bg = 'magenta')
b.pack(side='BOTTOM')
b.bind('<Button-1>', screamer)"""
