import datetime

from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print(datetime.datetime.today().strftime("%d.%m.%Y"))
    calculate_salary()
    get_employees()