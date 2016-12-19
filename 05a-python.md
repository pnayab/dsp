# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

###Differences
1. **Mutability:** Lists are mutables(can be edited) while tuples are immutable(fixed values). As a result of this, tuples are easier on memory and processor. We can gain performance optimization using tuples at the right places. 
2. **Syntax:** List members are listed within square brackets [] while tuple members are enclosed in parenthesis (), or just comma separated list of values.
3. **Usage:** Tuples are heterogenous while lists are homogenous. Python interpreter does not enforce this, but the better way of usage is - the items contained in  tuples express different concepts. Tuples are semantic -  they have an inherent meaning to them. Items in a list express the same concept or belong to the same category and idea they express.

###Similarity
1. **Operators:** Lists and tuples have mostly the same operators. Bracker operator indexes an element [], slice operator selects a range of elements. 
2. **Values:** Lists and tuples can have any type of values.

Tuples are used as keys in dictionaries because they are hashable. A dictionary is implemented using a hash table. A hash is a function that takes a value and returns an integer. Dictionaries use these integers, called hash values, to store and look up key-value pairs. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

###Differences
1. **Order:** Lists are ordered and can be accessed by index while sets are unordered and hence does not record the position or order of insertion. Accordingly, sets do not support indexing, slicing, or other sequence-like behavior.
2. **Duplicates:** Lists can have duplicated while sets cannot have duplicates
3. **Objects type:** Lists can contain any type of objects while sets can only have hashable objects.
4. **Mathematical operations:** Sets support mathematical operations like union, intersection, difference, and symmetric difference.

###Similarity
1. **Mutable:** Lists and sets are both mutable

###Examples of using lists:


###Examples of using Sets:
Basic examples include membership testing and eliminating duplicates

###Performance:
Finding an element in a set is vastly faster, especially for large sets. That is because the set uses a hash function to map to a bucket. Since Python implementations automatically resize that hash table, the speed can be constant  no matter the size of the set.
In contrast, to evaluate whether an object is a member of a list, Python has to compare every single member for equality.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is the keyword used in python to describe an anonymous function. Anonymous functions are also called lambda functions. Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. We use lambda functions when we require a nameless function for a short period of time. In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments). Lambda functions are used along with built-in functions like filter(), map() etc.
* Example 1:
double = lambda x: x * 2
print(double(5))

* Example 2:
sorted(["Pallavi", "Jai", "Nayab", "anushri"], key = lambda word: word.lower())


###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions provide compact, elegant, and efficient ways to encode a few common idioms in programming. List comprehensions are a tool for transforming one list (any iterable actually) into another list. During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.

new_things = []
 for items in old_things:
    if condition_based_on(ITEM):
       new_things.append("something with " + ITEM)

*
We can rewrite this for loop as a list comprehension:
* 
new_things = ["something with " + ITEM for ITEM in old_things if condition_based_on(ITEM)]
* 

Example 1: with map
*
def capitalise_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
* 
Equivalent with list comprehension
* 
def capitalise_all(t):
    return [s.capitalize() for s in t]
* 
Example 2: with filter
*  
def only_upper(t):
    res = []
    for i in t:
        if i.isupper():
            res.append(i)
    return res
* 
Equivalent with list comprehnesion
* 
def only_upper(t):
    return [s for s in t if s.isupper()]
* 
Every list comprehension can be rewritten as a for loop but not every for loop can be rewritten as a list comprehension.
List comprehensions are concise and easy to read for simple expressions. They are also usually much faster than the equivalent for loops used in maps and filters.

**Set Comprehensions:**
Similar to List Comprehensions.
s = {x for x in range(10)}

**Dictionary Comprehension:**
Dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
a = {x: x+2 for x in (2, 4, 6)}


###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





