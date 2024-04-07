#Given an array arr[] of distinct integers of size N and a value sum, the task is to find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.
class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        c=0
        arr.sort()
        
        for k in range(n-2):
            i=k+1
            j=n-1
            
            while i<j:
                s=arr[i]+arr[j]+arr[k]
                if s<sumo:
                    c+=j-i
                    i=i+1
                else:
                    j=j-1
        return c 