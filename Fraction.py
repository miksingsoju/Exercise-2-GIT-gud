class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO constructors
        if denominator == 0:
            raise ZeroDivisionError('Denominator cannot be zero.')
        

        # Pair of integers
        if len(args) == 2:
            if denominator == 0:
                print('Denominator cannot be 0')
            else:
                self.numerator = intA
                self.denominator = intB

        # Rational number
        def __init__(self, rational):
            if type(rational) != int:
                print('INVALID INPUT')
            else:
                self.numerator = rational
                self.denominator = 1

        # String
        def __init__(self,fractionString):
            #split the string into list of 2 numbers
            splitNumberList = fractionString.strip().split('/')
            self.numerator = splitNumberList[0]
            self.denominator = splitNumberList[1]

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