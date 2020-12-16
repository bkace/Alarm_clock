#Importing libraries

from tkinter import *
import datetime
import time
from pydub import AudioSegment
from pydub.playback import play


def alarm(set_timer):
    while True:
        time.sleep(1)       #halts the execution until the time value is passed by the user
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set date is:{} \n".format(date))
        print("Current time: {}".format(now))
        print("Alarm time: {}".format(set_timer))
        sound = AudioSegment.from_mp3('Alarm-ringtone.mp3')
        if now == set_timer:
            print("Buzzzz !!!")
            play(sound)
            break

def actual_time():
    set_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(set_timer)

#Creating GUI using tkinter
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("500x250")
wakeup_time = Label(clock, text = "When to wake you up", fg = "blue", relief = "solid",
                    font = ("Helvetica",12,"bold")).place(x = 20, y = 30)
time_format = Label(clock, text = "Enter time in 24 hour format! : HH:MM:SS", fg="red", 
                    bg="gray20", font = "Arial").place(x = 110, y = 120)


#Variables required to set the alarm
hour = StringVar()
minute = StringVar()
second = StringVar()

#Time required to set the alarm clock:
hour_Time = Entry(clock, textvariable = hour, bg = "LightCyan2", width = 15).place(x= 200, y = 30)
min_Time = Entry(clock, textvariable = minute, bg = "LightCyan2", width = 15).place(x= 250, y = 30)
sec_Time = Entry(clock, textvariable = second, bg = "LightCyan2", width = 15).place(x= 300, y = 30)

#Time input by user
submit_button = Button(clock, text = "Set Alarm", fg = "red", bg = "light yellow", width = 10, 
                        command = actual_time).place(x =270, y = 70)
close_button = Button(clock, text = "Close", fg = "red", bg = "light yellow", width = 10, 
                        command = clock.destroy).place(x =120, y = 70)
clock.mainloop()