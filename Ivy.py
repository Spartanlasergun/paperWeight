import tkinter
import math
import random
import time


root = tkinter.Tk()
root.geometry('1150x650')
root.title('Paperweight')
root.resizable(0, 0)


Graph = tkinter.Canvas(root, width=1150, height=650, background="ghostwhite")
Graph.place(x=0, y=0)

#Build Axis
#Graph.configure(scrollregion=(-575, -325, 575, 325))
Graph.create_line(0, 250, 300, 250, width=2)
Graph.create_line(300, 250, 300, 0, width=2)
Graph.create_line(0, 50, 350, 50, width=2)
Graph.create_line(350, 50, 350, 0, width=2)

x = 0
count = 0
factor = random.random() + 1
x_1 = 0
y_1 = 250
vines = []
while x <= 700:
    if count == 15:
        count = 0
        factor = random.random() + random.randint(3, 5)
    angle = math.radians(x) * (factor + 1)
    y = (10 * math.sin(angle)) + 250
    a = x
    b = y
    if a >= 315: #first turn
        a = y + 50
        b = -x + 575
        if b <= 40: #second turn
            a = x - 200
            b = y - 200
            if a >= 360: #third turn
                a = y + 100
                b = -x + 590

    #Graph.create_line(x_1, y_1, a, b)
    temp = [x_1, y_1]
    vines.append(temp)

    x_1 = a
    y_1 = b

    x = x + 5
    count = count + 1

#create fibonacci list
F_N = [0, 1]
stop = 0
first = 0
second = 1
while stop != 100:
    F_Next = F_N[first] + F_N[second]
    first = first + 1
    second = second + 1
    F_N.append(F_Next)
    stop = stop + 1


test = 0
a = 0
b = 1
c = 2
sprouts = []
leaves = []
while test != 65:
    colour = "green"
    thickness = random.randint(2, 4)
    Graph.create_line(vines[a][0], vines[a][1], vines[b][0], vines[b][1], vines[c][0], vines[c][1],
                      width=thickness, fill=colour, smooth=1)

    if thickness >= 3:
        x_1 = vines[b][0]
        y_1 = vines[b][1]
        curve_shift_1 = random.randint(1, 5)
        curve_shift_2 = random.randint(5, 15)
        offset_1 = random.randint(1, 5)
        offset_2 = random.randint(5, 15)
        if (x_1 < y_1) and (x_1 < 350):
            polar_shift = random.randint(0, 1)
            if polar_shift == 0:
                offset_1 = -offset_1
                offset_2 = -offset_2
            polar_shift = random.randint(0, 1)
            if polar_shift == 0:
                curve_shift_1 = -curve_shift_1
                curve_shift_2 = -curve_shift_2
            Graph.create_line(x_1, y_1,
                              (x_1 + curve_shift_1), (y_1 + offset_1),
                              (x_1 + curve_shift_2), (y_1 + offset_2),
                              width=2, fill=colour, smooth=1)

            #store sprout data
            temp = [x_1, y_1,
                    (x_1 + curve_shift_1), (y_1 + offset_1),
                    (x_1 + curve_shift_2), (y_1 + offset_2)]
            sprouts.append(temp)

            #create_leaf
            l_base_x = x_1 + curve_shift_2
            l_base_y = y_1 + offset_2
            apex_x = l_base_x + curve_shift_2
            apex_y = l_base_y + offset_2
            Graph.create_polygon(l_base_x, l_base_y,
                                 (apex_x - curve_shift_1), l_base_y,
                                 apex_x, (apex_y - offset_1),
                                 apex_x, apex_y,
                                 (apex_x - offset_1), apex_y,
                                 l_base_x, (apex_y - offset_1),
                                 l_base_x, l_base_y,
                                 fill="lime", outline="black", smooth=1)

            #store leaf_data
            temp_1 = [l_base_x, l_base_y,
                        (apex_x - curve_shift_1), l_base_y,
                        apex_x, (apex_y - offset_1),
                        apex_x, apex_y,
                        (apex_x - offset_1), apex_y,
                        l_base_x, (apex_y - offset_1),
                        l_base_x, l_base_y]
            leaves.append(temp_1)

        elif (x_1 > y_1) and (y_1 < 240):
            polar_shift = random.randint(0, 1)
            if polar_shift == 0:
                offset_1 = -offset_1
                offset_2 = -offset_2
            polar_shift = random.randint(0, 1)
            if polar_shift == 0:
                curve_shift_1 = -curve_shift_1
                curve_shift_2 = -curve_shift_2
            Graph.create_line(x_1, y_1,
                              (x_1 + offset_1), (y_1 + curve_shift_1),
                              (x_1 + offset_2), (y_1 + curve_shift_2),
                              width=2, fill=colour, smooth=1)

            # store sprout data
            temp = [x_1, y_1,
                    (x_1 + offset_1), (y_1 + curve_shift_1),
                    (x_1 + offset_2), (y_1 + curve_shift_2)]
            sprouts.append(temp)

            #create_leaf
            l_base_x = x_1 + offset_2
            l_base_y = y_1 + curve_shift_2
            apex_x = l_base_x + offset_2
            apex_y = l_base_y + curve_shift_2
            Graph.create_polygon(l_base_x, l_base_y,
                                 (apex_x - offset_1), l_base_y,
                                 apex_x, (apex_y - offset_1),
                                 apex_x, apex_y,
                                 (apex_x - offset_1), apex_y,
                                 l_base_x, (apex_y - curve_shift_1),
                                 l_base_x, l_base_y,
                                 fill="lime", outline="black", smooth=1)

            # store leaf_data
            temp_1 = [l_base_x, l_base_y,
                        (apex_x - offset_1), l_base_y,
                        apex_x, (apex_y - offset_1),
                        apex_x, apex_y,
                        (apex_x - offset_1), apex_y,
                        l_base_x, (apex_y - curve_shift_1),
                        l_base_x, l_base_y]
            leaves.append(temp_1)

    a = a + 2
    b = b + 2
    c = c + 2
    test = test + 1
    Graph.update()
    time.sleep(0.02)
Graph.create_line(0, 250, 300, 250, width=2, dash=(125, 125))
Graph.create_line(300, 250, 300, 0, width=2, dash=(125, 125))

root.mainloop()