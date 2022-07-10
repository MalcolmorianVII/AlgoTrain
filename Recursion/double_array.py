def double_array(arr,index=0):
    if index == len(arr):
        return 
    arr[index] *= 2
    double_array(arr,index + 1)

aray = [1,2,3,4,5,6]
double_array(aray)
print(aray)