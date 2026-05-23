class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        for i in range(n):
            a=i+1
            b=n-1
            find=target-numbers[i]
            while a<=b:
                mid=(a+b)//2
                if numbers[mid]==find:
                    return [i+1,mid+1]
                elif numbers[mid]<find:
                    a=mid+1
                else:
                    b=mid-1