#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 1
day = 15

def test_code1():
    assert main.waterState(31) == "solid"
    assert main.waterState(32) == "solid"
    assert main.waterState(33) == "liquid"
    assert main.waterState(211) == "liquid"
    assert main.waterState(212) == "gas"
    assert main.waterState(213) == "gas"

def test_code2():
    assert main.isDozen(48) == True
    assert main.isDozen(24) == True
    assert main.isDozen(28) == False

def test_code3():
    assert main.toGerman("yes") == "ja"
    assert main.toGerman("no") == "nein"

def test_code4():
    assert main.stopLight("red") == "stop"
    assert main.stopLight("yellow") == "slow"
    assert main.stopLight("green") == "go"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
