import math

class CIS:

    def __init__(self, num_string):
        self.int_fract = num_string.split(".")
        self.__int = self.int_fract[0]
        self.__fractional = self.int_fract[1]


    def _get_postfix(self, num, order):
        if order == 1:
            if num[-1] == '0' or int(num[-1]) > 4:
                return 'рублей '
            elif num[-1] == '1':
                return 'рубль '
            else:
                return 'рубля '
        if order == 2:
            if num[-1] == '0' or int(num[-1]) > 4:
                return 'тысяч '
            elif num[-1] == '1':
                return 'тысяча '
            else:
                return 'тысячи '
        if order == 0:
            if num[-1] == '0' or int(num[-1]) > 4:
                return ' копеек'
            elif num[-1] == '1':
                return ' копейка'
            elif 1 < int(num) < 5:
                return ' копейки'
            else:
                return ' копеек'


    def get3(self, numstr, order):

        if order == 0:
            return numstr + self._get_postfix(numstr, order)

        if order == 2:
            set_dict_1["1"] = "одна "
            set_dict_1["2"] = "две "
        else:
            set_dict_1["1"] = "один "
            set_dict_1["2"] = "два "

        phrase = ''
        while len(numstr) < 3:
            numstr = '0' + numstr

        num11 = numstr[-2:]
        if 9 < int(num11) < 20:
            phrase = set_dict_1[num11]
        else:
            phrase = set_dict_2[num11[0]] + set_dict_1[num11[1]]

        num111 = set_dict_3[numstr[0]] + phrase

        return num111


    def _get_order(self, numstr):
        order = math.ceil(len(numstr) // 3)
        return order


    def _get_phrase(self, numstr, kop=False):

        phrase = ''

        ch1 = numstr[-3:]
        ch2 = numstr[-6:-3]

        if kop:
            phrase = self.get3(numstr, 0)
        else:
            phrase = self.get3(ch2, 2) + self._get_postfix(ch2[-2:], 2) + self.get3(ch1, 1) + self._get_postfix(ch1[-2:], 1)

        return phrase



    def get_full_phrase(self):
        full_phrase = self._get_phrase(self.__int) + self._get_phrase(self.__fractional, True)
        full_phrase = full_phrase.capitalize()
        return full_phrase






set_dict_1 = {
    "0": "",
    "1": "один ",
    "2": "два ",
    "3": "три ",
    "4": "четыре ",
    "5": "пять ",
    "6": "шесть ",
    "7": "семь ",
    "8": "восемь ",
    "9": "девять ",
    "10": "десять ",
    "11": "одиннадцать ",
    "12": "двенадцать ",
    "13":"тринадцать ",
    "14": "четырнадцать ",
    "15": "пятнаднадцать ",
    "16": "шестнадцать ",
    "17": "семнадцать ",
    "18": "восемнадцать ",
    "19": "девятнадцать "
}

set_dict_2 = {
    "0": "",
    "2": "двадцать ",
    "3": "тридцать ",
    "4": "сорок ",
    "5": "пятьдесят ",
    "6": "шестьдесят ",
    "7": "семьдесят ",
    "8": "восемьдесят ",
    "9": "девяносто "
}

set_dict_3 = {
    "0": "",
    "1": "сто ",
    "2": "двести ",
    "3": "триста ",
    "4": "четыреста ",
    "5": "пятьсот ",
    "6": "шестьсот ",
    "7": "семьсот ",
    "8": "восемьсот ",
    "9": "девятьсот "
}
