def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
a=[7,2,1,6,8,3,10,29]
bubble(a);
for i in range(len(a)):
    print(a[i])
