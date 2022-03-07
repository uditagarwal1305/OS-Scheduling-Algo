#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Defining a First come first serve function
def findWaitingTime(processes, n,bt, wt):


    wt[0] = 0


    for i in range(1, n ):
        wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTime(processes, n,bt, wt, tat):

    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime( processes, n, bt):

    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    
    findWaitingTime(processes, n, bt, wt)
    
    findTurnAroundTime(processes, n,bt, wt, tat)

    print( "Processes Burst time " +" Waiting time " +" Turn around time")


    for i in range(n):

        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +str(bt[i]) + "\t " + str(wt[i]) + "\t\t " + str(tat[i]))

    print( "Average waiting time = "+ str(total_wt / n))
    print("Average turn around time = "+ str(total_tat / n))


if __name__ =="__main__":


    processes = [ 1, 2, 3]
    n = len(processes)


    burst_time = [13,4 ,6 ]

    findavgTime(processes, n, burst_time)


# In[6]:


#SJF
def arrangeArrival(n, array):
    for i in range(0, n):
        for j in range(i, n-i-1):
            if array[1][j] > array[1][j+1]:
                for k in range(0, n):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]
 
 
def CompletionTime(n, array):
    value = 0
    array[3][0] = array[1][0] + array[2][0]
    array[5][0] = array[3][0] - array[1][0]
    array[4][0] = array[5][0] - array[2][0]
    for i in range(1, n):
        temp = array[3][i-1]
        mini = array[2][i]
        for j in range(i, n):
            if temp >= array[1][j] and mini >= array[2][j]:
                mini = array[2][j]
                value = j
        array[3][value] = temp + array[2][value]
        array[5][value] = array[3][value] - array[1][value]
        array[4][value] = array[5][value] - array[2][value]
        for k in range(0, 6):
            array[k][value], array[k][i] = array[k][i], array[k][value]
 
 
if __name__ == '__main__':
    n = 4
    arr = [[int(i) for i in range(1, n+1)], [2, 0, 4, 5],
           [3, 4, 2, 4], [0]*n, [0]*n, [0]*n]
    arrangeArrival(n, arr)
    CompletionTime(n, arr)
    print("Process     Arrival        Burst        Completion        \tWaiting        \tTurnaround ")
    waitingtime = 0
    turaroundtime = 0
    for i in range(0, n):
        print(arr[0][i], "\t\t", arr[1][i], "\t\t", arr[2][i],
              "\t\t", arr[3][i], "\t\t", arr[4][i], "\t\t\t", arr[5][i])
        waitingtime += arr[4][i]
        turaroundtime += arr[5][i]
    print("Average waiting time is ", (waitingtime/n))
    print("Average Turnaround Time is  ", (turaroundtime/n))
 


# In[8]:


# Round Robin
def findWaitingTime(processes, n, bt, wt, quantum):
    rem_bt = [0] * n
 
    
    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0 
 
    
    while(1):
        done = True
 
        
        for i in range(n):
             
            
            if (rem_bt[i] > 0) :
                done = False 
                 
                if (rem_bt[i] > quantum) :
                 
                    
                    t += quantum
 
                    
                    rem_bt[i] -= quantum
                 
                
                else:
                 
                 
                    t = t + rem_bt[i]
 
                   
                    wt[i] = t - bt[i]
 
                    
                    rem_bt[i] = 0
                 
        
        if (done == True):
            break
             

def findTurnAroundTime(processes, n, bt, wt, tat):
     
    
    for i in range(n):
        tat[i] = bt[i] + wt[i]
 
 

