## Divide-and-Conquer Algorithms

In computer science, divide and conquer is an algorithm design paradigm. A divide-and-conquer algorithm **recursively** breaks down a problem into two or more sub-problems of the **same** or **related type**, until these become **simple enough** to be solved directly.

Some examples of divide-and-conquer algorithms: **[Merge Sort](../01-introduction/02-merge-sort.py)**, **[Binary Search](01-binary-search.py)**

### Maximum Subarray Problem
In computer science, the maximum sum subarray problem is the task of finding a contiguous subarray with the largest sum, within a given one-dimensional array A[1...n] of numbers. Formally, the task is to find indices *i* and *j* with 1 <= i <= j <= n, such that the sum of elements of the array in this range is as large as possible. (Some formulations of the problem also allow the empty subarray to be considered; by convention, the sum of all values of the empty subarray is zero.) Each number in the input array A could be positive, negative, or zero.

For example, for the array of values [−2, 1, −3, 4, −1, 2, 1, −5, 4], the contiguous subarray with the largest sum is [4, −1, 2, 1], with sum 6.

Some properties of this problem are:

1. If the array contains all non-negative numbers, then the problem is trivial (ignorable); a maximum subarray is the entire array.
2. If the array contains all non-positive numbers, then a solution is any subarray of size 1 containing the maximal value of the array (or the empty subarray, if it is permitted).
3. Several different sub-arrays may have the same maximum sum.

This problem can be solved using several different algorithmic techniques, including brute force, divide and conquer, dynamic programming, and reduction to shortest paths. 

Maximum subarray problems arise in many fields, such as **genomic sequence analysis** and **computer vision**.

Genomic sequence analysis employs maximum subarray algorithms **to identify important biological segments of protein sequences**. These problems include conserved segments, GC-rich regions, tandem repeats, low-complexity filter, DNA binding domains, and regions of high charge.

In computer vision, maximum-subarray algorithms are used on **bitmap images** to **detect the brightest area in an image**. [Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem) Reading the whole Wikipedia page is recommended.

Divide and Conquer algorithm to solve the maximum subarray can be found [here](02-maximum-subarray.py).

### Matirx Multiplication
In this problem (like many other problems), divide-and-conquer technique is not gaining a lot performance. You can see the brute-force implementation [here], which does not defer in execution time to the recursive (divided-and-conquered) version of it [here]().

Professor Volker Strassen with lots of mathematics work could design an algorithm resulting in O(n<sup>2.8</sup>) compared to O(n<sup>3</sup>) complexity of straightforward divide-and-conquer solution. Also, he added a kind of complexity to the algorithm that it doesn't make sense at least for me personally.

