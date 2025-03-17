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

First, ``random.seed()`` determines the seed used to generate "random" numbers. This helps ensure security by individualising the pearson table generated.

```py
pearson_table = list(range(256))
random.shuffle(pearson_table)
```

These two lines contribute to the table being deterministic, anyone with the same pearson table can map the same keys to the same values.

Now we start the algorithm itself:
```py
def pearson_hash(key: str, size: int):
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

This is fairly simple, our hash starts at 0. For each character in our key, we set the hash to ``pearson_table[hash ^ ord(char)]``.
This line takes a bit of explaining. First, ``ord(char)``, gives is the integer for the unicode character we input. Next, we use ``^`` with the current hash value.
``^`` performs a bitwise XOR operation, essentially returning the bits in ``hash_`` _or_ ``ord(char)``, but not both. Finally, we access the integer at that index of the pearson table. This ensures collision resistance, as common
characters within the key do not result in only a small number of returned values. This is also not a complex algorithm, making it very efficient as a hashing algorithm.

Lastly, we ``return hash_ % size``, which ensures the value is within the range of the hash table's array.

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Your answer here

```
class HashMap:
   
   int size = 10
   array<playerList> with length of size
   
   private function hash returns int:
      <implement chosen hash algorithm>
      
   public function add(player):
      var index = this.hash(player.uid)
      this.array[index].append(player)
      
   public function get(key):
      var index = this.hash(player.uid)
      
      foreach (player in this.array[index]):
         if player.uid == key:
            return player
         raise Error("Key not found")
         
   
class PlayerList:
   
   Player head
   
   public function append(player):
       player.next = this.head
       this.head = player
   
class Player:

   string uid
   string name
   nullable player next
```


## Reflection

1. What was the most challenging aspect of this task?

> Your answer here

From the whole assignment, the main difficulty was completing the knowledge questions, it can be difficult to put knowledge into words
and explain sometimes.

For the practical aspect of the assessment, it was mostly reworking the existing PlayerList and Player classes to work with how I wanted to
implement the HashMap. As they were parts of a previous assessment with restrictions, there were certain refactors that had to be made in order to
implement the HashMap, as I had not written PlayerList with a HashMap in mind previously.

It was also difficult to write tests for HashMap. I don't usually like unittests that require me to look multiple data structures down to understand, I had to check PlayerList and
Player to understand how HashMap should behave, this may be due to the "skeleton" nature of their implementation or it may just be part of testing 3 layers of custom data structures
that build on each other.

Another part of the HashMap that I found difficult to decide how to implement was deciding where to put the
hashing function. While I decided to put it in Player, it was not a decision I liked, ideally I would have put it in HashMap.
The main reason I didn't is because Player is the only value I wanted to hash, so it was easier to just call ``__hash__`` of the Player,
which allows me to control how the Player is hashed easily. If I were to implement the HashMap again I would try to put the hashing algorithm as
part of the HashMap itself, instead of in Player.

2. If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?

> Your answer here

Even if I wasn't implementing a PlayerList specifically, I probably would have used a linked list of some kind. Build properly, they are
very easy to work with from their own methods, without having to deal with issues such as limited size - although in the event of a _resize
being implemented the limited size of something like a ListArray, and in python this wouldn't be a concern regardless - but the base data structure wouldn't matter too much either way.

The main change would be with how the following syntax works:
```py
my_hashmap[key] = value
```

With PlayerList, I'm the key is part of the data structure itself - ``Player.uid`` - so the key is part of the data structure. Since ``Player.name`` is the only other
data stored within ``Player``, it makes sense that I would change the name of the player in ``__setitem__`` given these restrictions. If ``PlayerList`` wasn't a requirement,
I would probably use the following structure:
```
HashMap -> LinkedList -> LinkedListNode
```

In this case, ``LinkedListNode`` would simply have ``key`` and ``value``, which is similar to the current structure, except ``value`` could be any kind of object.
While technically its only a small difference, the main logic is the same for the general implementation of a linked list, regardless of what its storing. In this case
I would just rather the key and value be more seperated.

The other part I would consider refactoring are the ``display()`` and  ``__repr__`` methods of ``PlayerList`` and ``Player``. While they do accurately display the data,
it is rather verbose and somewhat difficult to read. The ``key`` value of a ``LinkedListNode`` would only exist purely for the ``HashMap``, since its not required for storing data in a linked list.
I would probably have ``LinkedList.display`` (if implemented) display data in this kind of format:
```
LinkedList((key: '1', value: 1), (key: '2', value: 2), (key: 'Hello', value: 'World!'))
```

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
