import tkinter
from tkinter import font

root = tkinter.Tk()
root.geometry('1150x650')
root.title('Paperweight')
root.resizable(0, 0)

font_canvas = tkinter.Canvas(root, width=1150, height=650, background='white')
font_canvas.place(x=0, y=0)
font_list = font.families()

x = 20
y = 10
for item in font_list:
    if x >= 1100:
        x = 20
        y = y + 20
    font_check = font.Font(family=item, size=10)
    font_canvas.create_text(x, y, text=item+"11", font=font_check)
    x = x + 160
    font_canvas.update()




root.mainloop()