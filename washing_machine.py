# A module for WashingMachine
#
# Author: Indrajit Ghosh
#
# Created on: Dec 19, 2022
#

from datetime import datetime, timedelta
from calendar import monthrange
from pathlib import Path
import json
from pprint import pprint

DATABASE_DIR = Path(__file__).parent.resolve() / "database"

# TODO: Add method to write TeX file corresponding to slot at (month, year)


__all__ = ["WashingMachine"]


class WashingMachine:
    """
    A class representing a washing maching

    Author: Indrajit Ghosh
    Created On: Dec 19, 2022


    Attributes:
    -----------
        `name`: `str`
        `timings`: `dict`; 
                    defaults to {
                                    1: "7:00am-11:00am",
                                    2: "2:00pm-6:00pm",
                                    3: "9:00pm-1:00am"
                                }

        `slots`: `dict`
                  defaults to None

    """
    default_timings = {
        1: "7:00am-11:00am",
        2: "2:00pm-6:00pm",
        3: "9:00pm-1:00am"
    }

    def __init__(
        self, 
        name:str="RS Hostel Machine", 
        timings:dict = None,
        slots:dict=None,
        **kwargs
    ):

        self._name = name
        self._slots = {} if slots is None else slots
        self._timings = self.default_timings if timings is None else timings
    

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    @property
    def slots(self):
        return self._slots

    @slots.setter
    def slots(self, new):
        self._slots = new

    @property
    def timings(self):
        return self._timings
    
    @timings.setter
    def timings(self, new):
        self._timings = new

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name}, timings={self._timings})"


    def _get_slots(self, month:int, year:int):
        """
        Generate a new slots if no slots found in 
        """
        k = f"{month}-{year}"
        if k in self._slots.keys():
            return self._slots[k]
        else:
            return None


    @staticmethod
    def iter_days(year, month):
        """
        Returns a generators of dates in that month
        """
        dt = datetime(year, month, 1)
        while dt.year == year and dt.month == month:
            yield dt
            dt += timedelta(days=1)

    
    def add_blank_slots(self, month:int, year:int=None):
        """
        This method retunrs a blank slot
        Returns:
        --------
            `np.ndarray`
        """
        year = datetime.now().year if year is None else year
        num_of_days = monthrange(year, month)[1] # (week_day_of_first_day, number_of_days)

        key = f"{month}-{year}"
        rows, cols = num_of_days, len(self._timings)
        self._slots[key] = [[False for _ in range(cols)] for _ in range(rows)]


    def book_slot(self, day:int, month:int, timing:int, year:int=None, entry:str=None):
        """
        Book a slot on the given day-month and year
        """
        year = datetime.now().year if year is None else year
        booking_dt = datetime(day=day, month=month, year=year)

        if booking_dt < datetime.today():
            raise Exception("You cannot book slots in the past!")

        day -= 1
        key = f"{month}-{year}"


        if self._get_slots(month, year) is None:
            self.add_blank_slots(month, year)

        if self._slots[key][day][timing - 1]:
            return False
        else:
            self._slots[key][day][timing - 1] = True if entry is None else entry
            return True
    

    def vacant_slot(self, day:int, month:int, timing:int, year:int=None):
        """
        Vacants a specific slot on the given day-month and year
        """

        year = datetime.now().year if year is None else year
        day -= 1

        key = f"{month}-{year}"

        if self._get_slots(month, year) is None:
            return False # Done nothing
        else:
            self._slots[key][day][timing - 1] = False
            return True

    
    def clear_history(self):
        """
        This method removes all the slots which happened in the past.
        """
        curr_month, curr_year = datetime.now().month, datetime.now().year
        temp_dic = self._slots.copy()

        for key in self._slots.keys():
            m, y = [int(e) for e in key.split('-')]

            if y < curr_year:
                del temp_dic[key]
            elif y == curr_year and m < curr_month:
                del temp_dic[key]
            else:
                pass
        
        self._slots = temp_dic


    def serialize(self):
        slots = '' if self._slots is None else self._slots
        return {
            "name": self._name,
            "slots": slots,
            "timings": self.timings
        }

    def save(self, title:Path=None):
        """
        Saves `self.serialize()` into the file
        """
        if not DATABASE_DIR.exists():
            DATABASE_DIR.mkdir()

        filepath = DATABASE_DIR / (title + '.json')
        with open(filepath, 'w') as f:
            json_obj = json.dumps(self.serialize(), indent= 4)
            f.write(json_obj)

        return self.serialize()

    @classmethod
    def load(cls, json_path):
        """
        Loads from a json file
        """
        with open(json_path, 'r') as f:
            content = json.loads(f.read())
        
        name = content['name']
        slots = content['slots']
        slots = None if slots == '' else slots
        timings = content['timings']

        return WashingMachine(name=name, timings=timings, slots=slots)



def main():
    # print('class: WashingMachine')
    machine = WashingMachine.load(DATABASE_DIR / "rs_hostel.json")
    print(machine.slots)


    


if __name__ == '__main__':
    main()