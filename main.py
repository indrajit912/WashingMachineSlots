# WashingMachineSlots - A python script to create a .tex file which can generate 
# a washing machine slots table.
#
# Author: Indrajit Ghosh
#
# Created On: Jan 23, 2022
# Modified On: Dec 19, 2022
#

INDRAJIT = r"\textit{Indrajit (RF-8)}"
INDRAJITS_CHOICE = 6 # Sunday


from datetime import datetime, timedelta
from wash_tex_templates import FRONT, BACK
from pathlib import Path
import os, sys

HOME = Path.home()
DESKTOP = HOME / 'Desktop/'

def iter_days(year, month):
    dt = datetime(year, month, 1)
    while dt.year == year and dt.month == month:
        yield dt
        dt += timedelta(days=1)


def get_table_text(year, month):

    s = ''

    for dt in iter_days(year, month):
        date = dt.strftime(f'%b %-d, {year}')

        # Monday = 0, ..., Sunday = 6
        if dt.weekday() == INDRAJITS_CHOICE:
            # Indrajit's slot
            text = date + "&" + INDRAJIT +  r" & & \\" + "\n" + r"\hline" + "\n"

        else:
            text = date + r" & & & \\" + "\n" + r"\hline" + "\n"
            
        s += text

    return s


def create_slots_tex(year, month, dir, filename):

    with open(dir / filename, 'w') as f:
        f.write(FRONT)

        f.write(get_table_text(year, month))

        f.write(BACK)


def generate_slots(year:int, month:int):

    tex_filename = "wash_slot_" + datetime(year, month, 1).strftime('%b_%y') + ".tex"

    output_dir = DESKTOP / f"wash_slots_{datetime(year, month, 1).strftime('%b_%y')}"
    try:
        os.system('clear')

        os.makedirs(output_dir)
        print("\nTeX directory created.")

        create_slots_tex(year, month, output_dir, tex_filename)
        print("Main tex file has been written.")

        os.chdir(output_dir)
        os.system(f"pdflatex {tex_filename} > {os.devnull}")
        print(f"\nThe `pdf` has been created inside: ```{output_dir}```\n")

    except FileExistsError:
        print(f"There is already a directory with the name ``{output_dir.name}``. Delete that directory first and try again later!")


def main():

    y = None
    m = None

    if len(sys.argv) < 2:
        m = int(input("Enter the month code (e.g. 1 for Jan): "))

    elif len(sys.argv) == 2:
        m = int(sys.argv[1])

    else:
        if '-m' in sys.argv:
            m = int(sys.argv[sys.argv.index('-m') + 1])
        if '-y' in sys.argv:
            y = int(sys.argv[sys.argv.index('-y') + 1])

    # Check if month is given or not. If not print USAGE
    USAGE = f"""
    WashingMachineSlots 
    ---------------------
    Author: Indrajit Ghosh
    Created On: Jan 23, 2022
    Modified On: Dec 19, 2022

    Usages:
        python3 main.py
        python3 main.py <month>
        python3 main.py -m <month> -y <year>
    
    Examples:
        Following cmd will generate slots for August(8) for the current year
            python3 main.py 8 

        Generate slots for specific month November and year 2025
            python3 main.py -m 11 -y 2025
    """

    if m is None:
        print(USAGE)
        sys.exit()
    else:
        y = datetime.now().year if y is None else y
        generate_slots(year=y, month=m)


if __name__ == '__main__':
    main()
