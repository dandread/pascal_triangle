# Recursively create Pascal's triangle using functions

def triangle(n: 'row', k: 'column') -> 'value':
    """Compute the individual values of the Pascal triangle.

    Keyword arguments:
    n -- the row index
    k -- the column index

    Function contains two cases; the base case, and the recursive
    case. Each recursive call adds stack frame until base case
    is reached.

    The recursive case utilizes a formula for combinations to
    find the value at any place in the triangle.
    """
    # Base Case:
    if k in (0, n):
        return 1  # top of triangle

    # Recursive Case:
    else:
        # each subsequent row is the sum of the two numbers
        # diagonally above
        return triangle(n-1, k-1) + triangle(n-1, k)


def pascal(N: 'number of rows'):
    """Inserts row and column index into 'triangle' function
    based on number of desired rows.
    """
    for i in range(N):
        for k in range(i + 1):
            # add a new line after each row
            print(triangle(i, k), end=' ')
        # group each row by line
        print()


def main():
    """Return 'pascal' when script runs.
    """
    return pascal


# enter number of rows desired to be printed and run the script
if __name__ == "__main__":
    pascal(10)
