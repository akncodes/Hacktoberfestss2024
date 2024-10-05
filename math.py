import math 

minimum = 100
maximum = 200

min_multiple = math.ceil(minimum / 35) * 35
max_multiple = math.floor(maximum / 35) * 35

result = range(min_multiple, max_multiple+1, 35) 

if result: 
	print(*result, sep='\n') 
else: 
	print("No numbers found.") 
