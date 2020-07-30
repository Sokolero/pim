from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import XFStyle, Font
import math
from . import cis_2


class Act:

    def __init__(self, template, path, numb, date, contract, adress, cost):
        self.template = template
        self.path = path
        self.numb = numb
        self.date = date
        self.contract = contract
        self.adress = adress
        self.cost = cost
        self.cell_content_dict = {
            'Numdate': self._get_numdate,
            'Contractinfo': self._get_contractinfo,
            'Adress': self._get_adress,
            'Cost': self._get_cost,
            'CostLow': self._get_cost_low,
            'Tax': self._get_tax,
            'CostAll': self._get_cost,
            'CostString': self._get_number_by_string
        }

    def _get_adress(self):
        return 'Разработка проектно-рабочей документации по объекту: "' + self.adress + '"'

    def _get_cost(self):
        return self.cost.replace('.', ',')

    def _get_numdate(self):
        return 'Aкт №{} от {}.{}.{}'.format(self.numb, self.date.day,
            self.date.month, self.date.year)

    def _get_contractinfo(self):
        return 'по договору №{} от {}.{}.{}'.format(self.contract[0],
            self.contract[1], self.contract[2], self.contract[3])

    def _get_cost_low(self):
        n_cost = float(self.cost)
        return str(round(n_cost / 1.2, 2)).replace('.', ',')

    def _get_tax(self):
        n_tax = round(float(self.cost) - float(self._get_cost_low()), 2)
        return str(n_tax).replace('.', ',')

    def _get_str(self, name):
        return self.cell_content_dict[name]()

    def _get_number_by_string(self):
        print(cis_2.CIS(self.cost).get_full_phrase())
        return cis_2.CIS(self.cost).get_full_phrase()

    def create_act(self):
        template = open_workbook(self.template, formatting_info=1)
        new_file = copy(template)

        sheet = new_file.get_sheet(0)

        for cell in cells_conf:
            print('Coздаем ячейку {}'.format(cell['name']))
            style = XFStyle()
            font = Font()
            style.alignment.horz = cell['align_horz']
            font.name = cell['fontname']
            font.bold = cell['fontbold']
            font.height = cell['fontsize']
            style.font = font
            name = cell['name']

            sheet.write(cell['row'], cell['col'],
                self._get_str(name), style)

        new_file.save(self.path)




cells_conf = [
    {
        'name': 'Numdate',
        'row': 10,
        'col': 1,
        'fontname': 'Times New Roman',
        'fontbold': 'true',
        'fontsize': 240,
        'align_horz': 2
    },
    {
        'name': 'Contractinfo',
        'row': 12,
        'col': 1,
        'fontname': 'Times New Roman',
        'fontbold': 'true',
        'fontsize': 240,
        'align_horz': 2
    },
    {
        'name': 'Adress',
        'row': 19,
        'col': 1,
        'fontname': 'Times New Roman',
        'fontbold': 'false',
        'fontsize': 240,
        'align_horz': 1
    },
    {
        'name': 'Cost',
        'row': 19,
        'col': 4,
        'fontname': 'Times New Roman',
        'fontbold': 'false',
        'fontsize': 240,
        'align_horz': 2
    },
    {
        'name': 'CostLow',
        'row': 19,
        'col': 2,
        'fontname': 'Times New Roman',
        'fontbold': 'false',
        'fontsize': 240,
        'align_horz': 2
    },
    {
        'name': 'Tax',
        'row': 19,
        'col': 3,
        'fontname': 'Times New Roman',
        'fontbold': 'false',
        'fontsize': 240,
        'align_horz': 2
    },
    {
        'name': 'CostAll',
        'row': 20,
        'col': 4,
        'fontname': 'Times New Roman',
        'fontbold': 'true',
        'fontsize': 240,
        'align_horz': 2
    },
    {
        'name': 'CostString',
        'row': 22,
        'col': 1,
        'fontname': 'Times New Roman',
        'fontbold': 'true',
        'fontsize': 240,
        'align_horz': 1
    }
]
