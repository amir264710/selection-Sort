import numpy as np
def selectionSort(x):
  for i in range(len(x)): 
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i + 1, len(x)): 
        if x[min_idx] > x[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    x[i], x[min_idx] = x[min_idx], x[i]

############  Driver to test the function
n = 4
x = np.array([0] * 4, int)
for i in range(len(x)):
    line = input("Enter a number: " )
    x[i] = int(line)
    
selectionSort(x)
print ("Sorted array") 
for i in range(len(x)): 
    print("%d" %x[i]),
