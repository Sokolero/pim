from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import XFStyle, Font

template = open_workbook('act.xls', formatting_info=1)
new_file = copy(template)


style_1 = XFStyle()
font = Font()

# насройка объектов стиля и шрифта
style_1.alignment.horz = 2
font.name = 'Times New Roman'
font.bold = 'true'
font.height = 240
style_1.font = font

sheet = new_file.get_sheet(0)

sheet.write(10, 1, 'Акт №10 от 10 июля 2020 г.', style_1)

new_file.save('new_act.xls')
