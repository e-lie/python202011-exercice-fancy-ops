"""A simple/boring calculator to compute fancy int operations.

Usage:
  cli_calculator.py <operation> <int_n> <int_m>
  cli_calculator.py listops

Options:
  -h --help     Show this screen.
"""
from docopt import docopt
from computation_libs.fancy_int_operations import fancy_operations

if __name__ == '__main__':
    cli_arguments = docopt(__doc__)
    
    if cli_arguments['listops']:
        for operation in fancy_operations.keys():
            print(operation)
        exit(0)
    
    try:
        int_n = int(cli_arguments["<int_n>"])
        int_m = int(cli_arguments["<int_m>"])
        operation = fancy_operations[cli_arguments["<operation>"]]["function"]
        operation_symbol = fancy_operations[cli_arguments["<operation>"]]["symbol"]
    except:
        print("Bad operation or operand (should be integers)")
        exit(1)

    result = operation(int_n, int_m)
    print("{} {} {} = {}".format(int_n, operation_symbol, int_m, result))

