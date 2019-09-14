import sys
import math
import argparse

parser = argparse.ArgumentParser(
           description='Parsing operator.')

parser.add_argument('--file_name',
                    type=str,
                    help='Name of file',
                    required=True)

parser.add_argument('--column_number',
                    type=int,
                    help='The number of the column',
                    required=True)

args = parser.parse_args()


file_name = args.file_name
col_num = args.column_number


def file_check(file_name):
    f = None
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('No input file.')
        sys.ext(1)
    except PermissionError:
        print('Could not open file.')
        sys.exit(1)
    finally:
        return f


def mean(V):
    m = sum(V)/len(V)

    return m


def stdev(V):

    sd = math.sqrt(sum([(x-mean(V))**2 for x in V]) / len(V))

    return sd


def main():
    if file_check(file_name) is None:
        sys.exit(1)
    else:
        V = []

        for l in file_check(file_name):
            A = [int(x) for x in l.split()]
            V.append(A[col_num])

        print('mean:', mean(V))
        print('stdev:', stdev(V))


if __name__ == '__main__':
    main()
