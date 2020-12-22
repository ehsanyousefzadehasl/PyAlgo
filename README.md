# Algorithms in Python
### What is an algorithm?
An algorithm is a procedure that consists of a finite set of instructions which, given input from some set of possible inputs, enables to obtain an output.
>Donald Knuth: “**Computer Science is the Study of Algorithms.**”

#### Starting Example: Insertion Sort
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Note: Finding the right place of the picked element is another algorithm, we have to find its place by comparing and shifting till finding its correct place. I noted it here because I remember while for the first time I learned about algorithms, especially sorting one, always I was thinking so high level and because of that, I was thinking I don’t have a mind to understand or even design algorithms.
I took the following image of how the insertion algorithm works from Wikipedia. Also, there are many other websites like [visualgo](https://visualgo.net/en) that visualizes these algorithms and also Data Structures.

![insertion sort](01-introduction/Insertion_sort.gif)

You can find the source code of this algorithm in Python here. The complexity of this algorithm is O(x<sup>2</sup>) because it consists of two nested loops.