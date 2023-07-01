# WashingMachineSlots - A python script to create a .tex file which can generate 
# a washing machine slots table.
#
# Author: Indrajit Ghosh
# Created On: Jan 23, 2022
# Modified On: Dec 19, 2022; Mar 02, 2023
#

##################### Define your choice ##############################
# 0 : Mon, 1 : Tue, 2 : Wed, 3 : Thu, 4 : Fri, 5 : Sat, 6 : Sun
INDRAJIT = (6, 1, "Indrajit (RF-8)") # (Sunday, 1st-slot, entry-text)
SNEHA = (6, 2, "Sneha (RF-7)")

############## Add your choice to the following list ##################

CHOICES = [INDRAJIT]

#######################################################################


from washing_machine import WashingMachine
from datetime import datetime
import sys, os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    ...........................................................................
    ...........................................................................

    """

    # Check if month is given or not. If not print USAGE
    if m is None:
        print(USAGE)
        sys.exit()
    else:
        y = datetime.now().year if y is None else y
        
        clear_screen()
        print(USAGE)

        machine = WashingMachine()
        for c in CHOICES:
            machine.book_recurring_slot(month=m, year=y, choice=c)
        
        machine.generate_pdf(
            year=y,
            month=m
        )


if __name__ == '__main__':
    main()