# ICSS Coding Challenge
This is the repository where you can find my solution to the alaTest/ValueChecker (ICSS) challenge 2021 and my CV.

## Author :black_nib:
### Yhoan Alejandro Guzmán García
> yaguzmang@eafit.du.co
### CV:
[Resume Yhoan Alejandro Guzman Garcia](CV/Resume_Yhoan_Alejandro_Guzman_Garcia.pdf)
### Relevant code examples:
- [Fish store - code](https://github.com/jsperezsalazar2001/AquaLife)

I can not share the code of other projects since the codebases are not public and I am under an NDA.

## Routing of telephone calls - The challenge :memo:
The challenging part of routing telephone calls in this context is to handle any number of operators with thousands of price entries and then calculate the cheapest operator for a given phone number. 

Although all entries fit in memory, it is important to have a less redundant way of storing data. For example, if we were to traditionally store the entries '46' and '467', we would need to store two different prefixes, while the only difference is the '7' at the end. The same happens when calculating the best price. We would need to look at the prefixes '46' and then '467', while the only difference is the '7' at the end.

## The solution :bulb:
### Storing the data:
My solution, accounting for the mentioned challenges, is a data structure similar to a Trie. This data structure solves the redundant data and lookups:

![](Images/data_structure.png)
**Image 1** - Data structure

This data structure considerably lowers the memory usage as it inserts prefixes by only adding the non-existing digits. It also allows handling any number of operators. As seen in the image, it is possible to differentiate operators by adding the `operator:price` pairs in the digit nodes.
### Finding the cheapest operator:
To find the cheapest operator, we need to traverse the Trie following the each digit in the phone number. When we encounter a digit node that contains `operator:price` pairs, we know that those operators support the phone number up to the current digit. After finding the supported prefixes and their prices and operators, it is only a matter of picking the cheapest. It is important to note that the supported prefixes found are the longest matching prefixes per operator.

Here you can see how the algorithm works:

![](Images/find_cheapest.gif)
**Animated Image 1** - Finding the cheapest operator
### Asymptotic Computational Complexity of the solution:
The cost of inserting prefixes and finding the cheapest operator is `O(phone_length) + O(number_operators)`. In comparison, a regular list lookup would cost `O(N)`, where N is the total number of entries.

When it comes to the memory complexity, the upper bound is `O(m*n)`, where `m` is the average length of the prefixes and `n` is the number of prefixes. This upper bound is only met in cases where the prefixes do not share digits in common. The average memory consumption would be much lower as many prefixes can share digits in common.

From the Asymptotic Computational Complexity analysis, we can conclude that the solution is very efficient. The only trade-off with a regular list implementation is the insertion cost. Inserting in a list costs only `O(1)`, but insertion only happens once per prefix, so the trade-off makes sense. 

## Application (command line) demo :computer:
![](Images/demo.gif)
**Animated Image 2** - App demo
## About the implementation :keyboard:

The code was developed in python 3.8, following the next class diagram for the Trie and TrieNode classes:
![](Images/trie_class_diagram.png)
**Image 2** - Trie and TrieNode class diagram

The [unit tests](Coding%20challenge/tests/test_trie.py) were implemented with the python unittest framework, passing all tests in 0.002s.

For any other information or question, feel free to reach out.