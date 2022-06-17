import tkinter

canvas = tkinter.Canvas(width=640, height=480)

canvas.pack()

def stvorec():
    y1, y2 = 215, 265
    for i in range(1,9):
        canvas.create_rectangle(i*50, y1, i*50+50, y2)

def vyfarbi_stvorec(event):
    if event.y > 215 and event.y < 265:
        if event.x > 50 and event.x < 450:
            canvas.create_rectangle(event.x//50*50, 215, event.x//50*50+50, 265, fill='red')

stvorec()
canvas.bind('<ButtonPress-1>', vyfarbi_stvorec)    # po kliknuti vyfarbi stvorec nacerveno

canvas.mainloop()