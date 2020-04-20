# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 14:49:25 2020

@author: Anonymous
"""
import numpy as np
import random
#molecular conformers
#part a

conformerA = 150
conformerB = 150

#in every hour 20% of conformerA will become B.,,
#moreso, in every hour 10% of conformerB will become A

def transition(conformerA, conformerB):
    newB = 20*conformerA/100
    newA = 10*conformerB/100 - newB
    
    newB = newB - 10*conformerB/100
    
    B1 = newB+ conformerB
    A1 = newA + conformerA
    print("conformerA", A1)
    print("ConformerB", B1)
    
    vector = np.array([[A1],
                       [B1]])
    print(vector)
    return vector


vector = transition(conformerA, conformerB)


#part b
def matrixprob(vector):
    p = np.array([[0.8,1.2],
                  [1.1,0.9]])
    
    mult = vector * p
    print(p)
    print("mult: ", mult)
    #todo test hermitian matrix

vector = np.array([[150],
                   [150]])   
matrixprob(vector)

#part c
#set up loop for 72 hours

def longtime(vector):
    conformerA = vector[0][0]
    conformerB = vector[1][0]
    vector = transition(conformerA, conformerB)
    print("newA and B: ", vector)
    return vector

for x in range(0,72):
    vector = longtime(vector)

#after reaching a poitn where conformer A is 100, and conformerB is 199.01..
# the populations of conformer A and B become constant or stable throughout 
# the rest of the days.
   


#problem 2
def find_fix_point(a, x0):
    '''
    a ois the growth rate
    x0 is the initial value
    '''
    #should return the convergence point of the sequence
    #xn lets populate it to 0.1 to 1.0f
    x = [0.0]
    for n in range(0.1, 1.0):
        x[n+1] = a * x[n] *( 1-x[n])
        #nb the convergence point comes when 1-xn = 0
        if x[n] == 0:
            break
    else:
        convergencepoint = n
        return convergencepoint
    
    return None

#problem 2(b)

def variation(a_init, a_final):
    
    x_list = {0:[]}
    for a in range(a_int, a_final):
        #loop over 50 possible values for x0 in the range [0,1]
        if a not in x_list:
            x_list[a] = [] #create a list for the values of x
        for x in range(0,50):
            #choose them at random
            x0 = math.random() #for 50 random points between 1 and 0
            x_list[a].append(x0) #store all possible values of x in list
    
    #now make a scatter plot
    # the scatter plot is the hardest part here since each combination of x,y
    # has multiple values of x