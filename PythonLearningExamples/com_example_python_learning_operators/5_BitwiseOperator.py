'''
Created on 13-May-2020

@author: selvaraj
'''
print("#10  Python Logical Operator");
print("*************************");

'''
& - Logical And operator

2 --> 0010
3 --> 0011 
-----------
2 <--0010
-----------
'''
print(2 & 3);

'''
| - Logical OR operator

2 --> 0010
3 --> 0011 
-----------
3 <-- 0011
-----------
'''
print( 2 | 3);

'''
^ - Logical Ex OR operator
2 --> 0010
3 --> 0011 
-----------
3 <-- 0001
-----------
'''
print( 2 ^ 3);

'''
~ - Logical Compement operator
--> ~2
--> -(2+1) = -3
'''
print(~2);

'''
<< - Logical Left Shift operator
2 --> 0010
<< -> 2<<1 --> 0100 -> 4
'''
print(2 << 1);

'''
>> - Logical Right Shift operator
2 --> 0010
>> -> 2>>1 --> 0001 -> 1
'''
print(2 >> 1);