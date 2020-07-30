class CIS:

    def __init__(self, num_string):
        self.int_fract = num_string.split(".")
        self.int_part = self.int_fract[0]
        self.fract_part = self.int_fract[1]


    def _get_postfix(self, num, order):
        if order == 1:
            if num == '0' or int(num) > 4:
                return 'рублей '
            elif num == '1':
                return 'рубль '
            else:
                return 'рубля '
        if order == 2:
            if num == '0' or int(num) > 4:
                return 'тысяч '
            elif num == '1':
                return 'тысяча '
            else:
                return 'тысячи '
        if order == 0:
            if num == '0' or int(num) > 4:
                return 'копеек '
            elif num == '1':
                return 'копейка '
            elif 1 < int(num) < 5:
                return 'копейки'
            else:
                return 'копеек '


    def _get_phrase(self, num_string, kop=False):

        if kop:
            order = 0
        else:
            order = 1

        if order == 1:
            set_dict_1["1"] = "один "
            set_dict_1["2"] = "два "
        else:
            set_dict_1["1"] = "одна "
            set_dict_1["2"] = "две "

        phrase = ''
        int_len = len(num_string)
        index = 1

        for i in range(int_len):
            print(i)
            num = num_string[- (i + 1)]

            if i % 3 == 0:
                phrase = self._get_postfix(num, order) + phrase
                if (i + 1) != int_len:
                    if num_string[-(i+2)] == "1":
                        phrase = set_dict_1[num_string[-(i+2)]] + phrase
                        i += 1
                        print('index became {}'.format(i))
                    else:
                        phrase = set_dict_1[num] + phrase
            elif index == 2 and num != "1":
                phrase = set_dict_2[num] + phrase
            elif index == 3:
                phrase == set_dict_3[num] + phrase
            else:
                break

            if (i + 1) % 3 == 0:
                order += 1
                index = 1
            else:
                index += 1

            if order == 1:
                set_dict_1["1"] = "один "
                set_dict_1["2"] = "два "
            else:
                set_dict_1["1"] = "одна "
                set_dict_1["2"] = "две "

        return phrase


    def get_full_phrase(self):
        full_phrase = self._get_phrase(self.int_part) + self._get_phrase(self.fract_part, True)
        return full_phrase






set_dict_1 = {
    "0": " ",
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
