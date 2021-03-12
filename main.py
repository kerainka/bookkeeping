from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary


def main():
    print("{:%d/%m/%Y %H:%M}".format(datetime.now()))


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    main()
