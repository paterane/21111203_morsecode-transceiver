def on_received_number(receivedNumber):
    global count, I, trace, index
    list_Y.append(receivedNumber)
    list_X.append(4)
    count = len(list_X)
    I = count - 1
    basic.clear_screen()
    while index <= I:
        if index == I:
            trace = 0
        if trace == 0:
            list_X[index] = list_X[index] - 1
        else:
            list_X[index] = list_X[index] - (trace + 1)
        led.plot(list_X[index], list_Y[index])
        index += 1
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global count, I, trace
    if del2:
        radio.send_string("del")
        list_X.pop()
        list_Y.pop()
        count = len(list_X)
        I = count - 1
        basic.clear_screen()
        index2 = 0
        while index2 <= I:
            list_X[index2] = list_X[index2] + 1
            led.plot(list_X[index2], list_Y[index2])
            index2 += 1
    elif list_X[0] <= -1:
        basic.clear_screen()
        index3 = 0
        while index3 <= I:
            list_X[index3] = list_X[index3] + 1
            led.plot(list_X[index3], list_Y[index3])
            index3 += 1
        trace += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global count, I
    if receivedString == "del":
        list_X.pop()
        list_Y.pop()
        count = len(list_X)
        I = count - 1
        basic.clear_screen()
        index4 = 0
        while index4 <= I:
            list_X[index4] = list_X[index4] + 1
            led.plot(list_X[index4], list_Y[index4])
            index4 += 1
radio.on_received_string(on_received_string)

def on_logo_pressed():
    global del2, list_X, list_Y, trace, del_count
    if trace == 0:
        if del_count == 0:
            del2 = True
        else:
            list_X = []
            list_Y = []
            trace = 0
            basic.clear_screen()
        if del_count < 1:
            del_count += 1
        else:
            del_count = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

space = 0
space_lock = False
release = 0
reset = False
press = 0
lock = False
index = 0
trace = 0
I = 0
count = 0
del_count = 0
del2 = False
list_X: List[number] = []
list_Y: List[number] = []
radio.set_group(1)
del2 = False
del_count = 0
count = 0
I = 0
trace = 0
list_X = []
list_Y = []

def on_forever():
    global press, lock, reset, del2, del_count, release, space_lock, count, I, trace, space
    if input.button_is_pressed(Button.B) and not (lock):
        press = control.millis()
        lock = True
        reset = False
        del2 = False
        del_count = 0
    elif not (input.button_is_pressed(Button.B)) and lock:
        release = control.millis()
        lock = False
        reset = True
        space_lock = True
        if press + 250 < release:
            list_Y.append(1)
            radio.send_number(1)
            music.play_tone(740, music.beat(BeatFraction.HALF))
        else:
            list_Y.append(2)
            radio.send_number(2)
            music.play_tone(740, music.beat(BeatFraction.SIXTEENTH))
        list_X.append(4)
        count = len(list_X)
        I = count - 1
        basic.clear_screen()
        index5 = 0
        while index5 <= I:
            if index5 == I:
                trace = 0
            if trace == 0:
                list_X[index5] = list_X[index5] - 1
            else:
                list_X[index5] = list_X[index5] - (trace + 1)
            led.plot(list_X[index5], list_Y[index5])
            index5 += 1
    if reset:
        if space_lock:
            space_lock = False
            space = control.millis()
        if space + 2000 < control.millis():
            list_Y.append(5)
            radio.send_number(5)
            list_X.append(4)
            count = len(list_X)
            I = count - 1
            basic.clear_screen()
            index6 = 0
            while index6 <= I:
                list_X[index6] = list_X[index6] - 1
                led.plot(list_X[index6], list_Y[index6])
                index6 += 1
            reset = False
    else:
        space = 0
basic.forever(on_forever)
