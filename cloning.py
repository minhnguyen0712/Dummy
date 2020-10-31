# A function to find factorial of a 
# given number 
def fact(num): 
	fact = 1; 
	
	while(num>1): 
		fact = fact * num; 
		num = num-1; 
	return fact; 

# Find nth catalan number 
def catalan(n): 
	return fact(2 * n)//(fact(n)*fact(n + 1)) 

# Driver Code 
if __name__ == '__main__': 
	
	# size of arr[] 
	n = 5
	
	# Elements in arr[] 
	arr = [1, 2, 3, 4, 5] 

	for k in range(n): 
		s = 0
	
		# Count the number of element 
		# less than current element 
		# in arr[k] 
		for i in range(n): 
			if arr[i] < arr[k]: 
				s+= 1

		# Here s = number of node in left 
		# BST and (n-s-1) = number of node 
		# in right BST 
		# Find number of BST using elements 
		# in left BST 
		catalan_leftBST = catalan(s) 
		
		# Find number of BST using elements 
		# in right BST 
		catalan_rightBST = catalan(n-s-1) 
		
		# Find total number of BST 
		totalBST = catalan_rightBST * catalan_leftBST 
		
		# Print total BST count 
		print(totalBST, end =" ") 
