import scrollphat
import fourletterphat
import json
from datetime import datetime
from time import sleep

def date_bin(currdate, currfulldate):
    # TODO : Parse json for data
    firstLetter = ''
    secondLetter = ''
    match = False

    try:
        data = openJSON()
    except:
        break

    for i in data:
...     if i['bin'] == 'Grey Bin (General waste)':
            if i['date'] == currfulldate:
                firstLetter = 'G'
                match = True
...             # print(i['bin'], '==', i['day'], '==', i['date'])
    for i in data:
...     if i['bin'] == '240Ltr Green Bin (Recycling)':
            if i['date'] == currfulldate:
                secondLetter = 'G'
                match = True

    for i in data:
...     if i['bin'] == '240Ltr Brown Bin (Garden waste)':
            if i['date'] == currfulldate:
                secondLetter = 'B'
                match = True
    
    binletters = f"{firstLetter}{secondLetter}"
    fourletterphat.print_str(f"{currdate}{binletters}")
    if match:
        fourletterphat.show()
        binday = True
    else:
        binday = False

def weekday(currday):
    scrollphat.write_string(f"{currday}", 0)
    
def clearHats():
    scrollphat.clear()
    fourletterphat.clear()

def dimHats():
    fourletterphat.set_brightness(0)
    scrollphat.set_brightness(1)

def brightenHats():
    fourletterphat.set_brightness(15)
    scrollphat.set_brightness(15)

def openJSON():
    with open("../binDates.json", "r") as read_file:
        data = json.load(read_file)
    return data


prevday = datetime.today().weekday()
delta_hour = 0
binday = false


weekdays = {
        0:"Mo",
        1:"Tue",
        2:"We",
        3:"Thu",
        4:"Fri",
        5:"Sat",
        6:"Sun"
        }

while True:
    now_hour = datetime.datetime.now().hour

    if delta_hour != now_hour:

        currday = datetime.today().weekday()
        currdate = datetime.today().date()
        currfulldate = datetime.today().strftime('%d/%m/%Y')

        if currday > prevday:
            prevday = currday
            data = openJSON()

        weekday(weekdays[currday])
        date_bin(currdate, currfulldate)

    delta_hour = now_hour

    time.sleep(60)

    if delta_hour > 0 and < 7:
        clearHats()
    if delta_hour > 7 not binday:
        dimHats()
    if delta_hour > 7 and binday and < 8:
        brightenHats()
    if delta_hour > 8 and binday:
        dimHats()

