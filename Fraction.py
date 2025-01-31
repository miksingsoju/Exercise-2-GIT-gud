class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        
        #check if it is a string ('5/7') if not, keep checking if the inputs are integers
        if  isinstance(numerator,str):
            splitNumberList = numerator.strip().split('/')

            # There should only be 2 items in the list
            if len(splitNumberList) != 2:
                self.numerator = 0
                self.denominator = 1
            else:
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
            
        elif not isinstance(numerator,int) or not isinstance(denominator,int):
                self.numerator = 0
                self.denominator = 1            
        else:
            # Handles pair of integers Fraction(5,7) and rational number Fraction 10
            self.numerator = numerator
            self.denominator = denominator

    def get_sign_of_string(numberString):
        if numberString[0] == '-':
            return '-'
        else:
            return ''

    @staticmethod       
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        else:
            return Fraction.euclidean(a, b)
        
    @staticmethod
    def euclidean(a, b):
        if b == 0:
            return abs(a)
        else:
            return Fraction.euclidean(b, a % b)

    def get_numerator(self):
        return str(self.numerator)

    def get_denominator(self):
        return str(self.denominator)

    def get_fraction(self):
        lowest_numerator = self.numerator /self.gcd(self.numerator,self.denominator)
        lowest_denominator = self.denominator / self.gcd(self.denominator, self.numerator)
        self.numerator = lowest_numerator
        self.denominator = lowest_denominator
        
        return_message = self.get_sign_of_string + self.get_numerator() + '/' + self.get_denominator