def findavgTime(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n
 
    
    findWaitingTime(processes, n, bt,
                         wt, quantum)
 
   
    findTurnAroundTime(processes, n, bt,
                                wt, tat)
 
 
    print("Processes    Burst Time     Waiting",
                     "Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i],
              "\t\t", wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turn around time = %.5f "% (total_tat / n))
     

if __name__ =="__main__":
     

    proc = [1, 2, 3]
    n = 3
 
  
    burst_time = [14, 5, 7]
 

    quantum = 2;
    findavgTime(proc, n, burst_time, quantum)


# In[9]:


#Priority
def findWaitingTime(processes, n, wt):
    wt[0] = 0
 
    # calculating waiting time
    for i in range(1, n):
        wt[i] = processes[i - 1][1] + wt[i - 1]
 

def findTurnAroundTime(processes, n, wt, tat):
     
    # Calculating turnaround time by
    # adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]
 


def findavgTime(processes, n):
    wt = [0] * n
    tat = [0] * n
 
    # Function to find waiting time
    # of all processes
    findWaitingTime(processes, n, wt)
 
    # Function to find turn around time
    # for all processes
    findTurnAroundTime(processes, n, wt, tat)
 
    # Display processes along with all details
    print("\nProcesses    Burst Time    Waiting",
          "Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", processes[i][0], "\t\t",
                   processes[i][1], "\t\t",
                   wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.5f "%(total_wt /n))
    print("Average turn around time = ", total_tat / n)
 
def priorityScheduling(proc, n):
     
    # Sort processes by priority
    proc = sorted(proc, key = lambda proc:proc[2],
                                  reverse = True);
 
    print("Order in which processes gets executed")
    for i in proc:
        print(i[0], end = " ")
    findavgTime(proc, n)
     
# Driver code
if __name__ =="__main__":
     
    # Process id's
    proc = [[1, 10, 1],
            [2, 5, 0],
            [3, 8, 1]]
    n = 3
    priorityScheduling(proc, n)
     


# In[10]:


# Consumer-Producer
import threading
import time
 

CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
 

mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
 

class Producer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
     
    items_produced = 0
    counter = 0
     
    while items_produced < 20:
      empty.acquire()
      mutex.acquire()
       
      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced : ", counter)
       
      mutex.release()
      full.release()
       
      time.sleep(1)
       
      items_produced += 1
 

class Consumer(threading.Thread):
  def run(self):
     
    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full
     
    items_consumed = 0
     
    while items_consumed < 20:
      full.acquire()
      mutex.acquire()
       
      item = buffer[out_index]
      out_index = (out_index + 1)%CAPACITY
      print("Consumer consumed item : ", item)
       
      mutex.release()
      empty.release()      
       
      time.sleep(2.5)
       
      items_consumed += 1
 

producer = Producer()
consumer = Consumer()
 

consumer.start()
producer.start()
 

producer.join()
consumer.join()


# In[11]:


#Dead Lock
P = 5
R = 3


def calculateNeed(need, maxm, allot):
    for i in range(P):
        for j in range(R):
              
            
            need[i][j] = maxm[i][j] - allot[i][j] 
  


def isSafe(processes, avail, maxm, allot):
    need = []
    for i in range(P):
        l = []
        for j in range(R):
            l.append(0)
        need.append(l)
          
    
    calculateNeed(need, maxm, allot)
  
    
    finish = [0] * P
      
  
    safeSeq = [0] * P 
  
   
    work = [0] * R 
    for i in range(R):
        work[i] = avail[i] 
  
    count = 0
    while (count < P):
 
        found = False
        for p in range(P): 
          
          
            if (finish[p] == 0): 
              
               
                for j in range(R):
                    if (need[p][j] > work[j]):
                        break
                
                if (j == R - 1): 
                  
                    
                    for k in range(R): 
                        work[k] += allot[p][k] 
  
              
                    safeSeq[count] = p
                    count += 1
  
                
                    finish[p] = 1
  
                    found = True
                  
       
        if (found == False):
            print("System is not in safe state")
            return False
          
  
    print("System is in safe state.",
              "\nSafe sequence is: ", end = " ")
    print(*safeSeq) 
  
    return True
  

if __name__ =="__main__":
      
    processes = [0, 1, 2, 3, 4]
  
    avail = [3, 3, 2] 
  
    
    
    maxm = [[7, 5, 3], [3, 2, 2],
            [9, 0, 2], [2, 2, 2],
            [4, 3, 3]]
  
    allot = [[0, 1, 0], [2, 0, 0],
             [3, 0, 2], [2, 1, 1],
             [0, 0, 2]] 
  
 
    isSafe(processes, avail, maxm, allot) 


# In[18]:


# Page Replacement FIFO
print("Enter the number of frames: ",end="")
capacity = int(input())
f,fault,top,pf = [],0,0,'No'

#s = list(map(int,input().strip().split()))
s = [ 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
print("\nString|Frame →\t",end='')
for i in range(capacity):
    print(i,end=' ')
print("Fault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%capacity
        fault += 1
        pf = 'Yes'
    else:
        pf = 'No'
    print("   %d\t\t"%i,end='')
    for x in f:
        print(x,end=' ')
    for x in range(capacity-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))


# In[15]:


# Page Replacement LRU
mem = 4
processList = [ 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

s = []
 
pageFaults = 0

for i in processList:
    if i not in s:
        if(len(s) == mem):
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        pageFaults +=1
    else:
        s.remove(i)
        s.append(i)
        
print("Page Faults: ",pageFaults)


# In[19]:


# Disc Scheduling FCFS
size = 8
 
def FCFS(arr, head):
 
    seek_count = 0
    distance, cur_track = 0, 0
 
    for i in range(size):
        cur_track = arr[i]
 
       
        distance = abs(cur_track - head)
 
        seek_count += distance
 
       
        head = cur_track
     
    print("Total number of seek operations = ", seek_count)
 
    
    print("Seek Sequence is")
 
    for i in range(size):
        print(arr[i])
     

if __name__ == '__main__':
 
    
    arr = [ 176, 79, 34, 60,
            92, 11, 41, 114 ]
    head = 50
 
    FCFS(arr, head)


# In[20]:


#SSTF
def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)
     

def findMin(diff):
 
    index = -1
    minimum = 999999999
 
    for i in range(len(diff)):
        if (not diff[i][1] and
                minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index
     
def shortestSeekTimeFirst(request, head):            
        if (len(request) == 0):
            return
         
        l = len(request)
        diff = [0] * l
         
        # initialize array
        for i in range(l):
            diff[i] = [0, 0]
        
        seek_count = 0
         
        
        seek_sequence = [0] * (l + 1)
         
        for i in range(l):
            seek_sequence[i] = head
            calculateDifference(request, head, diff)
            index = findMin(diff)
             
            diff[index][1] = True
             
            
            seek_count += diff[index][0]
             
         
            head = request[index]
     
        
        seek_sequence[len(seek_sequence) - 1] = head
         
        print("Total number of seek operations =",
                                       seek_count)
                                                         
        print("Seek Sequence is")
         
       
        for i in range(l + 1):
            print(seek_sequence[i])
     

if __name__ =="__main__":
  
    proc = [176, 79, 34, 60,
            92, 11, 41, 114]
    shortestSeekTimeFirst(proc, 50)


# In[22]:


#SCAN
size = 8
disk_size = 200
 
def SCAN(arr, head, direction):
 
    seek_count = 0
    distance, cur_track = 0, 0
    left = []
    right = []
    seek_sequence = []
 
   
    if (direction == "left"):
        left.append(0)
    elif (direction == "right"):
        right.append(disk_size - 1)
 
    for i in range(size):
        if (arr[i] < head):
            left.append(arr[i])
        if (arr[i] > head):
            right.append(arr[i])
 
    
    left.sort()
    right.sort()
 
  
    run = 2
    while (run != 0):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                cur_track = left[i]
 
                
                seek_sequence.append(cur_track)
 
              
                distance = abs(cur_track - head)
 
                
                seek_count += distance
 
         
                head = cur_track
             
            direction = "right"
     
        elif (direction == "right"):
            for i in range(len(right)):
                cur_track = right[i]
                 
               
                seek_sequence.append(cur_track)
 
             
                distance = abs(cur_track - head)
 
           
                seek_count += distance
 
                
                head = cur_track
             
            direction = "left"
         
        run -= 1
 
    print("Total number of seek operations =",
          seek_count)
 
    print("Seek Sequence is")
 
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])

arr = [ 176, 79, 34, 60,
         92, 11, 41, 114 ]
head = 50
direction = "left"
 
SCAN(arr, head, direction)


# In[ ]:




