https://codeforces.com/problemset/problem/1795/B

for _ in range(int(input())):
    n,k=map(int,input().split(' '))
    
    
    '''
        1. First of all, we shouldn't consider those intervals where target is not present.
        2. We should remove them.
        3. The question asks if we could have an ideal number or not.
        4. An ideal number is possible if we remove all those intevals where the target is not present and:
        5. If after removing intervals, we have this case:
            lets say target=3
            
            [1,3],[2,4]- we won't be able to have an ideal number because 3's count will be 2 and 2's count will be 2
            We either should have an interval like [3,3] or our intervals should be of the form:
            [1,3],[3,4] only then we can have an ideal number at 3
    '''
    
 
    right=True
    left=True
 
    for i in range(n):
        l,r=map(int,input().split(' '))
        if l==k:
            left=False
        if r==k:
            right=False
        
    print("No" if left or right else "Yes")