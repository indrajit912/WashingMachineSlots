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
        1: "07:00-10:30",
        2: "11:30-15:00",
        3: "16:00-19:30",
        4: "20:30-00:00"
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
        If there is no slots then returns None 
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
    

    def generate_main_tex(self):
        """
        This function creates
        """
        pass


class WashTeX:
    """
    A class containing various TeX constants for generating a washing machine slots.
    """
    default_table_title = r"Washing Machine {\it \large{(BOSCH)}} Slots"
    default_first_col_width = "2.3cm"
    default_col_width = "2.6cm"
    default_diagbox_width = "3.5cm"
    default_diagbox_height = "1cm"

    default_first_col_heading_1 = "Date"
    default_first_col_heading_2 = "Slot"

    wash_preamble = r"""
% Author: Indrajit Ghosh
% Title: Washing Machine Slots

\documentclass[11pt, a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=0.4in]{geometry}
\usepackage{diagbox} % For diagonal line inside table

\usepackage{hyperref}
\hypersetup{
	pdftitle={Washing Machine Slots for RS Hostel, ISIBc},
	pdfauthor={Indrajit Ghosh},
	pdfsubject={Washing Machine},
	pdfcreationdate={\today},
	pdfcreator={MikTex},
	pdfkeywords={ISI},
}


\setlength{\arrayrulewidth}{0.5mm}
\setlength{\tabcolsep}{18pt}
\renewcommand{\arraystretch}{1.5}

    """

    diagbox_sty = r"""
    %%
%% This is file `diagbox.sty',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% diagbox.dtx  (with options: `package')
%% 
%% This is a generated file.
%% 
%% Copyright (C) 2011 by Leo Liu <leoliu.pku@gmail.com>
%% --------------------------------------------------------------------------
%% This work may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%   http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2005/12/01 or later.
%% 
\NeedsTeXFormat{LaTeX2e}[1999/12/01]
\ProvidesPackage{diagbox}
    [2011/11/23 v2.0 Making table heads with diagonal lines]
\RequirePackage{keyval}
\RequirePackage{pict2e}
\RequirePackage[nomessages]{fp}
\newbox\diagbox@boxa
\newbox\diagbox@boxb
\newbox\diagbox@boxm
\newdimen\diagbox@wd
\newdimen\diagbox@ht
\newdimen\diagbox@sepl
\newdimen\diagbox@sepr
\define@key{diagbox}{width}{%
  \setlength{\diagbox@wd}{#1}}
\define@key{diagbox}{height}{%
  \setlength{\diagbox@ht}{#1}}
\define@key{diagbox}{trim}{%
  \@tfor\@reserveda:=#1\do{%
    \ifcsname diagbox@sep\@reserveda\endcsname
      \setlength{\csname diagbox@sep\@reserveda\endcsname}{\z@}%
    \else
      \PackageError{diagbox}{Unknown trim option `#1'.}{l, r, lr and rl are supported.}%
    \fi}}
\define@key{diagbox}{dir}{%
  \def\diagbox@dir{#1}%
  \unless\ifcsname diagbox@dir@#1\endcsname
    \PackageError{diagbox}{Unknown direction `#1'.}{NW, NE, SW, SE are supported.}%
    \def\diagbox@dia{NW}%
  \fi}
\let\diagbox@dir@SE\relax
\let\diagbox@dir@SW\relax
\let\diagbox@dir@NE\relax
\let\diagbox@dir@NW\relax
\def\diagbox@pict{%
  \unitlength\p@
  \begin{picture}
    (\strip@pt\dimexpr\diagbox@wd-\diagbox@sepl-\diagbox@sepr\relax,\strip@pt\diagbox@ht)
    (\strip@pt\diagbox@sepl,0)
      \@nameuse{diagbox@\diagbox@part @pict@\diagbox@dir}
  \end{picture}}
\def\diagbox@double@pict@SE{%
  \put(0,0) {\makebox(0,0)[bl]{\box\diagbox@boxa}}
  \put(\strip@pt\diagbox@wd,\strip@pt\diagbox@ht) {\makebox(0,0)[tr]{\box\diagbox@boxb}}
  \Line(0,\strip@pt\diagbox@ht)(\strip@pt\diagbox@wd,0)}
\let\diagbox@double@pict@NW\diagbox@double@pict@SE
\def\diagbox@double@pict@NE{%
  \put(0,\strip@pt\diagbox@ht) {\makebox(0,0)[tl]{\box\diagbox@boxa}}
  \put(\strip@pt\diagbox@wd,0) {\makebox(0,0)[br]{\box\diagbox@boxb}}
  \Line(0,0)(\strip@pt\diagbox@wd,\strip@pt\diagbox@ht)}
\let\diagbox@double@pict@SW\diagbox@double@pict@NE
\def\diagbox@double#1#2#3{%
  \begingroup
  \diagbox@wd=\z@
  \diagbox@ht=\z@
  \diagbox@sepl=\tabcolsep
  \diagbox@sepr=\tabcolsep
  \def\diagbox@part{double}%
  \setkeys{diagbox}{dir=NW,#1}%
  \setbox\diagbox@boxa=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#2\end{tabular}}%
  \setbox\diagbox@boxb=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#3\end{tabular}}%
  \ifdim\diagbox@wd=\z@
    \ifdim\wd\diagbox@boxa>\wd\diagbox@boxb
      \diagbox@wd=\dimexpr2\wd\diagbox@boxa+\diagbox@sepl+\diagbox@sepr\relax
    \else
      \diagbox@wd=\dimexpr2\wd\diagbox@boxb+\diagbox@sepl+\diagbox@sepr\relax
    \fi
  \fi
  \ifdim\diagbox@ht=\z@
    \diagbox@ht=\dimexpr\ht\diagbox@boxa+\dp\diagbox@boxa+\ht\diagbox@boxb+\dp\diagbox@boxb\relax
  \fi
  $\vcenter{\hbox{\diagbox@pict}}$%
  \endgroup}
\def\diagbox@triple@setbox@NW#1#2#3{%
  \setbox\diagbox@boxa=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#1\end{tabular}}%
  \setbox\diagbox@boxm=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#2\end{tabular}}%
  \setbox\diagbox@boxb=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#3\end{tabular}}}
\let\diagbox@triple@setbox@SW\diagbox@triple@setbox@NW
\def\diagbox@triple@setbox@SE#1#2#3{%
  \setbox\diagbox@boxa=\hbox{%
    \begin{tabular}{@{\hspace{\diagbox@sepl}}l@{}}#1\end{tabular}}%
  \setbox\diagbox@boxm=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#2\end{tabular}}%
  \setbox\diagbox@boxb=\hbox{%
    \begin{tabular}{@{}r@{\hspace{\diagbox@sepr}}}#3\end{tabular}}}
\let\diagbox@triple@setbox@NE\diagbox@triple@setbox@SE
\def\diagbox@triple@pict@NW{%
  \put(0,0)   {\makebox(0,0)[bl]{\box\diagbox@boxa}}
  \put(0,\y)  {\makebox(0,0)[tl]{\box\diagbox@boxm}}
  \put(\x,\y) {\makebox(0,0)[tr]{\box\diagbox@boxb}}
  \Line(0,\yym)(\x,0)
  \Line(\xm,\y)(\x,0)}
\def\diagbox@triple@pict@NE{%
  \put(0,\y)  {\makebox(0,0)[tl]{\box\diagbox@boxa}}
  \put(\x,\y) {\makebox(0,0)[tr]{\box\diagbox@boxm}}
  \put(\x,0)  {\makebox(0,0)[br]{\box\diagbox@boxb}}
  \Line(0,0)(\xxm,\y)
  \Line(0,0)(\x,\yym)}
\def\diagbox@triple@pict@SW{%
  \put(0,\y) {\makebox(0,0)[tl]{\box\diagbox@boxa}}
  \put(0,0)  {\makebox(0,0)[bl]{\box\diagbox@boxm}}
  \put(\x,0) {\makebox(0,0)[br]{\box\diagbox@boxb}}
  \Line(0,\ym)(\x,\y)
  \Line(\xm,0)(\x,\y)}
\def\diagbox@triple@pict@SE{%
  \put(0,0)   {\makebox(0,0)[bl]{\box\diagbox@boxa}}
  \put(\x,0)  {\makebox(0,0)[br]{\box\diagbox@boxm}}
  \put(\x,\y) {\makebox(0,0)[tr]{\box\diagbox@boxb}}
  \Line(0,\y)(\xxm,0)
  \Line(0,\y)(\x,\ym)}
\def\diagbox@triple#1#2#3#4{%
  \begingroup
  \diagbox@wd=\z@
  \diagbox@ht=\z@
  \diagbox@sepl=\tabcolsep
  \diagbox@sepr=\tabcolsep
  \def\diagbox@part{triple}%
  \setkeys{diagbox}{dir=NW,#1}%
  \@nameuse{diagbox@triple@setbox@\diagbox@dir}{#2}{#3}{#4}%
  \edef\xa{\strip@pt\wd\diagbox@boxa}%
  \edef\ya{\strip@pt\dimexpr\ht\diagbox@boxa+\dp\diagbox@boxa\relax}%
  \edef\xb{\strip@pt\wd\diagbox@boxb}%
  \edef\yb{\strip@pt\dimexpr\ht\diagbox@boxb+\dp\diagbox@boxb\relax}%
  \edef\xm{\strip@pt\wd\diagbox@boxm}%
  \edef\ym{\strip@pt\dimexpr\ht\diagbox@boxm+\dp\diagbox@boxm\relax}%
  \FPneg\bi\yb
  \FPadd\ci\xb\xm  \FPneg\ci\ci
  \FPmul\di\xm\yb
  \FPadd\bj\ya\ym  \FPneg\bj\bj
  \FPneg\cj\xa
  \FPmul\dj\xa\ym
  \FPsub\u\dj\di
  \FPupn{v}{bj ci * bi cj * -}%
  \FPupn{delta}{bi dj * bj di * - cj ci - * 4 * %
    v u + copy * %
    - 2 swap root}%
  \ifdim\diagbox@wd=\z@
    \FPupn{x}{2 bj bi - delta v u - + / /}%
    \diagbox@wd=\x\p@
  \else
    \edef\x{\strip@pt\diagbox@wd}%
  \fi
  \ifdim\diagbox@ht=\z@
    \FPupn{y}{2 cj ci - delta v u + - / /}%
    \diagbox@ht=\y\p@
  \else
    \edef\y{\strip@pt\diagbox@ht}%
  \fi
  \FPsub\xxm\x\xm
  \FPsub\yym\y\ym
  $\vcenter{\hbox{\diagbox@pict}}$%
  \endgroup}
\newcommand\diagbox[3][]{%
  \@ifnextchar\bgroup
    {\diagbox@triple{#1}{#2}{#3}}{\diagbox@double{#1}{#2}{#3}}}
\expandafter\xdef\csname ver@slashbox.\@pkgextension\endcsname{9999/99/99}
\def\slashbox{%
  \def\diagbox@slashbox@options{dir=SW,}%
  \slashbox@}
\def\backslashbox{%
  \def\diagbox@slashbox@options{dir=NW,}%
  \slashbox@}
\newcommand\slashbox@[1][]{%
  \ifx\relax#1\relax\else
    \edef\diagbox@slashbox@options{%
      \unexpanded\expandafter{\diagbox@slashbox@options}%
      \unexpanded{width=#1,}}%
  \fi
  \slashbox@@}
\newcommand\slashbox@@[3][]{%
  \edef\diagbox@slashbox@options{%
    \unexpanded\expandafter{\diagbox@slashbox@options}%
    \unexpanded{trim=#1,}}%
  \expandafter\diagbox\expandafter[\diagbox@slashbox@options]{#2}{#3}}
\endinput
%%
%% End of file `diagbox.sty'.
    """


def main():
    # print('class: WashingMachine')
    # machine = WashingMachine.load(DATABASE_DIR / "rs_hostel.json")
    machine = WashingMachine(name="New Machine")
    machine.add_blank_slots(month=3)
    print(machine.slots)
    print(machine.book_slot(day=2, month=3, timing=1, entry="Indrajit (RF-8)"))
    print(machine.book_slot(day=2, month=3, timing=1, entry="Sneha (RF-7)"))
    pprint(machine.slots)


    


if __name__ == '__main__':
    main()