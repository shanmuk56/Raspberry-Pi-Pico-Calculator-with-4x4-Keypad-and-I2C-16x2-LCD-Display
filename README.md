# Raspberry-Pi-Pico-Calculator-with-4x4-Keypad-and-I2C-16x2-LCD-Display
This repository contains the code for a basic calculator implemented using a Raspberry Pi Pico microcontroller, a 4x4 Keypad Module, and an I2C 16x2 LCD Display.. The calculator allows users to perform addition, subtraction, multiplication,division,floor division and square operations by pressing the A, B, C, and D keys on the keypad. The result is then displayed on the LCD.


**Project Components:**
Raspberry Pi Pico: The microcontroller used as the main processing unit.
16x2 I2C LCD Display: Displays the calculator input and output.
4x4 Keypad Module: Allows users to input numbers and operations.

**Project Structure:**
The project consists of three Python files:
pico_i2c_lcd.py: Implements the communication with the I2C LCD display and defines the I2cLcd class.
lcd_api.py: Provides an API for talking to HD44780 compatible character LCDs. It includes the LcdApi class.
calculator.py: The main code for the calculator. It initializes the components, handles user input from the keypad, and performs basic arithmetic operations.

**Getting Started:**
Connect the Raspberry Pi Pico to the 4x4 Keypad and the 16x2 I2C LCD Display using jumper wires as per your hardware configuration.
Upload and run pico_i2c_lcd.py and lcd_api.py to initialize and configure the LCD display.
Upload and run calculator.py to start the calculator. The LCD display will show the calculator interface.

**How to Use:**
Press the numeric keys (1-9) and the arithmetic operation keys (+, -, *, /) on the keypad to input the expression.
Press '=' to evaluate the expression and see the result on the LCD display.
Press 'c' to clear the screen and start a new calculation.

**Project Notes:**
The project includes error handling for invalid expressions, displaying an error message on the LCD.
Ensure you have the required components: Raspberry Pi Pico, 16x2 I2C LCD Display, 4x4 Keypad Module, jumper wires, and a breadboard.
Connect the components following your hardware configuration.

**IEEE Documentation:**
The IEEE document related to this project can be found in the repository. It provides detailed information about the design, implementation, and functionality of the calculator project.

Contributors:
Surya Shanmuk PHD,
Nithish Reddy C,
Yegnessh Sayi Reddy M
