# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return 0

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')



def hanoi(n,A,C,B):
    if n==1:
        print("move disk 1 from {} to {}".format(A,C))
        return 0
    hanoi(n-1,A,B,C)    
    print("move {} from {} to {}".format(n,A,C))
    hanoi(n-1,B,C,A)




disks = int(input('Number of disks to be displaced: '))  
hanoi(disks, 'A', 'C', 'B')