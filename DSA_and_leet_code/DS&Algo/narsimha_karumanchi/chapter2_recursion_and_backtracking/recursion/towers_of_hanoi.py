def towers_of_hanoi(n, source, auxiliary, target):
    
    if n == 1:
        # Base case: If there is only one disk, move it from the source to the target peg.
        print(f"Move disk 1 from peg {source} to peg {target}")
        return
    else:
        # Recursive case:
        # 1. Move the top n-1 disks from the source peg to the auxiliary peg using the target peg as auxiliary.
        towers_of_hanoi(n-1, source, target, auxiliary)
        
        # 2. Move the nth disk from the source peg to the target peg.
        print(f"Move disk {n} from peg {source} to peg {target}")
        
        # 3. Move the n-1 disks from the auxiliary peg to the target peg using the source peg as auxiliary.
        towers_of_hanoi(n-1, auxiliary, source, target)

# Example usage:
n = 3
source = 'A'
auxiliary = 'B'
target = 'C'
print(f"Number of Disks = {n} \nThe Source peg is {source} \nThe Auxiliary Peg is {auxiliary} \nThe Target peg is {target}")

towers_of_hanoi(n, source, auxiliary, target)

"""
The time complexity for this algorithm is O(2^n)

The base case of recursion is n=1

The recusive case of recursion is n>1


"""









"""
Text-book solution for solving towers of Hanoi recursion 

def towersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
    if numberOfDisks:
        towersOfHanoi (numberOfDisks-1, startPeg, 6-startPeg-endPeg)
        print(f"number of disks:{numberOfDisks}, Start Peg: {startPeg}, End Peg:{endPeg}")
        print ("Move disk %d from peg %d to peg %d" % (numberOfDisks, startPeg, endPeg))
        towersOfHanoi (numberOfDisks-1, 6-startPeg-endPeg, endPeg)
"""
