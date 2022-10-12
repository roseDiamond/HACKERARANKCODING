def plusMinus(arr):
    # Write your code here
    l= len(arr)
    n=0
    p=0
    z=0
    for i in arr:
        if i >0:
            p=p+1
        elif i<0:
            n=n+1
        
        else:
            z=z+1
    po=p/l
    no = n/l
    zo = z/l     
    print(f'{po:.3f}')   
    print(f'{no:.6f}')   
    print(f'{zo:.6f}')  
plusMinus([1,2,3,0.-1,-9])
v=[1,2,3,0.-1,-2]