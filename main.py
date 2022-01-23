# WashingMachine - A python script to create a tex file which can generate 
# a washing machine slots table.
#
# Author: Indrajit Ghosh
#
# Date: Jan 23, 2022
#


from datetime import datetime, timedelta
from wash_tex_templates import FRONT, BACK

def iter_days(year, month):
    dt = datetime(year, month, 1)
    while dt.year == year and dt.month == month:
        yield dt
        dt += timedelta(days=1)


def get_table_text(year, month):

    s = ''

    for dt in iter_days(year, month):
        date = dt.strftime('%b %-d, 2022')
        text = date + r" & & & \\" + "\n" + r"\hline" + "\n"
        s += text

    return s


def create_slots_tex(year, month):
    with open('tests/wash_slots.tex', 'w') as f:
        f.write(FRONT)

        f.write(get_table_text(year, month))

        f.write(BACK)



def main():

    YEAR = 2022
    MONTH = int(input("Enter the month code (e.g. 1 for Jan): "))

    create_slots_tex(YEAR, MONTH)

    print(f"\nThe .tex file has been created!\n")
    


if __name__ == '__main__':
    main()