import json


def generate_report(values_path, tests_path, report_path):
    with open(values_path, 'r') as values_file:
        values_data = json.load(values_file)

    with open(tests_path, 'r') as tests_file:
        tests_data = json.load(tests_file)

    def fill_values(tests, values):
        for test in tests:
            for value in values['values']:
                if value['id'] == test['id']:
                    test['value'] = value['value']
                if 'values' in test:
                    fill_values(test['values'], values)

    fill_values(tests_data['tests'], values_data)

    with open(report_path, 'w') as report_file:
        json.dump(tests_data, report_file, indent=4)


# values_path = ''
# tests_path = ''
# report_path = ''

values_path = input('Введите путь к файлу значений(values.json): ')
tests_path = input('Введите путь к файлу тестов(tests.json): ')
report_path = input('Введите путь к файлу отчета (report.json): ')

generate_report(values_path, tests_path, report_path)
