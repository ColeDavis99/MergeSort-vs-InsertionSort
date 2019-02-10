'''//////////////////////////////////////////////////////////////////////
/// Project1.py
/// Cole Davis, CS2500 Algorithms. Section 1A
/// This file contains the class Sort() as well as the drivers for it.
//////////////////////////////////////////////////////////////////////
'''

import time
import math
import random

import matplotlib.pyplot as plt
plt.xlim([0, 50000000])
plt.ylim([0, 10000])
plt.ylabel('Runtime (Seconds)')
plt.xlabel('Data Size')




'''
//////////////////////////////////////////////////////////////////////
/// Sort class
/// This class contains the code for merge and insertion sort.
/// It is constructed with a list of data to be sorted. With that
/// Data, you can choose to perform one of the two sorting operations
//////////////////////////////////////////////////////////////////////
'''
class Sort():
    #Paramaterized Constructor
    def __init__(self, Array):
        #Here's the input set we're given
        self.Array = Array
        self.data_size = len(Array)
        
        self.merge_sort_time = 0
        self.insertion_sort_time = 0
        

        

    def do_merge_sort(self):
        #Make a copy of the data set for merge_sort to use
        merge_sort_arr = list(self.Array)

        #Time merge sort
        start = time.time()
        self.merge_sort(merge_sort_arr)
        end = time.time()

        #Plot the time taken and the data size
        self.merge_sort_time = (end-start)
        print("Merge sort time: ",str(self.merge_sort_time))
        plt.scatter(len(merge_sort_arr),self.merge_sort_time, color = "b")

    

    def do_insertion_sort(self):

        #Make a copy of the data set for insertion_sort to use
        insertion_sort_arr = list(self.Array)

        #Perform Insertion Sort
        start2 = time.time()
        self.insertion_sort(insertion_sort_arr)
        end2 = time.time()

        #Plot the time taken and the data size
        self.insertion_sort_time = (end2-start2)
        print("Insertion sort time: ",str(self.insertion_sort_time))
        plt.scatter(len(insertion_sort_arr),self.insertion_sort_time, color = "r")




    def insertion_sort(self, Arr):
        for i in range(1,len(Arr)):
            dec = i-1
            elem = Arr[i]
            while(dec >= 0 and Arr[dec] > elem):
                Arr[dec+1] = Arr[dec]
                dec = dec-1
            Arr[dec+1] = elem
            
        
             
    def merge_sort(self, Arr):
        #Base case
        if(len(Arr) > 1):
            middle = int(len(Arr)/2) #Casting to an int() because splice operator below requires ints, and interpreter is typing it to a float for some reason

            #Splice to get our right and left sub arrays
            L = Arr[:middle]
            R = Arr[middle:]

            #Recursive Calls
            self.merge_sort(L)
            self.merge_sort(R)


            #Below this line is where the comparisons happen and the lists are sorted in ascending order
            left_ctr = 0
            right_ctr = 0
            total_ctr = 0

            #While there's still elements left in both lists
            while(left_ctr < len(L) and right_ctr < len(R)):
                if(L[left_ctr] <= R[right_ctr]):
                    Arr[total_ctr] = L[left_ctr]
                    left_ctr = left_ctr+1

                    
                else:
                    Arr[total_ctr] = R[right_ctr]
                    right_ctr = right_ctr+1 
                total_ctr = total_ctr+1 #Increment every time

        
            #The two while loops copy the rest of the elements in if one sub array was emptied before the other. Only one of these while loops will execute.
            while(left_ctr < len(L)):
                Arr[total_ctr] = L[left_ctr]
                total_ctr=total_ctr+1
                left_ctr = left_ctr+1

            while(right_ctr < len(R)):
                Arr[total_ctr] = R[right_ctr]
                total_ctr = total_ctr+1
                right_ctr = right_ctr+1




#Appends an array into the Testing list
def Rand(iterations, lower_bound, upper_bound):
    arr = []
    for j in range(iterations):
        arr.append(random.randint(lower_bound, upper_bound))
    return arr

#Appends an array into the Testing list
def nearly_sorted(iterations):
    arr = []
    for j in range(iterations):
        if(j%50 == 0):
            arr.append(0)
        else:
            arr.append(j*2)
    print("array is ",len(arr))
    return arr





'''
Driver Below
'''
#Random Element Values
INCREMENTER1 = 5000
LOWER_BOUND1 = 0
UPPER_BOUND1 = 45000
for i in range(LOWER_BOUND1, UPPER_BOUND1, INCREMENTER1):
    Arr = Rand(i, 0, 1000)
    SortObject = Sort(Arr)
    print (i)
    print()
    print()

    #Call the sorts
    SortObject.do_insertion_sort()
    SortObject.do_merge_sort()


#Nearly Sorted Element Values
INCREMENTER1 = 500
LOWER_BOUND1 = 500
UPPER_BOUND1 = 30500
for i in range(LOWER_BOUND1, UPPER_BOUND1, INCREMENTER1):
    Arr = nearly_sorted(i)
    SortObject = Sort(Arr)
    print (i)
    print()
    print()


    #Call the sorts
    SortObject.do_insertion_sort()
    SortObject.do_merge_sort()


plt.show()

