'''
6)Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
'''
Answer:
a=int(input())
numbers=[]
for i in range(a):
    num=int(input())
    numbers.append(num)
min_number=min(numbers)
print('minimum number is:',min_number)

Output:

5
12
2
4
5
6
minimum number is: 2
