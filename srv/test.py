import scrollphat
import fourletterphat
from time import sleep

weekdays = {
        0:"Mo",
        1:"Tue",
        2:"We",
        3:"Thu",
        4:"Fri",
        5:"Sat",
        6:"Sun"
        }

for i in range(6):
    scrollphat.write_string("{}".format(weekdays[i]), 0)
    sleep(0.5)
    scrollphat.clear()
    scrollphat.write_string("***")

for i in range(1,32):
    fourletterphat.print_str("{}  ".format(i))
    fourletterphat.show()
    sleep(0.25)
    fourletterphat.print_str("{}{}".format(i,'GG'))
    fourletterphat.show()
    sleep(0.25)
    fourletterphat.print_str("{}{}".format(i,'GB'))
    fourletterphat.show()
    sleep(0.25)
    fourletterphat.print_str("{}{}".format(i,'GT'))
    fourletterphat.show()
    sleep(0.25)
    