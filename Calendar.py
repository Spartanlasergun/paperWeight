import os
from os import path
import tkinter
import time
import random
import subprocess
from datetime import datetime
from tkinter import font

root = tkinter.Tk()
root.geometry('1150x650')
root.title('Paperweight')
root.resizable(0, 0)

#get current working directory
cur_dir = os.getcwd()

#check for polyfile directory and create one if necessary
sub_dirs = [f.path for f in os.scandir(cur_dir) if f.is_dir()]
polyfile_check = 0
polyfile = cur_dir + "/polyfile"
for dir in sub_dirs:
    if path.basename(dir) == "polyfile":
        polyfile_check = 1
if polyfile_check == 0:
    os.mkdir(polyfile)

Main_Canvas = tkinter.Canvas(root, width=1150, height=650, background='ghostwhite')
Main_Canvas.place(x=-1, y=-1)

#----------------------------------------Calendar_Operations_BEGIN----------------------------------------------

#load images
Calendar_IMG = tkinter.PhotoImage(file="Calendar_2.png")

#For Global Use
Month_List = ["null", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
Month_Abbrev = ["null", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

Current_Month = "January"
Current_Year = 2020
First_Day = "Wednesday"
Current_Date = 1
month_get = 1
year_get = 2020

# store data for highlighted date in seperate variable so
# the user can update the current date from settings
Month_Highlight = Current_Month
Year_Highlight = Current_Year
Date_Highlight = Current_Date

#Click Highlight
Click_Highlight = None

#Define Calendar Date Boxes outside of Calendar_Base Method
cal_boxes = []

#Vines Animation
Load_Vines = False
Load_Vines_Delay = True
seed = cur_dir + "/Ivy.py"
germinate = subprocess.Popen(["python", seed])
germinate.wait()


def Calendar_Base():
    #Clear Canvas to initialize
    Main_Canvas.delete("all")

    #display background image
    Main_Canvas.create_image(0, 50, anchor='nw', image=Calendar_IMG)
    Main_Canvas.create_rectangle(75, 50, 225, 100, fill="white")

    global cal_boxes
    cal_boxes = []

    #basic calendar control panel outline
    line_colour = "black"
    Main_Canvas.create_line(-1, 50, 350, 50, width='2', fill=line_colour)
    Main_Canvas.create_line(-1, 250, 300, 250, width='2', fill=line_colour)
    Main_Canvas.create_line(300, -1, 300, 250, width='2', fill=line_colour)
    Main_Canvas.create_line(350, -1, 350, 50, width='2', fill=line_colour)
    Main_Canvas.create_line(75, 50, 75, 100, width='2', fill=line_colour)
    Main_Canvas.create_line(225, 50, 225, 100, width='2', fill=line_colour)
    Main_Canvas.create_line(75, 100, 225, 100, width='2', fill=line_colour)

    #IVY
    global Load_Vines
    global Load_Vines_Delay
    if Load_Vines == True:
        get_vines = open(cur_dir + "/vines.txt", "r", encoding='utf8')
        vines_pull = get_vines.read().splitlines()
        get_vines.close()
        vines = []
        for item in vines_pull:
            coords = item.split(",")
            x = coords[0]
            y = coords[1]
            temp = [x, y]
            vines.append(temp)
        stop = 0
        a = 0
        b = 1
        c = 2
        while stop != 65:
            thickness = random.randint(2, 4)
            Main_Canvas.create_line(vines[a][0], vines[a][1], vines[b][0], vines[b][1], vines[c][0], vines[c][1],
                              width=thickness, fill="green", smooth=1)
            a = a + 2
            b = b + 2
            c = c + 2
            stop = stop + 1
            if Load_Vines_Delay == True:
                Main_Canvas.update()
                time.sleep(0.02)
        get_sprouts = open(cur_dir + "/sprouts.txt", "r", encoding='utf8')
        sprouts = get_sprouts.read().splitlines()
        get_sprouts.close()
        for item in sprouts:
            thickness = random.randint(2, 4)
            coords = item.split(",")
            x_1 = coords[0]
            y_1 = coords[1]
            x_2 = coords[2]
            y_2 = coords[3]
            x_3 = coords[4]
            y_3 = coords[5]
            Main_Canvas.create_line(x_1, y_1, x_2, y_2, x_3, y_3, width=thickness, fill="green", smooth=1)

        get_leaves = open(cur_dir + "/leaves.txt", "r", encoding='utf8')
        leaves = get_leaves.read().splitlines()
        get_leaves.close()
        for poly in leaves:
            item = poly.split(",")
            x_1 = item[0]
            y_1 = item[1]
            x_2 = item[2]
            y_2 = item[3]
            x_3 = item[4]
            y_3 = item[5]
            x_4 = item[6]
            y_4 = item[7]
            x_5 = item[8]
            y_5 = item[9]
            x_6 = item[10]
            y_6 = item[11]
            x_7 = item[12]
            y_7 = item[13]
            Main_Canvas.create_polygon(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5, x_6, y_6, x_7, y_7,
                                       fill="lime", outline="black", smooth=1)
        Load_Vines_Delay = False

    #define date grid boundaries and properties
    lower_boundary = 240
    left_boundary = 10
    right_boundary = 290
    upper_boundary = 110
    row_width = (lower_boundary - upper_boundary) / 7
    column_width = (right_boundary - left_boundary) / 7

    while upper_boundary < lower_boundary:
        while left_boundary < right_boundary:
            #create date boxes
            Main_Canvas.create_rectangle(left_boundary, upper_boundary,
                                         (left_boundary+column_width), (upper_boundary + row_width),
                                         fill="white")

            #store co-ordinates for each date box in "cal_boxes"
            temp = [left_boundary, upper_boundary,
                                         (left_boundary+column_width), (upper_boundary + row_width)]
            cal_boxes.append(temp)

            #increment left_boundary
            left_boundary = left_boundary + column_width

        #reset left boundary and increment upper boundary
        left_boundary = 10
        upper_boundary = upper_boundary + row_width

    #Display Weekday Headings
    upper_boundary = 110
    left_boundary = 10

    day = 0
    inc = 0
    heading_colour = "grey"
    text_colour = "white"
    weekday_font = font.Font(family="Algerian", size=11)
    while day != 7:
        x = (((int(cal_boxes[day][2])) - (int(cal_boxes[day][0]))) / 2) + inc + left_boundary
        y = (((int(cal_boxes[day][3])) - (int(cal_boxes[day][1]))) / 2) + upper_boundary
        inc = inc + column_width
        if day == 0:
            Main_Canvas.create_rectangle(cal_boxes[day][0], cal_boxes[day][1],
                                         cal_boxes[day][2], cal_boxes[day][3],
                                         fill=heading_colour)
            Main_Canvas.create_text(x, y, text="S", anchor="center",
                                    font=weekday_font, fill=text_colour)
        elif day == 1:
            Main_Canvas.create_rectangle(cal_boxes[day][0], cal_boxes[day][1],
                                         cal_boxes[day][2], cal_boxes[day][3],
                                         fill=heading_colour)
            Main_Canvas.create_text(x, y, text="M", anchor="center",
                                    font=weekday_font, fill=text_colour)
        elif day == 2:
            Main_Canvas.create_rectangle(cal_boxes[day][0], cal_boxes[day][1],
                                         cal_boxes[day][2], cal_boxes[day][3],
                                         fill=heading_colour)
            Main_Canvas.create_text(x, y, text="T", anchor="center",
                                    font=weekday_font, fill=text_colour)
        elif day == 3:
            Main_Canvas.create_rectangle(cal_boxes[day][0], cal_boxes[day][1],
                                         cal_boxes[day][2], cal_boxes[day][3],
                                         fill=heading_colour)
            Main_Canvas.create_text(x, y, text="W", anchor="center",
                                    font=weekday_font, fill=text_colour)
        elif day == 4:
            Main_Canvas.create_rectangle(cal_boxes[day][0], cal_boxes[day][1],
                                         cal_boxes[day][2], cal_boxes[day][3],
                                         fill=heading_colour)
            Main_Canvas.create_text(x, y, text="T", anchor="center",
                                    font=weekday_font, fill=text_colour)
        elif day == 5:
            Main_Canvas.create_rectangle(cal_boxes[day][0], cal_boxes[day][1],
                                         cal_boxes[day][2], cal_boxes[day][3],
                                         fill=heading_colour)
            Main_Canvas.create_text(x, y, text="F", anchor="center",
                                    font=weekday_font, fill=text_colour)
        elif day == 6:
            Main_Canvas.create_rectangle(cal_boxes[day][0], cal_boxes[day][1],
                                         cal_boxes[day][2], cal_boxes[day][3],
                                         fill=heading_colour)
            Main_Canvas.create_text(x, y, text="S", anchor="center",
                                    font=weekday_font, fill=text_colour)
        day = day + 1

    #create calendar arrow buttons
    Main_Canvas.create_polygon(100, 65, 100, 85, 90, 75, 100, 65, fill="black", activefill="cyan")
    Main_Canvas.create_polygon(200, 65, 200, 85, 210, 75, 200, 65, fill="black", activefill="cyan")


def Cal_Setup():
    global First_Day
    global Current_Month
    global Current_Year
    global month_get
    global cal_boxes
    global Month_Highlight
    global Year_Highlight
    global Date_Highlight
    global Click_Highlight
    global Click_Attrib

    #For Current Date Highlight
    global Month_Highlight
    global Year_Highlight
    global Date_Highlight

    # Build Calendar Base
    Calendar_Base()

    #Reset Cal Boxes
    reset = 0
    while reset != 35:
        temp = cal_boxes[reset]
        if len(temp) == 6:
            del temp[5]
            del temp[4]
        if len(temp) == 5:
            del temp[4]
        cal_boxes[reset] = temp
        reset = reset + 1

    # Define Calendar Default Information
    start = 7  #referenced before assignment
    if First_Day == "Sunday":
        start = start + 0
    elif First_Day == "Monday":
        start = start + 1
    elif First_Day == "Tuesday":
        start = start + 2
    elif First_Day == "Wednesday":
        start = start + 3
    elif First_Day == "Thursday":
        start = start + 4
    elif First_Day == "Friday":
        start = start + 5
    elif First_Day == "Saturday":
        start = start + 6

    end = 31 #referenced before assignment
    if Current_Month == "January":
        end = 31 + start
    elif Current_Month == "February":
        leap = Current_Year/4
        if leap.is_integer():
            end = 29 + start
        else:
            end = 28 + start
    elif Current_Month == "March":
        end = 31 + start
    elif Current_Month == "April":
        end = 30 + start
    elif Current_Month == "May":
        end = 31 + start
    elif Current_Month == "June":
        end = 30 + start
    elif Current_Month == "July":
        end = 31 + start
    elif Current_Month == "August":
        end = 31 + start
    elif Current_Month == "September":
        end = 30 + start
    elif Current_Month == "October":
        end = 31 + start
    elif Current_Month == "November":
        end = 30 + start
    elif Current_Month == "December":
        end = 31 + start

    lower_boundary = 240
    left_boundary = 10
    right_boundary = 290
    upper_boundary = 110
    row_width = (lower_boundary - upper_boundary) / 7
    column_width = (right_boundary - left_boundary) / 7
    Date = 1

    Cal_Title = Month_Abbrev[month_get] + " " + str(Current_Year)
    title_font = font.Font(family="Garamond", size=14)
    number_font = font.Font(family="Arial CE", size=10)
    Main_Canvas.create_text(150, 75, text=Cal_Title, font=title_font)

    while start != end:
        x = (cal_boxes[start][2]) - (column_width / 2)
        y = (cal_boxes[start][3]) - (row_width / 2)

        # click highlight
        if (Click_Highlight != None) and (Date == Click_Highlight) and (Click_Attrib == "grid"):
            Main_Canvas.create_oval((x - 8), (y - 8), (8 + x), (8 + y), fill="lime")

        if (Date == Date_Highlight) and (Current_Year == Year_Highlight) and (Current_Month == Month_Highlight):
            Main_Canvas.create_oval((x - 8), (y - 8), (8 + x), (8 + y), fill="orange")
            Main_Canvas.create_text(x, y, text=str(Date), fill="white", activefill="cyan",
                                    font=number_font)
        else:
            Main_Canvas.create_text(x, y, text=str(Date), fill="black", activefill="cyan",
                                    font=number_font)

        #Attach Dates to assigned boxes
        temp = cal_boxes[start]
        try:
            temp[4] = (str(Current_Year) + str(Current_Month) + str(Date))
            temp[5] = Date
        except:
            temp.append(str(Current_Year) + str(Current_Month) + str(Date))
            temp.append(Date)
        cal_boxes[start] = temp

        #increment counters
        Date = Date + 1
        start = start + 1

    #Creating Grey Dates For Previous/Following Months

    #Previous Month
    if month_get == 1:
        prev_month = Month_List[12]
    else:
        prev_month = Month_List[(month_get - 1)]
    if prev_month == "January":
        end = 31
    elif prev_month == "February":
        leap = Current_Year / 4
        if leap.is_integer():
            end = 29
        else:
            end = 28
    elif prev_month == "March":
        end = 31
    elif prev_month == "April":
        end = 30
    elif prev_month== "May":
        end = 31
    elif prev_month == "June":
        end = 30
    elif prev_month == "July":
        end = 31
    elif prev_month == "August":
        end = 31
    elif prev_month == "September":
        end = 30
    elif prev_month == "October":
        end = 31
    elif prev_month == "November":
        end = 30
    elif prev_month == "December":
        end = 31

    #empty boxes check
    prev_count = 0
    limit = 0
    while limit != 21:
        l_check = len(cal_boxes[limit])
        if l_check <= 4:
            prev_count = prev_count + 1
        limit = limit + 1
    prev_grey_boxes = prev_count - 7
    prev_holder = prev_grey_boxes
    if prev_grey_boxes != 0:
        while prev_grey_boxes != 0:
            index = prev_grey_boxes + 6
            x = (cal_boxes[index][2]) - (column_width / 2)
            y = (cal_boxes[index][3]) - (row_width / 2)
            Main_Canvas.create_text(x, y, text=str(end), fill="grey", activefill="cyan")

            #attach dates to assigned boxes
            temp = cal_boxes[index]
            temp.append(end)
            cal_boxes[index] = temp

            #decrement counters
            end = end - 1
            prev_grey_boxes = prev_grey_boxes - 1

    #Following Month
    foll_count = 0
    limit = 48
    while limit != 21:
        l_check = len(cal_boxes[limit])
        if l_check <= 4:
            foll_count = foll_count + 1
        limit = limit - 1
    if Current_Month == "January":
        end = 31
    elif Current_Month == "February":
        leap = Current_Year / 4
        if leap.is_integer():
            end = 29
        else:
            end = 28
    elif Current_Month == "March":
        end = 31
    elif Current_Month == "April":
        end = 30
    elif Current_Month == "May":
        end = 31
    elif Current_Month == "June":
        end = 30
    elif Current_Month == "July":
        end = 31
    elif Current_Month == "August":
        end = 31
    elif Current_Month == "September":
        end = 30
    elif Current_Month == "October":
        end = 31
    elif Current_Month == "November":
        end = 30
    elif Current_Month == "December":
        end = 31

    foll_grey_boxes = foll_count

    if foll_grey_boxes != 0:
        while foll_grey_boxes != 0:
            index = foll_grey_boxes + end + 6 + prev_holder
            x = (cal_boxes[index][2]) - (column_width / 2)
            y = (cal_boxes[index][3]) - (row_width / 2)
            Main_Canvas.create_text(x, y, text=str(foll_grey_boxes), fill="grey", activefill="cyan")
            #attach dates to assigned boxes
            temp = cal_boxes[index]
            temp.append(foll_grey_boxes)
            cal_boxes[index] = temp

            #decrement counters
            foll_grey_boxes = foll_grey_boxes - 1

def Cal_Backward():
    global First_Day
    global Current_Month
    global Current_Year
    global month_get
    global year_get

    #set click attribute
    global Click_Attrib
    Click_Attrib = "arrow"

    # Update Month and Year
    month_get = month_get - 1
    if month_get == 0:
        month_get = month_get - 1
        year_get = year_get - 1
        Current_Year = year_get
        Current_Month = Month_List[12]
        month_get = 12
    else:
        Current_Month = Month_List[month_get]

    # Update First Day
    if Current_Month == "January":
        end = 31
    elif Current_Month == "February":
        leap = Current_Year / 4
        if leap.is_integer():
            end = 29
        else:
            end = 28
    elif Current_Month == "March":
        end = 31
    elif Current_Month == "April":
        end = 30
    elif Current_Month == "May":
        end = 31
    elif Current_Month == "June":
        end = 30
    elif Current_Month == "July":
        end = 31
    elif Current_Month == "August":
        end = 31
    elif Current_Month == "September":
        end = 30
    elif Current_Month == "October":
        end = 31
    elif Current_Month == "November":
        end = 30
    elif Current_Month == "December":
        end = 31
    while end > 7:
        end = end - 7
    remainder = end
    cur_val = (Weekdays.index(First_Day))
    if remainder > cur_val:
        First_Day = Weekdays[(7 - (remainder - cur_val))]
    else:
        First_Day = Weekdays[cur_val - remainder]
    Cal_Setup()

def Cal_Forward():
    global First_Day
    global Current_Month
    global Current_Year
    global month_get
    global year_get

    # set click attribute
    global Click_Attrib
    Click_Attrib = "arrow"

    if Current_Month == "January":
        end = 31
    elif Current_Month == "February":
        leap = Current_Year / 4
        if leap.is_integer():
            end = 29
        else:
            end = 28
    elif Current_Month == "March":
        end = 31
    elif Current_Month == "April":
        end = 30
    elif Current_Month == "May":
        end = 31
    elif Current_Month == "June":
        end = 30
    elif Current_Month == "July":
        end = 31
    elif Current_Month == "August":
        end = 31
    elif Current_Month == "September":
        end = 30
    elif Current_Month == "October":
        end = 31
    elif Current_Month == "November":
        end = 30
    elif Current_Month == "December":
        end = 31
    remainder = end - 28
    cur_val = (Weekdays.index(First_Day))
    if (remainder + cur_val) <= 6:
        First_Day = Weekdays[(remainder + cur_val)]
    else:
        First_Day = Weekdays[((remainder + cur_val) - 7)]

    month_get = month_get + 1
    if month_get == 13:
        month_get = 1
        Current_Month = Month_List[1]
        year_get = year_get + 1
        Current_Year = year_get
    Current_Month = Month_List[month_get]
    Cal_Setup()

def update_calendar():
    global year_get
    global month_get
    global Current_Date
    global Month_Highlight
    global Year_Highlight
    global Date_Highlight
    global Load_Vines

    date_data_get = datetime.now()  # Fetch OS Time and Date Information
    month = date_data_get.month
    year = date_data_get.year
    day = date_data_get.day
    while year_get > year:
        Cal_Backward()
    while year_get < year:
        Cal_Forward()
    while month_get > month:
        Cal_Backward()
    while month_get < month:
        Cal_Forward()

    Month_Highlight = Month_List[month]
    Year_Highlight = year
    Date_Highlight = day

    Load_Vines = True


def Calendar_Grid_Click():
    global cal_index
    global cal_boxes
    global Click_Highlight

    # set click attribute
    global Click_Attrib

    if len(cal_boxes[cal_index]) == 5:
        fetch = cal_boxes[cal_index]
        date = str(fetch[4])
        Click_Highlight = int(date)
        if cal_index < 21:
            Cal_Backward()
        elif cal_index > 21:
            Cal_Forward()
        Click_Attrib = "grid"
        Cal_Setup()
        Main_Canvas.create_text(575, 325, text=date)
        for item in cal_boxes:
            if len(item) == 6:
                if item[5] == int(date):
                    Main_Canvas.create_text(575, 350, text=item[4])
    elif len(cal_boxes[cal_index]) == 6:
        fetch = cal_boxes[cal_index]
        Click_Highlight = int(fetch[5])
        Click_Attrib = "grid"
        Cal_Setup()
        Main_Canvas.create_text(575, 325, text=str(fetch[5]))
        Main_Canvas.create_text(575, 350, text=str(fetch[4]))

#control Calendar for click bindings
def Cal_Switchboard(event):
    #retrieve calendar grid boxes
    global cal_boxes

    #calendar arrow bindings
    if (event.x < 105) and (event.x > 85) and (event.y > 65) and (event.y < 85):
        Cal_Backward()
        settings_icon()
        username_display()
    elif (event.x < 215) and (event.x > 195) and (event.y > 65) and (event.y < 85):
        Cal_Forward()
        settings_icon()
        username_display()

    #calendar grid boxes bindings
    global cal_index
    index_check = 0
    for coords in cal_boxes:
        if (event.x < coords[2]) and (event.x > coords[0]) and (event.y > coords[1]) and (event.y < coords[3]):
            cal_index = index_check
            Calendar_Grid_Click()
            settings_icon()
            username_display()
        index_check = index_check + 1

    #settings binding
    if (event.x < 350) and (event.x > 300) and (event.y > 0) and (event.y < 50):
        settings()
    
    #exit settings binding
    

#----------------------------------------Calendar_Operations END----------------------------------------------

#---------------------------------------Display_Username_Operations_BEGIN-------------------------------------

def username_display():
    global name
    heading = font.Font(family="Segoe UI Black11", size=16, weight="bold")
    Main_Canvas.create_text(150, 25, text=name, font=heading)


#---------------------------------------Display_Username_Operations_END---------------------------------------

#----------------------------------------Settings_Operations_BEGIN--------------------------------------------
def settings_click(event):
    global boot
    #exit settings
    if (event.x < 1100) and (event.x > 1075) and (event.y > 50) and (event.y < 75):
        boot = True
        Methods_Sequence()

    #create new user binding
    if (event.x < 300) and (event.x > 150) and (event.y > 100) and (event.y < 125):
        boot = 0
        Methods_Sequence()

    if (event.x < 300) and (event.x > 150) and (event.y > 125) and (event.y < 150):
        switch_user()

def settings():
    # create click binding
    Main_Canvas.bind('<Button>', settings_click)

    heading = font.Font(family="Segoe UI Black11", size=16, weight="bold")
    heading_2 = font.Font(family="Segoe UI Black11", size=10)
    body = font.Font(family="Segoe UI11", size=10)

    Main_Canvas.create_rectangle(50, 50, 1100, 600, fill="white", outline="black", width=2) #main window
    Main_Canvas.create_rectangle(50, 50, 1100, 75, fill="grey15", outline="grey15") #settings bar
    Main_Canvas.create_rectangle(1075, 50, 1100, 75, fill="red3")
    Main_Canvas.create_line(1075, 50, 1100, 75, width=2)
    Main_Canvas.create_line(1075, 75, 1100, 50, width=2)
    Main_Canvas.create_rectangle(1075, 50, 1100, 75, activefill="red")
    Main_Canvas.create_text(575, 64, text="SETTINGS", fill="white", font=heading)
    Main_Canvas.create_rectangle(50, 75, 1100, 100, fill="grey30") #settings categories bar
    Main_Canvas.create_text(225, 87, text="USERS", fill="white", font=heading_2)
    Main_Canvas.create_text(575, 87, text="DISPLAY", fill="white", font=heading_2)
    Main_Canvas.create_text(925, 87, text="CALCUALTIONS", fill="white", font=heading_2)
    Main_Canvas.create_line(400, 75, 400, 600)
    Main_Canvas.create_line(750, 75, 750, 600)
    Main_Canvas.create_text(225, 112, text="Create New User", fill="blue", activefill="cyan", font=body)
    Main_Canvas.create_text(225, 137, text="Switch User", fill="blue", activefill="cyan", font=body)
    Main_Canvas.create_text(225, 162, text="Delete User", fill="blue", activefill="cyan", font=body)
    Main_Canvas.create_text(225, 187, text="Clear User Data", fill="blue", activefill="cyan", font=body)
    Main_Canvas.create_text(575, 112, text="Change Display Theme", fill="blue", activefill="cyan", font=body)
    Main_Canvas.create_text(925, 112, text="Units of Measurement", fill="blue", activefill="cyan", font=body)
    Main_Canvas.create_text(925, 137, text="Advanced Calculations", fill="blue", activefill="cyan", font=body)

    # imaginary boxes for bindings
    #Main_Canvas.create_rectangle(150, 100, 300, 125) --->create new user
    #Main_Canvas.create_rectangle(150, 125, 300, 150) --->switch user

def settings_icon():
    Main_Canvas.create_text(325, 25, text="Settings", activefill="cyan")

#----------------------------------------Settings_Operations_END----------------------------------------------



#----------------------------------------Switch_User_Operations_BEGIN-----------------------------------------
def switch_user_click(event):
    global select_username

    if (event.x < 595) and (event.x > 555) and (event.y > 280) and (event.y < 300):
        select_username = select_username + 1
        switch_user()

    if (event.x < 595) and (event.x > 555) and (event.y > 350) and (event.y < 370):
        select_username = select_username + 1
        switch_user()

    if (event.x < 595) and (event.x > 555) and (event.y > 390) and (event.y < 410):
        global name
        global usernames
        name = usernames[select_username]
        settings()

global select_username
select_username = 0

def switch_user():
    # create click binding
    Main_Canvas.bind('<Button>', switch_user_click)

    #Read Usernames
    users = [f.path for f in os.scandir(polyfile) if f.is_dir()]
    global usernames
    usernames = []
    for name in users:
        username = path.basename(name)
        usernames.append(username)

    heading = font.Font(family="Segoe UI Black11", size=16, weight="bold")
    heading_2 = font.Font(family="Segoe UI Black11", size=20)

    Main_Canvas.create_rectangle(325, 125, 825, 525, fill="white", outline="black", width=2)  # main window
    Main_Canvas.create_rectangle(325, 125, 825, 150, fill="grey15", outline="grey15")  # settings bar
    Main_Canvas.create_text(575, 137, text="SWTICH USER", fill="white", font=heading)

    #create arrows
    #up
    Main_Canvas.create_polygon(595, 300, 555, 300, 575, 280, 595, 300, fill="black", activefill="cyan")
    #down
    Main_Canvas.create_polygon(595, 350, 555, 350, 575, 370, 595, 350, fill="black", activefill="cyan")

    #OK BUTTON
    Main_Canvas.create_rectangle(555, 390, 595, 410, fill="grey")
    Main_Canvas.create_text(575, 400, text="OK", font=heading, activefill="cyan")

    global select_username
    all = len(usernames) - 1
    if select_username < 0:
        select_username = all
    if select_username > all:
        select_username = 0
    Main_Canvas.create_text(575, 325, text=usernames[select_username], font=heading_2)

#----------------------------------------Switch_User_Operations_END-------------------------------------------


#----------------------------------------Boot_Screen_Operations_BEGIN-----------------------------------------
#Date of Birth
global dob_month
global dob_year
global dob_day
global gender
dob_month = 1
dob_year = 2000
dob_day = 1
gender = None

#load images
Clipboard_IMG = tkinter.PhotoImage(file="Clipboard.png")
Sticky_Notes_IMG = tkinter.PhotoImage(file="Sticky_Notes.png")

def sle_click(event):
    global select_username

    if (event.x < 595) and (event.x > 555) and (event.y > 280) and (event.y < 300):
        select_username = select_username + 1
        select_existing_user()

    if (event.x < 595) and (event.x > 555) and (event.y > 350) and (event.y < 370):
        select_username = select_username + 1
        select_existing_user()

    if (event.x < 595) and (event.x > 555) and (event.y > 390) and (event.y < 410):
        global name
        global usernames
        name = usernames[select_username]
        global boot
        boot = True
        Methods_Sequence()


def select_existing_user():
    # create click binding
    Main_Canvas.bind('<Button>', sle_click)

    #Read Usernames
    users = [f.path for f in os.scandir(polyfile) if f.is_dir()]
    global usernames
    usernames = []
    for name in users:
        username = path.basename(name)
        usernames.append(username)

    heading = font.Font(family="Segoe UI Black11", size=16, weight="bold")
    heading_2 = font.Font(family="Segoe UI Black11", size=20)

    Main_Canvas.create_rectangle(325, 125, 825, 525, fill="white", outline="black", width=2)  # main window
    Main_Canvas.create_rectangle(325, 125, 825, 150, fill="grey15", outline="grey15")  # settings bar
    Main_Canvas.create_text(575, 137, text="SWTICH USER", fill="white", font=heading)

    #create arrows
    #up
    Main_Canvas.create_polygon(595, 300, 555, 300, 575, 280, 595, 300, fill="black", activefill="cyan")
    #down
    Main_Canvas.create_polygon(595, 350, 555, 350, 575, 370, 595, 350, fill="black", activefill="cyan")

    #OK BUTTON
    Main_Canvas.create_rectangle(555, 390, 595, 410, fill="grey")
    Main_Canvas.create_text(575, 400, text="OK", font=heading, activefill="cyan")

    global select_username
    all = len(usernames) - 1
    if select_username < 0:
        select_username = all
    if select_username > all:
        select_username = 0
    Main_Canvas.create_text(575, 325, text=usernames[select_username], font=heading_2)

def create_new_user():
    Main_Canvas.delete("all")

    Main_Canvas.create_image(0, 0, anchor='nw', image=Sticky_Notes_IMG)
    stop = 0
    while stop != 200:
        Main_Canvas.create_rectangle(595-stop, 300-stop, 705+stop, 375+stop, fill="lightgrey",
                                     width=2, outline="purple")
        stop = stop + 10
        Main_Canvas.update()
        time.sleep(0.01)

    heading = font.Font(family="Constantia", size=25)
    body = font.Font(family="Arial CE", size=15)

    #Main_Canvas.create_image(0, 0, anchor='nw', image=Sticky_Notes_IMG)
    #Main_Canvas.create_rectangle(400, 100, 900, 575, fill="lightgrey")

    Main_Canvas.create_text(650, 150, text="CREATE NEW USER", font=heading)
    Main_Canvas.create_line(500, 125, 800, 125)
    Main_Canvas.create_line(500, 175, 800, 175)
    Main_Canvas.create_text(575, 205, text="Username:", font=body, anchor='ne')
    Main_Canvas.create_text(575, 305, text="Date of Birth:", font=body, anchor='ne')
    Main_Canvas.create_text(575, 400, text="Gender:", font=body, anchor='ne')

    #Username Entry Box
    Main_Canvas.create_rectangle(580, 205, 820, 230, fill="white")
    global name
    name = ""

    #Date of Birth
    Main_Canvas.create_rectangle(580, 305, 605, 330, fill="lightgrey", outline="lightgrey")
    Main_Canvas.create_text(592, 315, text=dob_day, font=body, anchor='c')
    Main_Canvas.create_rectangle(620, 305, 750, 330, fill="lightgrey", outline="lightgrey")
    Main_Canvas.create_text(685, 315, text=Month_List[dob_month], font=body, anchor='c')
    Main_Canvas.create_rectangle(760, 305, 820, 330, fill="lightgrey", outline="lightgrey")
    Main_Canvas.create_text(790, 315, text=dob_year, font=body, anchor='c')

    #day arrows
    Main_Canvas.create_polygon(602, 305, 582, 305, 592, 295, 602, 305, activefill="cyan")
    Main_Canvas.create_polygon(602, 330, 582, 330, 592, 340, 602, 330, activefill="cyan")

    #month arrows
    Main_Canvas.create_polygon(695, 305, 675, 305, 685, 295, 695, 305, activefill="cyan")
    Main_Canvas.create_polygon(695, 330, 675, 330, 685, 340, 695, 330, activefill="cyan")

    #year arrows
    Main_Canvas.create_polygon(800, 305, 780, 305, 790, 295, 800, 305, activefill="cyan")
    Main_Canvas.create_polygon(800, 330, 780, 330, 790, 340, 800, 330, activefill="cyan")

    #Gender Male
    Main_Canvas.create_rectangle(580, 400, 610, 430, fill="grey", activefill="blue")
    Main_Canvas.create_text(620, 400, text="Male", font=body, anchor='nw')

    #Gender Female
    Main_Canvas.create_rectangle(690, 400, 720, 430, fill="grey", activefill="magenta")
    Main_Canvas.create_text(730, 400, text="Female", font=body, anchor='nw')

    #create button
    #Main_Canvas.create_rectangle(600, 480, 700, 520, fill="grey")
    Main_Canvas.create_polygon(610, 475, 690, 475, 705, 500, 690, 525, 610, 525, 595, 500, 610, 475,
                               fill="cyan", outline="black", smooth=1)
    Main_Canvas.create_polygon(615, 480, 685, 480, 700, 500, 685, 520, 615, 520, 600, 500, 615, 480,
                               fill="grey", outline="black", smooth=1)
    Main_Canvas.create_text(650, 500, text="SUBMIT", activefill="cyan", font=('Arial CE', 14))

def cnu_store_data():
    global dob_month
    global dob_year
    global dob_day
    global gender
    global name

    body = font.Font(family="Arial CE", size=12)
    proceed = True
    if name == "":
        Main_Canvas.create_text(822, 207, text="*Required", fill="red", font=body, anchor='nw')
        proceed = False

    if gender == None:
        Main_Canvas.create_text(822, 400, text="*Required", fill="red", font=body, anchor='nw')
        proceed = False

    if proceed == True:
        username_taken = False
        name = name.strip()
        users = [f.path for f in os.scandir(polyfile) if f.is_dir()]
        for item in users:
            user = path.basename(item)
            if name == user:
                username_taken = True
                Main_Canvas.create_text(580, 185, text="*Username Taken", fill="red", font=body, anchor='nw')
        if username_taken == False:
            os.mkdir(polyfile + "/" + name)
            user_info = open(polyfile + "/" + name + "/user_info.txt", 'w', encoding='utf8')
            user_info.write(name + "\n")
            user_info.write(str(dob_day) + "/" + str(dob_month) + "/" + str(dob_year) + "\n")
            user_info.write(gender)
            user_info.close()
            global boot
            boot = True
            Methods_Sequence()

#create_new_user switchboard click bindings
def cnu_backspace(event):
    global name
    if len(name) > 0:
        name = name.rstrip(name[-1])
        body = font.Font(family="Arial CE", size=13)
        Main_Canvas.create_rectangle(580, 185, 820, 205, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_rectangle(583, 230, 820, 270, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_rectangle(580, 205, 820, 230, fill="white", outline="blue")
        Main_Canvas.create_text(583, 210, text=name, font=body, anchor='nw')

def cnu_entry(event):
    global name
    key = event.char

    #input validation
    invalid_characters = ["<", ">", ":", "\"", "/", "\\", "|", "?", "*", "."]
    invalid = False
    for character in invalid_characters:
        if character == key:
            invalid = True

    if len(name) > 14:
        invalid = True
    if invalid == True:
        Main_Canvas.create_text(583, 230, text="*Must not contain: <>:\"/\\|?*.", fill="red", anchor='nw')
        Main_Canvas.create_text(583, 250, text="*Must be less than 15 characters", fill="red", anchor='nw')
        body = font.Font(family="Arial CE", size=13)
        Main_Canvas.create_rectangle(580, 205, 820, 230, fill="white", outline="red")
        Main_Canvas.create_text(583, 210, text=name, font=body, anchor='nw')

    #display string
    if invalid == False:
        name = name + key
        body = font.Font(family="Arial CE", size=13)
        Main_Canvas.create_rectangle(580, 185, 820, 205, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_rectangle(583, 230, 820, 270, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_rectangle(580, 205, 820, 230, fill="white", outline="blue")
        Main_Canvas.create_text(583, 210, text=name, font=body, anchor='nw')

def cnu_switchboard(event):
    global dob_month
    global dob_year
    global dob_day
    global gender

    body = font.Font(family="Arial CE", size=15)

    #date data
    month = Month_List[dob_month]
    end = 30 #referenced before assignment
    if month == "January":
        end = 31
    elif month == "February":
        leap = dob_year/4
        if leap.is_integer():
            end = 29
        else:
            end = 28
    elif month == "March":
        end = 31
    elif month == "April":
        end = 30
    elif month == "May":
        end = 31
    elif month == "June":
        end = 30
    elif month == "July":
        end = 31
    elif month == "August":
        end = 31
    elif month == "September":
        end = 30
    elif month == "October":
        end = 31
    elif month == "November":
        end = 30
    elif month == "December":
        end = 31

    if (event.x < 602) and (event.x > 582) and (event.y > 295) and (event.y < 305):
        dob_day = dob_day + 1
        if dob_day > end:
            dob_day = 1
        Main_Canvas.create_rectangle(580, 305, 605, 330, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_text(592, 315, text=dob_day, font=body, anchor='c')
    elif (event.x < 602) and (event.x > 582) and (event.y > 330) and (event.y < 340):
        dob_day = dob_day - 1
        if dob_day < 1:
            dob_day = end
        Main_Canvas.create_rectangle(580, 305, 605, 330, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_text(592, 315, text=dob_day, font=body, anchor='c')
    elif (event.x < 695) and (event.x > 675) and (event.y > 295) and (event.y < 305):
        dob_month = dob_month - 1
        if dob_month < 1:
            dob_month = 12
        Main_Canvas.create_rectangle(620, 305, 750, 330, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_text(685, 315, text=Month_List[dob_month], font=body, anchor='c')

        #calculate new end
        month = Month_List[dob_month]
        if month == "January":
            end = 31
        elif month == "February":
            leap = dob_year / 4
            if leap.is_integer():
                end = 29
            else:
                end = 28
        elif month == "March":
            end = 31
        elif month == "April":
            end = 30
        elif month == "May":
            end = 31
        elif month == "June":
            end = 30
        elif month == "July":
            end = 31
        elif month == "August":
            end = 31
        elif month == "September":
            end = 30
        elif month == "October":
            end = 31
        elif month == "November":
            end = 30
        elif month == "December":
            end = 31
        #check that day is still in proper range
        if dob_day > end:
            dob_day = end
            Main_Canvas.create_rectangle(580, 305, 605, 330, fill="lightgrey", outline="lightgrey")
            Main_Canvas.create_text(592, 315, text=dob_day, font=body, anchor='c')
    elif (event.x < 695) and (event.x > 675) and (event.y > 330) and (event.y < 340):
        dob_month = dob_month + 1
        if dob_month > 12:
            dob_month = 1
        Main_Canvas.create_rectangle(620, 305, 750, 330, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_text(685, 315, text=Month_List[dob_month], font=body, anchor='c')

        # calculate new end
        month = Month_List[dob_month]
        if month == "January":
            end = 31
        elif month == "February":
            leap = dob_year / 4
            if leap.is_integer():
                end = 29
            else:
                end = 28
        elif month == "March":
            end = 31
        elif month == "April":
            end = 30
        elif month == "May":
            end = 31
        elif month == "June":
            end = 30
        elif month == "July":
            end = 31
        elif month == "August":
            end = 31
        elif month == "September":
            end = 30
        elif month == "October":
            end = 31
        elif month == "November":
            end = 30
        elif month == "December":
            end = 31
        # check that day is still in proper range
        if dob_day > end:
            dob_day = end
            Main_Canvas.create_rectangle(580, 305, 605, 330, fill="lightgrey", outline="lightgrey")
            Main_Canvas.create_text(592, 315, text=dob_day, font=body, anchor='c')
    elif (event.x < 800) and (event.x > 780) and (event.y > 295) and (event.y < 305):
        dob_year = dob_year + 1
        if dob_year > 2020:
            dob_year = 2020
        Main_Canvas.create_rectangle(760, 305, 820, 330, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_text(790, 315, text=dob_year, font=body, anchor='c')
        month = Month_List[dob_month]
        leap = dob_year / 4
        if (month == "February") and (leap.is_integer() == False):
            if dob_day > 28:
                dob_day = 28
                Main_Canvas.create_rectangle(580, 305, 605, 330, fill="lightgrey", outline="lightgrey")
                Main_Canvas.create_text(592, 315, text=dob_day, font=body, anchor='c')
    elif (event.x < 800) and (event.x > 780) and (event.y > 330) and (event.y < 340):
        dob_year = dob_year - 1
        if dob_year < 1920:
            dob_year = 1920
        Main_Canvas.create_rectangle(760, 305, 820, 330, fill="lightgrey", outline="lightgrey")
        Main_Canvas.create_text(790, 315, text=dob_year, font=body, anchor='c')
        month = Month_List[dob_month]
        leap = dob_year / 4
        if (month == "February") and (leap.is_integer() == False):
            if dob_day > 28:
                dob_day = 28
                Main_Canvas.create_rectangle(580, 305, 605, 330, fill="lightgrey", outline="lightgrey")
                Main_Canvas.create_text(592, 315, text=dob_day, font=body, anchor='c')
    elif (event.x < 610) and (event.x > 580) and (event.y > 400) and (event.y < 430):
        gender = "Male"
        Main_Canvas.create_rectangle(690, 400, 720, 430, fill="grey", activefill="magenta")
        Main_Canvas.create_line(580, 420, 590, 430, 610, 400, width=2, fill="green")
    elif (event.x < 720) and (event.x > 690) and (event.y > 400) and (event.y < 430):
        gender = "Female"
        Main_Canvas.create_rectangle(580, 400, 610, 430, fill="grey", activefill="blue")
        Main_Canvas.create_line(690, 420, 700, 430, 720, 400, width=2, fill="green")
    elif (event.x < 820) and (event.x > 580) and (event.y > 205) and (event.y < 230):
        Main_Canvas.focus_set()
        Main_Canvas.bind('<Key>', cnu_entry)
        Main_Canvas.bind('<BackSpace>', cnu_backspace)
        if name == "":
            Main_Canvas.create_rectangle(580, 205, 820, 230, fill="white", outline="blue")
    elif (event.x < 700) and (event.x > 600) and (event.y > 480) and (event.y < 520):
        cnu_store_data()

#----------------------------------------Boot_Screen_Operations_END-------------------------------------------


#--------------------------------Method_Sequence_Control_Panel_BEGIN----------------------------------------
#check polyfile directory for users
users = [f.path for f in os.scandir(polyfile) if f.is_dir()]
global boot
if len(users) == 0:
    boot = 0
elif len(users) == 1:
    boot = "only"
elif len(users) > 1:
    boot = 2

def fetch_username():
    # Read Usernames
    global name
    users = [f.path for f in os.scandir(polyfile) if f.is_dir()]
    fetch = users[0]
    username = path.basename(fetch)
    name = username
    global boot
    boot = True
    Methods_Sequence()

def Methods_Sequence():
    global boot
    if boot == 0:
        # create click binding
        Main_Canvas.bind('<Button>', cnu_switchboard)
        create_new_user()
    elif boot == "only":
        fetch_username()
    elif boot > 1:
        select_existing_user()
    elif boot == True:
        # create click binding
        Main_Canvas.bind('<Button>', Cal_Switchboard)

        #force calendar update to system time
        update_calendar()

        #Tumble Start (this loads vine animation)
        Cal_Setup()

        #Settings Icon
        settings_icon()

        #Display Username
        username_display()



#--------------------------------Method_Sequence_Control_Panel_END------------------------------------------

#Call Methods_Sequence to start program
Methods_Sequence()

root.mainloop()