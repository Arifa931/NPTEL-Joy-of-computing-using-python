def linear_search(n,x):
    e=[]
    for i in range(1,n):
        e.append(i)
    flag=0
    count=0
    for i in e:
        count+=1
        if(i==x):
            
            print("Number is found at position: "+str(i))
            flag=1
            break;
    if(flag==0):
        print("Number not found")
    print("Total number of iterations: "+str(count))
    
          
