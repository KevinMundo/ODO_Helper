3 #Creating an application that calculates the ODO value needed for calibration and used to entered into the ODO.ini fie, uses 40m run START and STOP Values in Hexadecimal

import pandas as panda
import numpy as np



# Prompt the user for the hexadecimal Start value
hex_start_value = input("Enter the hexadecimal START value: ")

try:
    # Convert the hexadecimal value to decimal
    decimal_value_start = int(hex_start_value, 16)

    # Print the decimal value
    print("The decimal equivalent of", hex_start_value, "is", decimal_value_start)

except ValueError:
    # Handle the case where the input value is not a valid hexadecimal string
    print("Error: '", hex_start_value, "' is not a valid hexadecimal value. Please make sure you enter a hexadecimal value only")

# Convert the hexadecimal value to decimal
decimal_value_start = int(hex_start_value, 16)

# Prompt the user for the hexadecimal Start value
hex_stop_value = input("Enter the hexadecimal STOP value: ")

try:
    # Convert the hexadecimal value to decimal
    decimal_value_stop = int(hex_stop_value, 16)

    # Print the decimal value
    print("The decimal equivalent of", hex_stop_value, "is", decimal_value_stop)

except ValueError:
    # Handle the case where the input value is not a valid hexadecimal string
    print("Error: '", hex_stop_value, "' is not a valid hexadecimal value.Please make sure you enter a hexadecimal value only")

# Convert the hexadecimal value to decimal
decimal_value_stop = int(hex_stop_value, 16)

# Convert the input strings to numbers and calculate the sum
result = int(decimal_value_stop) - int(decimal_value_start)
print('result of Stop Value - Start Value is:', result)
result1 = 40/result
if result1 < 0:
    # If the value is negative, convert it to its absolute value
    result1 = abs(result1)

# Print the result
print("New ODO Value is:", result1)

rounded_result = round(result1, 2)

print('Circumference Ratio =', rounded_result)


