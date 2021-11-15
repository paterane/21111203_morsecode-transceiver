function DisplayCode () {
    if (list_X[I] > 4) {
        list_X.push(list_X[I] + 1)
        count = list_X.length
        I = count - 1
    } else {
        list_X.push(5)
        count = list_X.length
        I = count - 1
        scrollDisplayLeft()
    }
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        list_Y1.push(2)
        list_Y2.push(5)
        DisplayCode()
    } else if (receivedNumber == 1) {
        list_Y2.push(2)
        list_Y1.push(5)
        DisplayCode()
    } else {
        list_Y2.push(5)
        list_Y1.push(5)
        DisplayCode()
    }
})
input.onButtonPressed(Button.A, function () {
    if (list_X[0] < 0) {
        scrollDisplayRight()
    }
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(2)
    basic.showLeds(`
        . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        `)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (list_X[I] > 4) {
        scrollDisplayLeft()
    }
})
function scrollDisplayRight () {
    basic.clearScreen()
    for (let index = 0; index <= I; index++) {
        list_X[index] = list_X[index] + 1
        if (list_Y1[index] == 2) {
            led.plot(list_X[index], list_Y1[index])
        } else if (list_Y2[index] == 2) {
            led.plot(list_X[index], list_Y2[index])
            led.plot(list_X[index], list_Y2[index] - 1)
            led.plot(list_X[index], list_Y2[index] + 1)
        } else {
            led.plot(list_X[index], 5)
        }
    }
}
function scrollDisplayLeft () {
    basic.clearScreen()
    for (let index = 0; index <= I; index++) {
        list_X[index] = list_X[index] - 1
        if (list_Y1[index] == 2) {
            led.plot(list_X[index], list_Y1[index])
        } else if (list_Y2[index] == 2) {
            led.plot(list_X[index], list_Y2[index])
            led.plot(list_X[index], list_Y2[index] - 1)
            led.plot(list_X[index], list_Y2[index] + 1)
        } else {
            led.plot(list_X[index], 5)
        }
    }
}
let list_Y2: number[] = []
let list_Y1: number[] = []
let list_X: number[] = []
let I = 0
let count = 0
radio.setGroup(1)
let lock = false
count = 0
I = 0
let press = 0
let release = 0
list_X = []
list_Y1 = []
list_Y2 = []
basic.forever(function () {
    if (input.logoIsPressed() && !(lock)) {
        press = control.millis()
        lock = true
        list_X = []
        list_Y1 = []
        list_Y2 = []
    } else if (!(input.logoIsPressed()) && lock) {
        release = control.millis()
        lock = false
        if (press + 250 < release) {
            music.playTone(740, music.beat(BeatFraction.Half))
            radio.sendNumber(1)
            basic.showLeds(`
                . . . . .
                . . # . .
                . . # . .
                . . # . .
                . . . . .
                `)
            basic.clearScreen()
        } else {
            music.playTone(740, music.beat(BeatFraction.Sixteenth))
            radio.sendNumber(0)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                `)
            basic.clearScreen()
        }
    }
})
