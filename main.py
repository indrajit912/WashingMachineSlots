# WashingMachineSlots - A python script to create a .tex file which can generate 
# a washing machine slots table.
#
# Author: Indrajit Ghosh
#
# Date: Jan 23, 2022
#

INDRAJIT = r"\textit{Indrajit (RF-8)}"
INDRAJITS_CHOICE = 6 # Sunday

DHANASRI = r"\textit{Dhanasri (RSS-2)}"
DHANASRIS_CHOICE = 5 # Saturday



from datetime import datetime, timedelta
from wash_tex_templates import FRONT, BACK
from pathlib import Path
import os, subprocess

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
        date = dt.strftime('%b %-d, 2022')

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



def generate_slots():

    YEAR = 2023
    MONTH = int(input("Enter the month code (e.g. 1 for Jan): "))

    tex_filename = "wash_slot_" + datetime(YEAR, MONTH, 1).strftime('%b_%y') + ".tex"

    output_dir = DESKTOP / f"wash_slots_{datetime(YEAR, MONTH, 1).strftime('%b_%y')}"
    try:
        os.makedirs(output_dir)
        create_slots_tex(YEAR, MONTH, output_dir, tex_filename)
        os.chdir(output_dir)
        subprocess.run(["pdflatex", tex_filename])
        print(f"\nThe .pdf has been created inside: ```{output_dir}```\n")

    except FileExistsError:
        print(f"There is already a directory with the name ``{output_dir.name}``. Delete that directory first and try again later!")


def main():
    
    generate_slots()


if __name__ == '__main__':
    main()
