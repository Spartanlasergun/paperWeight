import tkinter
from datetime import datetime

root = tkinter.Tk()
root.geometry('1150x650')
root.title('Paperweight')
root.resizable(0, 0)

Main_Canvas = tkinter.Canvas(root, width=1150, height=650, background='ghostwhite')
Main_Canvas.place(x=-1, y=-1)

#load images
Calendar_IMG = tkinter.PhotoImage(file="Calendar.png")

#For Global Use
Month_List = ["null", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
Month_Abbrev = ["null","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
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

def Calendar_Base():
    #Clear Canvas to initialize
    Main_Canvas.delete("all")

    #display background image
    Main_Canvas.create_image(0, 0, anchor='nw', image=Calendar_IMG)

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
                                         (left_boundary+column_width), (upper_boundary + row_width))

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
    while day != 7:
        x = (((int(cal_boxes[day][2])) - (int(cal_boxes[day][0]))) / 2) + inc + left_boundary
        y = (((int(cal_boxes[day][3])) - (int(cal_boxes[day][1]))) / 2) + upper_boundary
        inc = inc + column_width
        if day == 0:
            Main_Canvas.create_text(x, y, text="S", anchor="center")
        elif day == 1:
            Main_Canvas.create_text(x, y, text="M", anchor="center")
        elif day == 2:
            Main_Canvas.create_text(x, y, text="T", anchor="center")
        elif day == 3:
            Main_Canvas.create_text(x, y, text="W", anchor="center")
        elif day == 4:
            Main_Canvas.create_text(x, y, text="T", anchor="center")
        elif day == 5:
            Main_Canvas.create_text(x, y, text="F", anchor="center")
        elif day == 6:
            Main_Canvas.create_text(x, y, text="S", anchor="center")
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
    Main_Canvas.create_text(150, 75, text=Cal_Title)

    while start != end:
        x = (cal_boxes[start][2]) - (column_width / 2)
        y = (cal_boxes[start][3]) - (row_width / 2)

        # click highlight
        if (Click_Highlight != None) and (Date == Click_Highlight) and (Click_Attrib == "grid"):
            Main_Canvas.create_rectangle((x - 20), (y - 7), (20 + x), (7 + y), fill="lime")

        if (Date == Date_Highlight) and (Current_Year == Year_Highlight) and (Current_Month == Month_Highlight):
            Main_Canvas.create_rectangle((x-15), (y-8), (15+x), (8+y), fill="orange")
            Main_Canvas.create_text(x, y, text=str(Date), fill="white", activefill="cyan")
        else:
            Main_Canvas.create_text(x, y, text=str(Date), fill="black", activefill="cyan")

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

#force calendar update to system time
update_calendar()

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

#main control for click bindings
def Switchboard(event):
    #retrieve calendar grid boxes
    global cal_boxes

    #calendar arrow bindings
    if (event.x < 105) and (event.x > 85) and (event.y > 65) and (event.y < 85):
        Cal_Backward()
    elif (event.x < 215) and (event.x > 195) and (event.y > 65) and (event.y < 85):
        Cal_Forward()

    #calendar grid boxes bindings
    global cal_index
    index_check = 0
    for coords in cal_boxes:
        if (event.x < coords[2]) and (event.x > coords[0]) and (event.y > coords[1]) and (event.y < coords[3]):
            cal_index = index_check
            Calendar_Grid_Click()
        index_check = index_check + 1


#create click binding
Main_Canvas.bind('<Button>', Switchboard)

#Tumble Start
Cal_Setup()

root.mainloop()