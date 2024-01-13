
#Name: Jack Wyeth
import math 
def bubblesort(array,size):
    swap_counter=0
    for x in range(len(array)):
        for y in range(0, len(array)-x-1):
            if array[y]>array[y+1]:
                temp =array[y]
                array[y]=array[y+1]
                array[y+1]=temp
                swap_counter+=1
    bubble_math=size*(size-1)//2
    return bubble_math,swap_counter

def selectionsort(array,size):
    swap_counter=-1
    for x in range(size):
        min_index=x
        for y in range(x+1,size):
            if array[y]<array[min_index]:
                min_index=y
        array[x],array[min_index]=array[min_index],array[x]
        swap_counter+=1
    selection_math=size*(size-1)//2
    return selection_math, swap_counter

def insertionsort(arr):
    key_comparisons = 0
    array_assingments=0
   
    n=len(arr)

    for x in range(1, n): 
        key = arr[x] 
        y = x-1

        while y >= 0 and key < arr[y]:  
            arr[y+1] = arr[y]  
            array_assingments+=1
            y -= 1
            
            key_comparisons+=1
        #comparison was made and returned false
        if y>=0:
            key_comparisons+=1
        arr[y+1] = key  
        array_assingments+=1
    return key_comparisons, array_assingments




def mergesort(arr):
    if len(arr) <= 1:
        return 0
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursive call on each half
    key_comparisons = mergesort(left) + mergesort(right)

    # Two iterators for traversing the two halves
    x = 0
    y = 0
    
    # Iterator for the main list
    z = 0
    
    while x < len(left) and y < len(right):
        key_comparisons += 1
        if left[x] <= right[y]:
            arr[z] = left[x]
            x += 1
        else:
            arr[z] = right[y]
            y += 1
        z += 1

    while x < len(left):
        arr[z] = left[x]
        x += 1
        z += 1

    while y < len(right):
        arr[z]=right[y]
        y += 1
        z += 1

    return key_comparisons

 


    

def main():
    
    arr=[]
    
    size=int(input())
    flag=0
    while(flag<size):
        var=int(input())
        arr.append(var)
        flag+=1
    #at this point in the program we have our array filled in and then we make four deep copies to apply to the four algorithms   
    bubble_array=[]
    selection_array=[]
    insertion_array=[]
    merge_array=[]

    for val in arr:
        bubble_array.append(val)
        selection_array.append(val)
        insertion_array.append(val)
        merge_array.append(val)
    



    bkey,barray=bubblesort(bubble_array,size)
    print(bkey,"",barray)

    skey,sarray=selectionsort(selection_array,size)
    print(skey,"",sarray)

    ikey,iarray=insertionsort(insertion_array)
    print(ikey,"",iarray)

    mkey= mergesort(merge_array)
    print(mkey)


if __name__=="__main__": 
    main() 
