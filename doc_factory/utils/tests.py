import time
import factory
import os

paths = os.listdir('/home/srv/development/crm/pdf_for_tests')
# paths = [
#     '/home/srv/development/crm/pdf_for_tests/ТЗ 2-38-19-0931.pdf'
# ]

def show_lead_time(func):
    def wrapper():
        start = time.clock()
        result = func()
        time_int = time.clock() - start
        print(""" Функция: {}; результат: {}; время исполнения: {}""".format(func.__name__, result, time_int))
    return wrapper

# блок тестирования

def main():

    for path in paths:
        path = '/home/srv/development/crm/pdf_for_tests/' + path

        fact = factory.Factory(path)

        show_lead_time(fact._convert)()
        show_lead_time(fact._recognize)()
        show_lead_time(fact.find_title)()
        show_lead_time(fact.find_tu)()
        show_lead_time(fact.find_length)()
        show_lead_time(fact.find_res)()
        show_lead_time(fact.find_type)()
        show_lead_time(fact.find_adress)()

        print('\n' + path +'\n\n')

if __name__ == '__main__':
    main()
