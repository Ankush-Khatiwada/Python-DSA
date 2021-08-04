from time import time 

start_time=time()

for i in range(1,100):
	print('Hello')

end_time=time()
elapsed=end_time-start_time

print(elapsed)


'''
Find maximum

'''

def find_maximum(data):
	biggest = data[0] #The initial value
	for val in data: #For each value
		if val > biggest:#if it is greater than
			biggest=val#Found new biggest so far
	return biggest#Biggest is the max
find_maximum()			