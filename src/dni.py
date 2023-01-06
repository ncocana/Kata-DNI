from src.assignmentTable import *

class Dni:

    def __init__(self, string = ""):
        self.dni  = string
        self.numberValid = False
        self.letterValid = False
        self.table = AssignmentTable()
    

    # CHECK NUMBER PART

    # Changes its boolean value.
    def setNumberValid (self, booleanValue):

        self.numberValid = booleanValue
    
    # Checks if the the length is equal to "9".
    def checkLength(self):

        return len(self.dni) == 9

    # Checks if the first eight characters of the string are digits.
    def checkNumber(self):

        return self.dni[:-1].isdigit()

    # Returns its boolean value,
    # which can be "False" or "True".
    def getNumberValid(self):

        return self.numberValid

    def checkNumbersDni(self):
        
        # If the length is equal to "9",
        # and the first eight characters of the string are digits,
        # set the boolean value of "getNumberValid" to True.
        self.setNumberValid(self.checkLength() and self.checkNumber())

        # Returns the value of "getNumberValid".
        # Whether it be "False" or "True".
        return self.getNumberValid()
    


    # CHECK LETTER PART
    
    # Changes its boolean value.
    def setLetterValid (self, booleanValue):

        self.letterValid = booleanValue
    
    # Gets the last character of the string,
    # which should be the letter.
    def getLetterDni(self):

        return self.dni[-1]

    # Gets the first eight characters of the string,
    # which should be integers.
    def getNumbersDni(self):

        if self.getNumberValid():
            return self.dni[:-1]

        return False

    # If "getNumberValid()" is True,
    # return the correct letter calculated based on the assigment table.
    # Else, return "False".
    def getLetterTable(self):

        if self.getNumberValid():
            return self.table.calculateLetter(self.getNumbersDni())

        return False

    # If "getNumberValid()" is True,
    # return "True" if the letters compared are the same.
    # Else, return "False".
    def checkLetterValid(self):

        if self.getNumberValid():
            return self.getLetterDni() == self.getLetterTable()
        
        return False

    # Returns its boolean value,
    # which can be "False" or "True".
    def getLetterValid(self):

        return self.letterValid

    # If "getNumberValid()" is True,
    # checks if the following conditions are True:
    #   1. The letter is uppercase.
    #   2. The last character of the string is a letter.
    #   3. The letter asigned is a valid one.
    # If it is, the value of the variable "letterValid" change to "True".
    # If not, the value will remain as "False".
    # Finally, returns the value of "letterValid".
    def checkLetterDni(self):

        if self.getNumberValid():
            self.setLetterValid(self.getLetterDni().isupper() and self.getLetterDni().isalpha() and self.checkLetterValid())
        
        return self.getLetterValid()
    


    # CHECK IF THE FULL DNI IS VALID

    def checkDniValid(self):

        # Call the functions to check if the numbers
        # and the letter of the DNI are valid.
        # If so, changes the values of "getNumberValid()"
        # and "getLetterValid()" to True.
        self.checkNumbersDni()
        self.checkLetterDni()

        # If both "getNumberValid()" and "getLetterValid()"
        # return the boolean value "True",
        # return "True".
        if self.getNumberValid() and self.getLetterValid():
            return True
        
        # Else, return "False".
        return False
