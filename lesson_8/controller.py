from module import *
from view import *


def button_click():
    employees = read_csv()
    set_menu = show_menu()
    if set_menu == 1:
        for row in find_employees_by_last_name(employees):
            print(*row.values())

    elif set_menu == 2:
        for row in find_employees_by_position(employees):
            print(*row.values())

    elif set_menu == 3:
        for row in find_employees_by_salary_range(employees):
            print(*row.values())

    elif set_menu == 4:
        add_employee(get_employee())

    elif set_menu == 5:
        delete_employee(employees, get_employee_for_del())

    elif set_menu == 6:
        correction_employee(employees, get_id_employee())

    elif set_menu == 7:
        write_json(employees)

    elif set_menu == 8:
        write_csv(employees)

    elif set_menu == 9:
        exit(0)
