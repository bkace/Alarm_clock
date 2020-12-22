#Alarm Clock - Python 

A simple alarm clock using the below libraries:
```
1. Tkinter
2. datetime
3. time
4. pydub
```
[Tkinter](https://docs.python.org/3/library/tkinter.html) module belongs to a standard library of GUI in Python. It helps to create a dialog box with
any information that we want to provide or get from users.

[Datetime](https://docs.python.org/3/library/datetime.html?highlight=date%20time#module-datetime) and Time modules in python helps to work with the dates and time of the current day when 
the user is operating python and to maintain it too.

Python provides a module called pydub to work with audio files.For playing sound install pydub
    - `pip3 install pydub`

**pydub** is a Python library to work with only **.wav** files. For opening and saving non-wav files like mp3 - `ffmpeg` or `libav` is needed.
In Linux:
    - `sudo apt-get install ffmpeg libavcodec-extra`