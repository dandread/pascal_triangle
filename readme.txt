Name: Dominick D'Andrea
JHU ID: 75805A

Module 6 Assignment: Generating Mathematical Series
Due: 10/12/2020 at 11:59 PM EST

Summary
In this module, custom functions were used to generate a famous
mathematical number sequence, Pascal's triangle. In order to
execute this, a mathematical formula using combinations was
employed to find the value at any place in triangle.

Functions
Three functions were created to generate the triangle.

Triangle: This function computed the individual values of the
Pascal triangle by using recursion. The inputs for the function
are 'n' and 'k', which represent the row and column index,
respectively, to calculate the corresponding value.

The base case provides a value for the program to work backwards
toward. It inserts a value at the top of the pyramid, which for
Pascal's triangle, is 1.

The recursive case calculates the rest of the values. The formula
used for the recursive case utilizes combination C(n,k). This
combination is written as:

    C(n,k) = n! / k!(n-k)!
    *https://www.mathsisfun.com/pascals-triangle.html

This essentially says that the value at (n,k) is the sum of the
values diagonally above:

    row(n), col(k) = [row(n-1), col(k-1)] + [row(n-1), col(k)]
    *https://stackoverflow.com/questions/24093387/
    pascals-triangle-for-python

Pascal: Instead of entering the values n,k manually, another
function was created to automatically feed those values to the
function 'triangle'.

The input for this function is 'N', which represents the number
of rows desired in the triangle. Each row has one more column
than the row index, so a nested 'for' loop was constructed to
loop through each row and column, and feed the row and column
index of each value into the triangle function.

To print the triangle in a formatted fashion, that is, in a
triangle structure versus individual outputs, two print statements
were included. The first prints each value in the row, and the
second prints the row. The 'end' formatter was employed to
denote the end of the row.

Main: Finally, a simple function, 'main', was created to return
'pascal' when the script runs. It simply holds the line:

    return pascal

To run the script, an 'if' statement was written to run the script
when 'name' equals 'main'. In this conditional statement,
'pascal(10)' was inserted to print 10 rows of Pascal's
triangle.
