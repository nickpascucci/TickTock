# TickTock
An easy to use presentation timer written in Python and Qt.

## Installation

First, make sure that you have the PySide Qt bindings installed for your
platform. They can be downloaded for multiple operating systems from 
[here](http://qt-project.org/wiki/Category:LanguageBindings::PySide::Downloads).

Once you have those set up, clone this git repository and run ticktock.py. It's
as easy as that!

## Usage

Once you have ticktock.py running, you can enter an integer number of minutes to
count down. When you're ready to start timing, press the START button. If you
want to stop early, press the STOP button. There's no pause function at the
moment, so you'll have to manually restart at the right time if you want to
pause. When the time drops below 3 minutes, the numbers will turn yellow to
indicate that you're getting low on time; when they pass 1 minute, they'll turn
red. These numbers are hard-coded currently, but are easy to change in the
source file.

## Gratuitous Screenshot

![Screenshot!](https://github.com/nickpascucci/TickTock/raw/master/screenshot.png)
