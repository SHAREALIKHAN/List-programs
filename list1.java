Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
[1, 2, 3, 4]
answer:
package JAVA2;
import java.util.*;

public class List1 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		List <Integer> mylist=new ArrayList();
		for(int i=0;i<n;i++) {
			int b=sc.nextInt();
			mylist.add(b);
		}
		System.out.println(mylist);
	}

}
output:
4
1
2
3
4
[1, 2, 3, 4]

