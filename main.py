import datetime
import requests

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(datetime.datetime.today().strftime("%d.%m.%Y"))
    calculate_salary()
    get_employees()
