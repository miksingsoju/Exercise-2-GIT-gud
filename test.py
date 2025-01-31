from Fraction import Fraction

integerConstructor = Fraction(2, 4)
rationalConstructor = Fraction(25)
stringConstructor = Fraction('-5/-7')

print(integerConstructor.get_numerator())
print(integerConstructor.get_denominator())
print(integerConstructor.get_fraction())
print()
print(rationalConstructor.get_numerator())
print(rationalConstructor.get_denominator())
print(rationalConstructor.get_fraction())
print()
print(stringConstructor.get_numerator())
print(stringConstructor.get_denominator())
print(stringConstructor.get_fraction())