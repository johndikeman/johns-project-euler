# Euler 52: Permuted Multiples
# Link : https://projecteuler.net/problem=52

def permutation(num1, num2):
	if(set(str(num1)) == set(str(num2)) and len(str(num1)) == len(str(num2))):
		return True
	else:
		return False

solution = -1
i = 1
while( i < 1000000):
	if(permutation(i,2*i)):
		if(permutation(i,3*i)):
			if(permutation(i,4*i)):
				if(permutation(i,5*i)):
					if(permutation(i,6*i)):
						solution = i
						break
	i = i + 1

print(solution)
