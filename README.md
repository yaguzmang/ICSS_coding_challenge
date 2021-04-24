# ICSS Coding Challenge
This is the repository where you can find my solutions to the alaTest/ValueChecker (ICSS) challenge 2021

## Author :black_nib:
- Yhoan Alejandro Guzmán García
> yaguzmang@eafit.du.co

## Routing of telephone calls - The challenge :memo:
The challenging part of routing telephone calls in this context is to handle any number of operators with thousands of price entries and then calculate the cheapest operator for a certain number. 
Even though all entries fit into memory, it is important to have a way to store the data least redundantly. For example, if we were to traditionally store the entries '46' and '468', we would need to store two different prefixes, while the only difference is the '8' at the end. The same happens when calculating the best price. We would need to look at the prefixes '46' and then '468', while the only difference is the '8' at the end.

## The solution :bulb:
The solution, accounting for the mentioned challenges, is a modified prefix Trie data structure. This data structure solves the redundant data and lookups.
The structure is as follows: 
El diseño elegido que se planteó para la realización del aplicativo es el siguiente:
![](images/data_structure.png)
**Imagen 1** - Trie data structure