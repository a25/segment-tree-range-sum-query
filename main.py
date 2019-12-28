import math
arr = [1, 3, 5, 7, 9, 11]; 
length=len(arr)
x=2**int(math.ceil(math.log2(length)))
seg_len=2*x-1
tree=[0]*seg_len
print(tree)
a=[1,2]
# print(sum(a))

def construct(array,parent,mi,ma):
  # partial_arr_len=len(array)
  # print(array[mi:ma+1],parent)
  tree[parent]=sum(array[mi:ma+1])
  if(mi==ma):
    return array[mi]
  mid=(mi+ma)//2
  
  a=construct(array,2*parent+1,mi,mid)
  b=construct(array,2*parent+2,mid+1,ma)
  # print(a,b)
parent=0
construct(arr,parent,0,len(arr)-1)
print(tree)

def rangesum(array,parent,mi,ma,qmi,qmax,tree):
  if(qmi<=mi and qmax>=ma ):
    return tree[parent]##
  elif(qmi>ma or qmax<mi ):
    return 0
  else:
    mid=(mi+ma)//2
    return rangesum(array,2*parent+1,mi,mid,qmi,qmax,tree)+rangesum(array,2*parent+2,mid+1,ma,qmi,qmax,tree)
print(rangesum(arr,0,0,len(arr)-1,0,1,tree))


  

  

