
# Student Name = Muhammad Ishaq
# RollNo = 8
# Email = muhammadishaqpak801@gmail.com


# Python Library Maths.
import math

print()
print("Created By =:>👉  \" Muhammad Ishaq \""'\n')
print("                              *************** SCIENTIFIC CALCULATOR *************** \n")
print("\"🌷🌹Welcome to Simple Scientific Calculator🌷🌹\"")

# Select operators
print('\n'"Choice Operations:\n", '\n'"1. Addition (+)", '\n'"2. Subtraction (-)",
      '\n'"3. Multiplication (*)",'\n' "4. Division (/)", '\n'"5. Power (^)",
      "\n""6. Square Root (√)", '\n' "7. Degree (deg)",'\n'"8. Radiance (rad)",
      '\n' "9. Sine (sin)", '\n'"10. Cosine (Cos)", '\n' "11 . Tangent (tan)")


# Adding function
def add(x, y):
    """
       Add two numbers.

       Parameters:
       x (float): The first number.
       y (float): The second number.

       Returns:
       float: The sum of x and y.
       """
    return x + y


# Subtraction function
def sub(x, y):
    """
      Subtract one number from another.

      Parameters:
      x (float): The number to be subtracted from.
      y (float): The number to subtract.

      Returns:
      float: The difference of x and y.
      """
    return x - y


# Multiplication function
def multi(x, y):
    """
        Multiply two numbers.

        Parameters:
        x (float): The first number.
        y (float): The second number.

        Returns:
        float: The product of x and y.
        """
    return x * y


# Divide Function
def divide(x, y):
    """
      Divide one number by another.

      Parameters:
      x (float): The dividend.
      y (float): The divisor.

      Returns:
      float: The result of dividing x by y.
      """
    return x / y


# Power function
def power(x, y):
    """
      Raise a number to the power of another number.

      Parameters:
      x (float): The base.
      y (float): The exponent.

      Returns:
      float: The result of raising x to the power of y.
      """
    return math.pow(x, y)


# Square_root Function
def square_root(x):
    """
    Calculate the square root of a number.

    Parameters:
    x (float): The number whose square root is to be calculated.

    Returns:
    float: The square root of x.
    """

    return math.sqrt(x)


# Degree function
def degree(z):
    """
    Convert angle from radians to degrees.

    Parameters:
    z (float): Angle in radians.

    Returns:
    float: Angle converted to degrees.
    """

    return math.degrees(z)


# Radians function
def radians(z):
    """
       Convert angle from degrees to radians.

       Parameters:
       z (float): Angle in degrees.

       Returns:
       float: Angle converted to radians.
       """
    return math.radians(z)


# Sin 0~ function
def sin(x):
    """
       Calculate the sine of an angle in degrees.

       Parameters:
       x (float): Angle in degrees.

       Returns:
       float: Sine of the angle.
       """
    return math.sin(math.radians(x))


# cos 0~ function
def cos(x):
    """
      Calculate the cosine of an angle in degrees.

      Parameters:
      x (float): Angle in degrees.

      Returns:
      float: Cosine of the angle.
      """
    return math.cos(math.radians(x))


# tan 0~ function
def tan(x):
    """
       Calculate the tangent of an angle in degrees.

       Parameters:
       x (float): Angle in degrees.

       Returns:
       float: Tangent of the angle.
       """
    return math.tan(math.radians(x))


# Repeating question
while True:
    print()
    # Button for On or Off.
    Button_on_off = input("Type On or Off for using calculator :")
    if Button_on_off == "ON" or Button_on_off == "on" or Button_on_off == "On":

        try:
            choice = int(input("Enter your Operators number upto (1-11) :"))

            # If choice are this range after enter this block
            if choice in [1, 2, 3, 4, 5]:
                # user input select number.
                x = float(input("Enter your First number :"))
                y = float(input("Enter your second number :"))
                # Condition for select operation
                if choice == 1:
                    result = add(x, y)
                elif choice == 2:
                    result = sub(x, y)
                elif choice == 3:
                    result = multi(x, y)
                elif choice == 4:
                    result = divide(x, y)
                elif choice == 5:
                    result = power(x, y)
                print("Answer:>",result)

            # List for select operation.
            elif choice in [6, 7, 8, 9, 10, 11]:
                x = float(input("Enter your number :"))
                if choice == 6:
                    if x <= 0:
                        print("Error!😡: Cannot calculate square root of a negative number.")
                    result = square_root(x)
                elif choice == 7:
                    result = degree(x)
                elif choice == 8:
                    result = radians(x)
                elif choice == 9:
                    result = sin(x)
                elif choice == 10:
                    result = cos(x)
                elif choice == 11:
                    result = tan(x)
                # Finally answer
                print("Answer:>",result)
            else:
                print("Error!😡: Enter only number!.")
        # ValueError which user enter invalid input.
        except ValueError:
            print()
            print("Error!😡: Enter inputs in digits!.")
        # except square_root:

        # ZeroDivision Error handling.
        except ZeroDivisionError:
            print("Cannot divide by zero")
        # Error which user input invalid operation
        except:
            print()
            print("Error!😡: Invalid Choice Operation!.")

    # For shutdown calculator
    elif Button_on_off == "OFF" or Button_on_off == "Off" or Button_on_off == "off":
            print()
            print("🥰Thanks for using calculator.")
            print("👋👋Bye Bye.")
            break
    # For on or off Error.
    else:
        print("Error!😡: Invalid input!.")

