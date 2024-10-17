'''
5)Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
'''
Answer:
a=int(input())
numbers=[]
for i in range(a):
    num=int(input())
    numbers.append(num)
sum_of_numbers=sum(numbers)
print('sum of numbers is:',sum_of_numbers)

Output:
5
2
4
1
3
1
sum of numbers is: 11
