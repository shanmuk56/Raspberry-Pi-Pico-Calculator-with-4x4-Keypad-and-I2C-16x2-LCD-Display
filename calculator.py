from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)  # Adjust pin numbers based on your hardware
lcd = I2cLcd(i2c, 0x27, 2, 16)

keyName = [['1', '2', '3', '+'],
           ['4', '5', '6', '-'],
           ['7', '8', '9', '*'],
           ['c', '0', '=', '/']]
keypad_rows = [2, 3, 4, 5]
keypad_cols = [6, 7, 8, 9]

col_pins = []
row_pins = []

for x in range(0, 4):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(0)
    col_pins.append(Pin(keypad_cols[x], Pin.IN, Pin.PULL_UP))

expression = []


def clear_screen():
    expression.clear()
    lcd.clear()


def evaluate_expression():
    try:
        result = eval(''.join(expression))
        lcd.putstr(" {}".format(result))  # Print result on a new line
        utime.sleep(5)
    except:
        lcd.putstr("\nInvalid Expression")
    clear_screen()


def scan_keys():
    pressed_keys = []  # Store pressed keys for printing
    for row in range(4):
        row_pins[row].low()
        for col in range(4):
            if col_pins[col].value() == 0:
                key_press = keyName[row][col]
                pressed_keys.append(key_press)  # Store pressed key for printing
                utime.sleep(0.3)
        row_pins[row].high()

    if pressed_keys:
        lcd.putstr(" ".join(pressed_keys))  # Print pressed keys on LCD
        for key_press in pressed_keys:
            if key_press.isdigit() or key_press in ['+', '-', '*', '/']:
                expression.append(key_press)
            elif key_press == '=':
                evaluate_expression()
            elif key_press == 'c':
                clear_screen()


while True:
    scan_keys()

