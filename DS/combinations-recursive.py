def combinations(arr,i,result,path):
    if i ==len(arr):
        result.append(path)
        return
    pwc=path+[arr[i]]
    combinations(arr,i+1,result,path)
    combinations(arr,i+1,result,pwc)

arr=[1,2,3]
path=[]
result=[]
combinations(arr,0,result,path)
print(result)
