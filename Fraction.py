class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        self.numerator = 0
        self.denominator = 1

        if denominator == 0:
            raise ZeroDivisionError
        
        #check if it is a string ('5/7') if not, keep checking if the inputs are integers
        elif  isinstance(numerator, str):
            splitNumberList = numerator.strip().split('/')

            # There should only be 2 items in the list
            if len(splitNumberList) != 2:
                print('Invalid input')
            else:
                tempNumerator = splitNumberList[0]
                tempDenominator = splitNumberList[1]
            
                # Strip the items of the signs
                if tempNumerator.strip('-').isdigit() and tempDenominator.strip('-').isdigit():
                    # still a temp variable but atleast it has been checked as a digit
                    digitNumerator = int(tempNumerator)
                    digitDenominator = int(tempDenominator)

                    if digitDenominator == 0:
                        raise ZeroDivisionError
                    
                    if isinstance(digitNumerator,int) and isinstance(digitDenominator,int):
                        if Fraction.check_negative(digitDenominator):
                            digitNumerator = digitNumerator * -1
                            digitDenominator = digitDenominator * -1

                        lowestTermNumerator = int(digitNumerator / Fraction.gcd(digitNumerator, digitDenominator))
                        lowestTermDenominator = int(digitDenominator / Fraction.gcd(digitNumerator, digitDenominator))

                        self.numerator = lowestTermNumerator
                        self.denominator = lowestTermDenominator
            
        elif not isinstance(numerator,int) or not isinstance(denominator,int):
                print('Invalid input')
        else:
            # Handles pair of integers Fraction(5,7) and rational number Fraction 10
            if Fraction.check_negative(denominator):
                numerator = numerator * -1
                denominator = denominator * -1

            lowestTermNumerator = int(numerator / Fraction.gcd(numerator, denominator))
            lowestTermDenominator = int(denominator / Fraction.gcd(numerator, denominator))

            self.numerator = lowestTermNumerator
            self.denominator = lowestTermDenominator

    def check_negative(number):
        if number < 0:
            return True
        else:
            return False

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
    
        self.gcd_final = self.gcd(self.numerator,self.denominator)
        if self.gcd_final == 0:
            self.gcd_final = 1

        self.numerator = self.numerator // self.gcd_final
        self.denominator = self.denominator // self.gcd_final

        if self.numerator == 0:
            return str(0)
        
        if '-' in str(self.numerator) and '-' in str(self.denominator):
            return str(self.numerator).strip('-') + '/' + str(self.denominator).strip('-')
        elif '-' in str(self.numerator) or '-' in str(self.denominator):
            return '-'+ str(self.numerator).strip('-') + '/' + str(self.denominator).strip('-')
        return str(self.numerator) + '/' + str(self.denominator)