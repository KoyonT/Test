import json


def update_values(tests, values):
    for test in tests:
        for value in values['values']:
            if test['id'] == value['id']:
                test['value'] = value['value']
        if 'values' in test:
            update_values(test, values)


path_to_test = ('F:\\Python\\Code\\Test\\task3\\tests.json')
path_to_values = ('F:\\Python\\Code\\Test\\task3\\values.json')

try:
    with open(path_to_test, 'r') as tests_file, open(path_to_values, 'r') as values_file:
        tests_data = json.load(tests_file)
        values_data = json.load(values_file)
        update_values(tests_data, values_data)

except IOError:
    print('Файл не найден!')

with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)
