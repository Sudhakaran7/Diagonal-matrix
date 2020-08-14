Given a NxN matrix, print after sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Input Description:
First line contains, N the size of matrix.
Second line contains, N elements of matrix.

Output description:
Print after sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Sample Input:
3
1 2 3 3 2 1 1 2 4

Sample Output:
[[1 1 3]
 [2 2 2]
 [1 3 4]]
 
Explanation:
The given matrix is,
1 2 3
3 2 1
1 2 4

The diagonal sort matrix is,
1 1 3
2 2 2
1 3 4

Sample Input:
3
12 3 44 25 14 78 99 34 44

Sample Output:
[[12  3 44]
 [25 14 78]
 [99 34 44]]

Sample Input:
4
2 3 8 75 66 30 93 55 227 18 39 23 77 58 553 77

Sample Output:
[[  2   3   8  75]
 [ 18  30  23  55]
 [ 58  66  39  93]
 [ 77 227 553  77]]
 
Sample Input:
2
1001 2001 3001 4001

Sample Output:
[[1001 2001]
 [3001 4001]]
 
Sample Input:
2
0 1 1 0

Sample Output:
[[0 1]
 [1 0]]
 
Sample Input:
3

Sample Output:
23 166 57 84 73 90 881 1001 22
[[  22   90   57]
 [  84   23  166]
 [ 881 1001   73]]
