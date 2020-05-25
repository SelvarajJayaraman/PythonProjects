"""
Created on 25-May-2020

@author: Selvaraj Jayaraman
"""
print("#  Python Set Statement")
print("***********************")

a = {1, 2, 3, 4}
print("A is type:", type(a))

b = {1, 2, 5, 6}
print("B is type:", type(b))

c = set()
print("C is type:", type(c))

c.add(1)
c.add(2)
c.add(3)
print("After adding set collection values:", c)

c.remove(2)
print("After using remove method:", c)

c.pop()
print("After pop method:", c)

# mixed collection in set
d = {(1, 2), (3, 4)}
print("Mixed Set collection:", d)

# DeepCopy
e = {1, 2, 3, 4}
f = e
print("Deep copy of set collection:", e)
print("Deep copy of set collection:", f)

e.add(5)
f.add(6)
print("Deep copy of set collection:", e)
print("Deep copy of set collection:", f)

# ShallowCopy
g = e.copy()
print("Shallow copy of set collection:", g)
e.add(7)
print("after adding value in set(e) collection:", e)
print("after adding value in set(e) and copy(g) collection:", g)

# Difference Method
print("a difference b output:", a.difference(b))
print("b difference a output:", b.difference(a))

a.difference_update(b)
print("a difference update method:", a)

a = {1, 2, 3, 4}
print("Difference method symbol (-):", a - b)

# Union Method
print("Union method:", a.union(b))
print("Union method symbol (|):", a | b)

# Intersection Method
print("Intersection method:", a.intersection(b))
print("Intersection method symbol (&):", a & b)

a.intersection_update(b)
print("Intersection update method:", a)

# isdisjoint Method
c = {1, 2, 3, 4, 5, 6}
d = {8, 9, 10}
print("a isdisjoint of c:", a.isdisjoint(c))
print("d isdisjoint of c:", d.isdisjoint(c))

# isSubset Method
print("a issubset of c:", a.issubset(c))
print("d issubset of c:", d.issubset(c))

# issuperset Method
c = {1, 2}
print("d issuperset of a:", d.issuperset(a))
print("a issuperset of c:", a.issuperset(c))

# symmetric Method
a = {1, 2, 4}
b = {1, 5, 6}

print("a symmetric difference method symbol (^) b :", a ^ b)
print("a symmetric difference Method b:", a.symmetric_difference(b))

