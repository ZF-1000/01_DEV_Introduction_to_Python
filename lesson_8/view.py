def show_menu() -> int:
    print("\n" + "=" * 45)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")                           # +
    print("2. Сделать выборку сотрудников по должности")   # +
    print("3. Сделать выборку сотрудников по зарплате")    # +
    print("4. Добавить сотрудника")                        # +
    print("5. Удалить сотрудника")                         # +
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")       # +
    print("8. Экспортировать данные в формате csv")        # +
    print("9. Закончить работу")                           # +
    return int(input("Введите номер необходимого действия: "))


def get_salary_range():
    salary_range = input('Введите диапазон зарплат: ').split()
    return list(map(float, salary_range))


def get_position():
    return input('Введите должность: ')


def get_last_name():
    return input('Введите фамилию сотрудника: ')


def get_employee():
    return input('Введите через ",": id, last_name, first_name, position, phone_number, salary:\n').split(',')


def get_employee_for_del():
    return int(input('Введите id сотрудника для удаления: '))


def get_id_employee():
    return int(input('Введите id сотрудника для корректировки: '))