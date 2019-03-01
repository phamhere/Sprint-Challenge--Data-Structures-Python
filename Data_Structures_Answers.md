Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

2. What is the space complexity of your `depth_first_for_each` function?

3. What is the runtime complexity of your `breadth_first_for_each` method?
   `O(n)` since we're going through all the values of the BST.
4. What is the space complexity of your `breadth_first_for_each` method?
   `O(n)` since we're using a list to queue up all the nodes of the BST.

5. What is the runtime complexity of the provided code in `names.py`?
   `O(n*m)` since for every element of the first names list you loop through, you loop through the the entire seconds names list.
6. What is the space complexity of the provided code in `names.py`?
   `O(n)` since a list is used to store the values of the duplicates between the names list.
7. What is the runtime complexity of your optimized code in `names.py`?
   `O(n+m)` where `n` is the size of the first names list and `m` is the size of the second names list. Here I created a dictionary to get O(1) access time when looping through the second names list and seeing if there where any dublicates with the first names list.
8. What is the space complexity of your optimized code in `names.py`?
   `O(n+m)` where `n` is the size of the dictionary that is storing all the values of the first names list and `m` is the size of the duplications list that is storing all the values of the duplicates between the names list.
