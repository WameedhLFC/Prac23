N = int(input("Enter the number of triples: "))
A,B,C = [],[],[]
for i in range(N):
    A.append(input(f"Enter a triple #{i+1}: "))
for i in A:
    X = i.split()
    B = []
    for j in X:
        B.append(int(j))
    C.append(B)
for i in C:
    for j in i:
        if j < max(i) and j > min(i):
            print(j)      
##################################################################################################################
##################################################################################################################
# Problem Statement:
# Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

# Input:
# First line contains the number of triples, N.	
# The next N lines which follow each have three space separated integers.

# Output:
# For each of the N triples, output one new line which contains the second-maximum integer among the three.

# Constraints:
# 1 ≤ N ≤ 6
# 1 ≤ every integer ≤ 10000
# The three integers in a single triplet are all distinct. That is, no two of them are equal.

# Sample Input:
# 3
# 1 2 3
# 10 15 5
# 100 999 500

# Sample Output:
# 2
# 10
# 500