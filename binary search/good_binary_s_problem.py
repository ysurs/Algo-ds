Problem link: https://codeforces.com/problemset/problem/750/A

1. take care of the minimum number of problems solved, it is 0
2. there can be a case when target=0 i.e when there is no time left to solve the any problems


def function(input_values):
    
    cumulative_time=[]
    max_problems=0
    
    problems=int(input_values.split(" ")[0])
    minutes=int(input_values.split(" ")[1])
    target=240-minutes
    
    if target==0:
        print(0)
        return
    
    for i in range(1,problems+1):
        cumulative_time.append(5*i)
    
    for i in range(1,len(cumulative_time)):
        cumulative_time[i] = cumulative_time[i]+cumulative_time[i-1]
        
    l=0
    r=len(cumulative_time)-1
    
    while l<=r:
        mid=l+(r-l)//2
        if cumulative_time[mid]==target:
            print(mid+1)
            return
        elif cumulative_time[mid]>target:
            r=mid-1
        else:
            max_problems=max(max_problems,mid+1)
            l=mid+1
            
    print(max_problems)
    return
        
    
def main():
    
    input_values = input()
    
    function(input_values)
 
 
if __name__ == "__main__":
    main()