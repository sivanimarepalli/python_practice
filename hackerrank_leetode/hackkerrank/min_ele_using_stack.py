# Implement a stack that supports push, pop, top, and getMin operations in O(1) time, where getMin returns the minimum element.

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    # Write your code here
    actual_stack=[]
    min_stack=[]
    result=[]
    val=0
    for op in operations:
        parts=op.split()
        if parts[0]=="push":
            val=int(parts[1])
            actual_stack.append(val)
            
            if len(min_stack)==0 or val<=actual_stack[-1]:
                min_stack.append(val)
        if parts[0]=="pop":
            if actual_stack:
                popped_val=actual_stack.pop()
                if popped_val==min_stack[-1]:
                    min_stack.pop()
        if parts[0]=="top":
            result.append(actual_stack[-1])  
        if parts[0]=="getMin":
            result.append(min_stack[-1])
    return result

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
