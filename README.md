# best-practices
The get_column_stats.py script takes a tab delimited file and calculates both the mean and the stdev for a specified column.
Added argparse to handle inputs:
use '--file_name' to specify which file to input
use '--column_number' to specify which column number you'd like to calculate
Defined mean and stdev as modules.
Added a main function structure.
Added a function to catch if a file was input that didn't exist.

Updated the basic_test.sh file to test for the presence of a file.

Fixed the style.py file to adhere to Pep8 standards.