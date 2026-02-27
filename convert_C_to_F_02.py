# FILE NAME - convert_C_to_F_02.py

# NAME: Jared Thibado
# DATE: 02/26/2026
# BRIEF DESCRIPTION:I wrote a program that converts temperatures between Celsius and Fahrenheit.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def temp_converter():
    print("===== Temperature Converter =====\n")
    print("  1. Convert from Celsius to Fahrenheit")
    print("  2. Convert from Fahrenheit to Celsius\n")
    
    choice = input("Please choose from the above menu: ")
    
    
    if choice == '1':
        celsius = int(input("Enter a temperature to convert: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"\n{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
        
    elif choice == '2':
        fahrenheit = int(input("Enter a temperature to convert: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"\n{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")

temp_converter()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?
I learned how to better use multiple user inputs in the flow of the program.
...and that I did not know how to spell Fahrenheit.






'''