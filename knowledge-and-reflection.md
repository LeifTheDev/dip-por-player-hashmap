# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> Your answer here

A hash function is a function used to map a key to a (usually integer). Usually, this is used within hash tables to 
map any given key to an index within the size of the hash table.

Theres a few characterisics that hash tables share, one of which is that they are deterministic. A given set of inputs will always
produce the same output (although different algorithms may have their own unique inputs, such as pearson hash using a pearson table).
This is critical since it allows items to be both entered and retrieved from the hash table by their key correctly.

In addition to this, there are a few desirable properties that hashing functions should have.

The values returned by the hash function should be distributed evenly across the range of indexes within the size of the hash
table. This is to minimise collisions, which slow-down the lookup time of values in the hash table.

Hash functions should have large sensitivity, meaning that small changes to the input value of a hash function should result in a large change to the output, 
which helps ensure that the outputs of the hash function are evenly distributed within the hash table's size.

While less important than the other properties in the context of a hash table - since security isn't necessarily a concern,
it should be impossible/unfeasible to determine the input value of a hash function from its output.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some reasearch to answer this question 😱

> Your answer here

The first hash function:
```py
def ssh(key):
    return 1
```
This function is not suitable for use within a hash table, as it will always return ``1`` regardless of its input. This means that it
has no uniformity, collision resistance or sensitivity, which means that no benefits will be gained from implementing a hash table. 

Despite this, this function does have determinism and efficiency.

For the second hash function:
```py
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

This is a much more suitable hash function for use within a hash table, as it has a lot more uniformity, while also being deterministic.
However, the uniformity of this hash function is still not perfect, since different characters are far more likely to appear than others.

The security of this hash function is reasonably suitable for hash tables.

For the third hash function:
```py
import random

random.seed(42)

pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The pearson hash function has high uniformity, security, efficiency and sensitivity. Its uniform and has high sensitivity due to the fact that
it maps characters to other values, removing the issues with summing ascii values. Its also secure since it uses a "pearson table" to map values. Since this table
can be randomly generated, its unfeasible to determine what the initial value was before the hash. Due to its uniformity and sensitivity, it has a high collision resistance.


As for the fourth hash function, ``hash()`` calls ``__hash__()`` under the hood, so by default - in python 3.4+ - the SipHash
function is used. As well as being generally suitable in terms of uniformity and efficiency, this is hashing function is used by python as
it is difficult to execute collision attacks.

And finally for the fifth hash function:
```py
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

SHA256 is one of the most common hashing functions, most often for passwords, SSL, etc. 
SHA256 outputs a 256 bit, regardless of the size of the input, which contributes to its security.

Overall, its a very secure hashing function and has high collision resistance, however it is slow compared to other options.
For the purposes of a hash table, its probably not a suitable choice, as the level of security it offers is unnecessary.



3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> Your answer here

1. Determinism
2. Efficiency
3. Collision Resistance

Determinism is critical since the whole purpose of a hash map is to be able to store and retrieve a value by a key. If
there is no way to map a key to a value, the hash table is useless.

Efficiency is also very important for hash tables. As the hash function is used whenever a read or write happens
in the hash table, having an efficient (fast) hash function is very important. A slow hash function will immediately 

Finally, collision resistance is also important for hash functions. Having a large amount of collisions will reduce
the read speed of the hash table, especially as it grows in items. This can be mitigated by increasing the size (size of the initial array used to store values) of the
hash table, but this is still an important factor to consider when picking a hash function. 

Security is usually less important in the context of a hash table, as they typically aren't used for secure long-term data storage.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> Your answer here

I would choose to implement the pearson hash.

Theres a couple reasons for this:

First, it is reasonably efficient and collision resistant, which means that read and write speeds for the hash table
will remain acceptable, regardless of the size of the hash table.

The pearson algorithm can also be easily implemented without using any external libraries, which is nice for the purposes of preventing sudden breaks
in the event that python or a library updates.

Finally, since it uses a pearson table (which can be saved/shared) as part of the algorithm, it allows us to work with
persistent data (if we want to) while maintaining security. Only users we share the pearson table with can
map a key to its hash - and by extension its value.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> Your answer here

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Your answer here

## Reflection

1. What was the most challenging aspect of this task?

> Your answer here

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> Your answer here

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
