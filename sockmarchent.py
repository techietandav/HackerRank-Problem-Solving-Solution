def sockMerchant(n, ar):
    count=0
    ar.sort()
    i=0
    while i<n-1:
        if ar[i]==ar[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    return count

if __name__ == '__main__':
    

    n = int(input())

    ar = list(map(int, input().split()))

    result = sockMerchant(n, ar)
    print(result)

    
