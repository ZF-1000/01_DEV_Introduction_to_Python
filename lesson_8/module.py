import csv
import json
from pathlib import Path
from view import *


def read_csv() -> list:
    employee = []
    with open(Path.cwd() / 'database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin)
        for row in csv_reader:
            temp = {}
            temp["id"] = int(row[0])
            temp["last_name"] = row[1]
            temp["first_name"] = row[2]
            temp["position"] = row[3]
            temp["phone_number"] = row[4]
            temp["salary"] = float(row[5])
            employee.append(temp)
    return employee


def read_json() -> list:
    employee = []
    with open(Path.cwd() / 'database02.json', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            employee.append(temp)
    return employee


def write_csv(employees: list):
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8', newline='') as fout:
        csv_writer = csv.writer(fout)
        for employee in employees:
            csv_writer.writerow(employee.values())


def write_json(employees: list):
    with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
        for employee in employees:
            fout.write(json.dumps(employee) + '\n')


def find_employees_by_salary_range(employees: list) -> list:
    result = []
    lo, hi = get_salary_range()
    for employee in employees:
        if lo <= employee["salary"] <= hi:
            result.append(employee)
    return result


def find_employees_by_position(employees: list) -> list:
    result = []
    position = get_position()
    for employee in employees:
        if employee['position'] == position:
            result.append(employee)
    return result


def find_employees_by_last_name(employees: list) -> list:
    result = []
    last_name = get_last_name()
    for employee in employees:
        if employee['last_name'] == last_name:
            result.append(employee)
    return result


def add_employee(empl: list) -> None:
    temp = {}
    temp["id"] = int(empl[0])
    temp["last_name"] = empl[1]
    temp["first_name"] = empl[2]
    temp["position"] = empl[3]
    temp["phone_number"] = empl[4]
    temp["salary"] = float(empl[5])
    with open(Path.cwd() / 'database.csv', 'a', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(temp.values())


def delete_employee(employees: list, id: int) -> None:
    for employee in employees:
        if employee['id'] == id:
            employees.remove(employee)
    with open(Path.cwd() / 'database.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for employee in employees:
            writer.writerow(employee.values())


def correction_employee(employees: list, id: int) -> None:
    delete_employee(employees, id)
    add_employee(get_employee())