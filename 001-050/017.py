__author__ = 'Andrey Smirnov'
__email__ = 'mail@ansmirnov.ru'

DICT = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

DICT10 = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}


def num_to_name(num):
    if num in DICT.keys():
        return DICT[num]
    if num < 100:
        s = DICT10[num / 10]
        if num % 10 == 0:
            return s
        else:
            return s + '-' + num_to_name(num % 10)
    if num < 1000:
        s = DICT[num / 100] + ' hundred'
        if num % 100 == 0:
            return s
        else:
            return s + ' and ' + num_to_name(num % 100)

print sum([len(num_to_name(x).replace(' ', '').replace('-', '')) for x in xrange(1, 1000)]) + len('onethousand')

