'''
4)Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
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
numbers1=[]
for i in range(a):
    num=int(input())
    if num%2==0:
        numbers.append(num)
    else:
        numbers1.append(num)
print('Even numbers is:',numbers)
print('Odd numbers is:',numbers1)

Output:
5
1
2
3
4
5
Even numbers is: [2, 4]
Odd numbers is: [1, 3, 5]
