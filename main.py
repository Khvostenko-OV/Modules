from application.people import get_employees
from application.salary import calculate_salary
import datetime
from termcolor import cprint, colored

if __name__ == '__main__':
    cprint("It's main", "red")
    cprint("Today is " + str(datetime.date.today()), attrs=['reverse'])
    print()
    while True:
        cmd = input(colored(">>> ", "green"))
        if cmd == "1":
            get_employees()
        elif cmd == "2":
            calculate_salary()
        else:
            break
