import cis_2


test_set = [
    '41973.78',
    '54291.55',
    '49840.03',
    '85048.12',
    '75993.91',
    '50000.00'
]

def main():
    for elem in test_set:
        num_str = cis_2.CIS(elem)
        print(num_str.get_full_phrase())

if __name__ == '__main__':
    main()
