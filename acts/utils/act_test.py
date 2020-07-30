from act import Act
from datetime import datetime

template = 'act.xls'
numb = 55
date = datetime.today()
contract = ('П-111', '24', '10', '2019')
adress = 'ЭПУ оъекта Пушкина'
cost = '49995.40'

act = Act(template, numb, date, contract, adress, cost)

act.create_act()
