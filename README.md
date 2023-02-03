# Genetic-code

## Introduction
In this project, I use the A* algorithm to generate a genetic code that I want to reach, by starting from a sequence of numbers 1 to n. In this project, we have a restriction that we can only generate this genetic code by swapping the position of code 1 with other codes under the following conditions (1 code is in the i index):
<br>
* If the remainder of i by 4 equals 0, then code number 1 can go to positions i-4, i+4, i-1, and i+1.
* If the remainder of i by 4 equals 1, then code number 1 can Go to positions i-4, i+4, i-3, and i-1.
* If the remainder of i by 4 equals 2, then code number 1 can go to positions i-4, i+4, i+3, and i+1.
* If the remainder of i by 4 equals 3, then the code number 1 can go to positions i-4, i+4, i-1, and i+1.
## What is A* algorithm?
A* (pronounced "A-star") is a graph traversal and path search algorithm, which is used in many fields of computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its O ( <var>b</var><sup>d</sup> ) space complexity, as it stores all generated nodes in memory. Thus, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance, as well as memory-bounded approaches; however, A* is still the best solution in many cases.

Peter Hart, Nils Nilsson and Bertram Raphael of Stanford Research Institute (now SRI International) first published the algorithm in 1968. It can be seen as an extension of Dijkstra's algorithm. A* achieves better performance by using heuristics to guide its search.
Compared to Dijkstra's algorithm, the A* algorithm only finds the shortest path from a specified source to a specified goal, and not the shortest-path tree from a specified source to all possible goals. This is a necessary trade-off for using a specific-goal-directed heuristic. For Dijkstra's algorithm, since the entire shortest-path tree is generated, every node is a goal, and there can be no specific-goal-directed heuristic. [More about A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
