# Washing Machine Slots Generator

This Python project provides a convenient way to manage and generate washing machine slots for a specified month and year. The project consists of a `WashingMachine` class and a `main.py` script that utilizes the class to create a PDF representation of the washing machine slots.

**Author**: [Indrajit Ghosh](https://github.com/indrajit912)

**Project URL**: [WashingMachineSlots](https://github.com/indrajit912/WashingMachineSlots)

## `WashingMachine` Class

### Description

The `WashingMachine` class represents a washing machine with the ability to manage slots and generate a PDF schedule.

### Class Structure

The class has the following attributes and methods:

#### Attributes

- `name` (str): The name of the washing machine.
- `timings` (dict): A dictionary of predefined slot timings.
- `slots` (dict): A dictionary storing the booked slots.

#### Methods

- `book_slot`: Book a specific slot for a given day, month, and year.
- `book_recurring_slot`: Book a preferred slot in a recurring manner.
- `vacant_slot`: Mark a specific slot as vacant.
- `generate_pdf`: Generate a PDF representation of the washing machine slots for a specified month and year.
- Other utility methods for managing slots and data.

### Usage

To use the `WashingMachine` class, you can import it into your script and create an instance of the class. You can then use its methods to manage and generate washing machine slots. Example usage can be found in the provided `main.py` script.

## `main.py` Script

### Description

The `main.py` script provides a command-line interface for generating washing machine slots and creating a PDF schedule.

### Usage

You can run the `main.py` script from the command line with the following options:

- `python3 main.py`: Generates washing machine slots for a specific month (user input) of the current year.
- `python3 main.py <month>`: Generates washing machine slots for the specified month of the current year.
- `python3 main.py -m <month> -y <year>`: Generates washing machine slots for the specified month and year.

Before running the script, you can customize your preferred slots by modifying the `CHOICES` list in the script.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install any necessary dependencies.
4. Run the `main.py` script according to the usage instructions.

## Dependencies

- Python 3.x
- LaTeX (pdflatex). For detailed instructions on installing LaTeX, you can refer to the [LaTeX Installation Guide](https://github.com/indrajit912/HowTo/blob/cec45debd154246d029396e9f151d9407f7e5567/guides/install_latex.md) created by [Indrajit Ghosh](https://github.com/indrajit912).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Author

- [Indrajit Ghosh](https://github.com/indrajit912)
