"""Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules: 

>Only one disk can be moved at a time.
>Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
>No disk may be placed on top of a smaller disk."""
 
def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return   
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  

disks = int(input('Enter the number of disks: '))   
tower_of_hanoi(disks, 'A', 'B', 'C') 