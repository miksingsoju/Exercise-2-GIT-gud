class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO constructors
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        
         #check if it is a string ('5/7') if not, keep checking if the inputs are integers
        if  isinstance(numerator,str):
            splitNumberList = numerator.strip().split('/')

            tempNumerator = int(splitNumberList[0])
            tempDenominator = int(splitNumberList[1])
            
            if isinstance(tempNumerator,int) and isinstance(tempDenominator,int):
                self.numerator = tempNumerator
                self.denominator = tempDenominator
            else:
                raise ValueError('Numerator and Denominator must be digits')
            
        elif not isinstance(numerator,int) or not isinstance(denominator,int):
            raise ValueError('Numerator and Denominator must be Integers.') 
        else:
            self.numerator = numerator
            self.denominator = denominator

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass