class Solution:
    def selectionSort(self, arr,n):
        n = len (arr)
        for i in range(0,n):
            k = i
            for j in range (i+1,n):
                if arr[j] < arr[k]:
                    k = j
            if i!=k:
                arr[i], arr[k] = arr[k],arr[i]
        return arr 
