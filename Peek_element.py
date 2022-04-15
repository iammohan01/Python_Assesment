
def findpeek(arr , n) :
        ret = []
        if (n==1) :
            return arr[0]
        if (n==2) :
            if (arr[0] < arr[1] ) :
                return arr[1]
            else :
                return arr[0] 
         

        for i in range(1,n):
        
            if arr[i-1]<arr[i]>arr[i+1] :
                ret.append(arr[i])
        return ret
       

#code starts here
print('-------------------------')
ar = [4,5,345,54,543,35,423,42345,324,23143,2,42,134,12,342,34,234,23543,5]
print(findpeek(ar , ar.__len__()))
