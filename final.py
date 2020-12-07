import LinearRegEditable as lr
import healthDataEditable as hd
import homepage as hp
import tkinter as tk

global t


def getData():
    global t
    t = hp.submit()
    print(t)
    return


getData()
# def callImplement():