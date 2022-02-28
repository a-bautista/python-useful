# import re
# import unittest


# roman_numeral_pattern = re.compile('''
#     ^                   # beginning of string
#     M{0,4}              # thousands - 0 to 4 Ms  
#     (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
#                         #            or 500-800 (D, followed by 0 to 3 Cs)
#     (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
#                         #        or 50-80 (L, followed by 0 to 3 Xs)
#     (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
#                         #        or 5-8 (V, followed by 0 to 3 Is)
#     $                   # end of string
#     ''', re.VERBOSE)

# class KnownValues(unittest.TestCase):
#     known_values = ( (1, 'I'),
#                       #.
#                       #.
#                       #.
#                      (3999, 'MMMCMXCIX'),
#                      (4000, 'MMMM'),                                      #①
#                      (4500, 'MMMMD'),
#                      (4888, 'MMMMDCCCLXXXVIII'),
#                      (4999, 'MMMMCMXCIX') )

# class ToRomanBadInput(unittest.TestCase):
#     def test_too_large(self):
#         '''to_roman should fail with large input'''
#         self.assertRaises(roman8.OutOfRangeError, roman8.to_roman, 5000)  #②

#     #.
#     #.
#     #.

# class FromRomanBadInput(unittest.TestCase):
#     def test_too_many_repeated_numerals(self):
#         '''from_roman should fail with too many repeated numerals'''
#         for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):     #③
#             self.assertRaises(roman8.InvalidRomanNumeralError, roman8.from_roman, s)

#     #.
#     #.
#     #.

# class RoundtripCheck(unittest.TestCase):
#     def test_roundtrip(self):
#         '''from_roman(to_roman(n))==n for all n'''
#         for integer in range(1, 5000):                                    #④
#             numeral = roman8.to_roman(integer)
#             result = roman8.from_roman(numeral)
#             self.assertEqual(integer, result)



class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

to_roman_table = [ None ]
from_roman_table = {}

def to_roman(n):
    '''convert integer to Roman numeral'''
    if not (0 < n < 5000):
        raise OutOfRangeError('number out of range (must be 1..4999)')
    if int(n) != n:
        raise NotIntegerError('non-integers can not be converted')
    return to_roman_table[n]

def from_roman(s):
    '''convert Roman numeral to integer'''
    if not isinstance(s, str):
        raise InvalidRomanNumeralError('Input must be a string')
    if not s:
        raise InvalidRomanNumeralError('Input can not be blank')
    if s not in from_roman_table:
        raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
    return from_roman_table[s]

def build_lookup_tables():
    def to_roman(n):
        result = ''
        for numeral, integer in roman_numeral_map:
            if n >= integer:
                result = numeral
                n -= integer
                break
        if n > 0:
            result += to_roman_table[n]
        return result

    for integer in range(1, 5000):
        roman_numeral = to_roman(integer)
        to_roman_table.append(roman_numeral)
        from_roman_table[roman_numeral] = integer

build_lookup_tables()

res = to_roman(8)
print(res)