# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Jonathan Ou, 5/30/20, Modified code to product class
# Jonathan Ou, 5/31/21, added code to IO class
# Jonathan Ou, 5/31/21, added code to Main Script Body
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
objFile = None   # An object that represents a file
strStatus = ""


class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    """

    def __init__(self, product_name, product_price):
        self.__product_name = ''
        self.__product_price = ''
        self.product_name = product_name
        self.product_price = product_price

    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, name):
        if not name.isnumeric():
            self.__product_name = name
        else:
            raise Exception("Names can't be numbers")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        try:
            self.__product_price = float(value)  # cast to float
        except ValueError:
            raise Exception("Prices must be numbers")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)
    """
    pass

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                prod = line.split(",")
                row = Product(prod[0],prod[1])
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """ performs input/output tasks

    methods:
        print_menu_tasks()

        input_menu_choice()

        print_current_product_data()

        input_product_data()

        input_yes_no_choice()

        input_press_to_continue()

        """
    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Products     
        2) Add New Product Details
        3) Save Data to File
        4) Exit Program
        ''')
        print()

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = input("Which option would you like to perform? [1 to 4] - ").strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_product_data(lstOfProductObjects):
        print("******* The current Product details are: *******")
        for row in lstOfProductObjects:
            print(str(row.product_name)
                  + ","
                  + str(row.product_price))
        print("*******************************************")

    # TODO: Add code to get product data from user
    @staticmethod
    def input_product_data():
        name = str(input("What is your new product? - ").strip())
        price = float(input("What is your product price - ").strip())
        prod = Product(product_name=name, product_price=price)
        print()
        return prod

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program


# Step 1 - When the program starts, Load data from products.txt.
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # read file data

while (True):
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # show current products
        IO.print_current_product_data(lstOfProductObjects)  # Show current data in the list/table
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # add new product details
        lstOfProductObjects.append(IO.input_product_data())
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #
