"""
Created on 18-May-2020

@author: Selvaraj Jayaraman
"""
print("#  python List statement");
print("*********************");

list1 = [1,2,3,4,5,6];

print("Length of list:",len(list1));
print("Type of list:",type(list1));

print("max value in list:", max(list1));
print("min value in list:", min(list1));

list1.insert(2, 10);
print("Inserted value list:", list1);

print("take and remove value from list:", list1.pop(3));
print("After removing value from list:", list1);

list1.sort(key=None, reverse=False)
print("Sorted list:", list1);

print("Remove value from list:", list1.remove(2));

print("Reversed list:", list1.reverse());

print("Iterating list values:");
for i in list1:
    print(i);
