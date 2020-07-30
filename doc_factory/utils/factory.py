from PIL import Image
from tesserocr import PyTessBaseAPI
from pdf2image import convert_from_path
# from pdf2image.exceptions import (
#     PDFInfoNotInstalledError,
#     PDFPageCountError,
#     PDFSyntaxError
# )
# from openpyxl import Workbook, load_workbook
# # from openpyxl.utils import get_column_letter
# from xlrd import open_workbook
# from xlutils.copy import copy
# from xlwt import XFStyle
# from time import time
import re
# from django.conf import settings

class Factory:

    def __init__(self, path_to_pdf):
        self.path = path_to_pdf
        self.text = ''
        self.paths = []
        self.title = ''
        self._convert()
        self._recognize()

    def _convert(self):
        print('Путь временного хранения пдф - ' + self.path)
        n = 1
        images = convert_from_path(self.path)
        for img in images:
            path = 'img_{}.png'.format(n)
            img.save(path, dpi=(300, 300))
            self.paths.append(path)
            n += 1

    def _recognize(self):
        with PyTessBaseAPI(lang='rus') as api:
            api.SetImageFile(self.paths[0])
            self.text += api.GetUTF8Text()
            api.SetImageFile(self.paths[1])
            self.text += api.GetUTF8Text()

    def find_title(self):
        try:
            self.title = re.findall(r'1\. Наименование объекта[\._\s]+([\w\W]+)2\. Географическое положение', self.text)[0].strip()
            self.title = re.sub(r'\n', ' ', self.title)
            tu = self.find_tu()
            if not tu:
                print('2 вариант')
                self.title = re.findall(r'ЗАДАНИЕ НА ПРОЕКТИРОВАНИЕ[\s]+([А-Я][\w\W]+)1\. Наименование', self.text)[0].strip()
                self.title = re.sub(r'\n', ' ', self.title)
            return self.title
        except IndexError:
            return ''


    def find_tu(self):
        try:
            tu = re.findall(r'[1234][\D]+38[\D]+[\d]{2}[\D]+[\d]{4}', self.title)[0]
            tu = re.sub(r'\s', '', tu)
            return tu
        except IndexError:
            return ''

    def find_length(self):
        try:
            # print(self.text)
            length = re.findall(r'(\d,\d{1,2})\s+км', self.text)[0]
            return length
        except IndexError:
            return ''

    def find_res(self):
        try:
            res = re.findall(r'[ПЗКЦ]РРЭС', self.title)[0]
            return res
        except IndexError:
            return ''

    def find_type(self):
        try:
            sip = re.findall(r'Применить провод марки СИП', self.text)[0]
            return 'ВЛ'
        except IndexError:
            return 'ТП'

    def find_adress(self):
        try:
            adress = re.findall(r'Географическое положение объекта[.]?\n([\w\W]+)3\. Заказчик', self.text)[0]
            adress = re.sub(r'г\.?\s?Краснодар[,]?', '', adress).strip()
            adress = re.sub(r'Краснодарский край[,]?', '', adress).strip()
            adress = re.sub(r'\d{6}[,]?', '', adress).strip()
            adress = re.sub(r'\n\r', ' ', adress)
            return adress
        except IndexError:
            return ''
