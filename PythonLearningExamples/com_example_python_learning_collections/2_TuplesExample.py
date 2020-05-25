'''
Created on 18-May-2020

@author: Selvaraj Jayaraman
'''
print("#  Python Tuples  statement");
print("************************");

tuple1 = (1,2,3,4,5,6);
print("Tuples type:",type(tuple1));

tuple2 = tuple1 + (4,);
print("Adding values to type:",tuple2);

print("Print value based on index:",tuple2[2]);

print("Slicing tuples:", tuple2[2:]);

print("Length of tuple:",len(tuple1));

print("Max value of tuple:",max(tuple1));

print("Min value of tuple:",min(tuple1));

print("Count of value in tuple:",tuple1.count(5));

print("Index of value in tuple:",tuple1.index(5));

print("Iterated values from tuple:");
for i in tuple1:
    print(i);
    
a=(1,2,3);
b=(4,5,6);
c = a+b;
print("concated tuples:",c);

nestedTuple=((1,2),(3,4),(5,6));
print("Nested tuples:",nestedTuple);

for j in nestedTuple:
    k = j;
    print(k);
    for l in k:
        print(l);
        
d = [1,2,3,4,5];
print("Converting list to tuple:", tuple(d));