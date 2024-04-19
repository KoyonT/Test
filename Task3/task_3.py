import json

def update_values(tests, values):
    for test in tests:
        for value in values['values']:
            if test['id'] == value['id']:
                test['value'] = value['value']
        if 'values' in test:
            update_values(test, values)

# Load data from files
with open('tests.json', 'r') as tests_file:
    tests_data = json.load(tests_file)

with open('values.json', 'r') as values_file:
    values_data = json.load(values_file)

update_values(tests_data, values_data)
with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)