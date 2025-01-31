class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        
        #check if it is a string ('5/7') if not, keep checking if the inputs are integers
        if  isinstance(numerator,str):
            splitNumberList = numerator.strip().split('/')

            # There should only be 2 items in the list
            if len(splitNumberList) != 2:
                raise ValueError('Invalid fraction format')
            
            tempNumerator = splitNumberList[0]
            tempDenominator = splitNumberList[1]
            
            # Strip the items of the signs
            if tempNumerator.strip('-').isdigit() and tempDenominator.strip('-').isdigit():
                # still a temp variable but atleast it has been checked as a digit
                digitNumerator = int(tempNumerator)
                digitDenominator = int(tempDenominator)

                if digitDenominator == 0:
                    raise ZeroDivisionError('Denominator cannot be zero.')
                
                if isinstance(digitNumerator,int) and isinstance(digitDenominator,int):
                    self.numerator = digitNumerator
                    self.denominator = digitDenominator
            else:
                raise ValueError('Numerator and Denominator must be digits')
            
        elif not isinstance(numerator,int) or not isinstance(denominator,int):
                raise ValueError('Numerator and Denominator must be Integers.')            
        else:
            # Handles pair of integers Fraction(5,7) and rational number Fraction 10
            self.numerator = numerator
            self.denominator = denominator
                
    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_fraction(self):
        #TODO
        pass