class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO constructors

        # Pair of integers
        def __init__(self, intA, intB):
            if intB == 0:
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
            splitNumberList = fractionString.split('/')
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