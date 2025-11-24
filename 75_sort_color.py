class Solution(object):
    def sortColors(self, nums):
        l, r = 0, len(nums)-1
        i =0

        while i<=r:
            if nums[i] ==0:
                nums[l], nums[i] = nums[i], nums[l]
                l +=1



            elif nums[i] ==2:
                nums[i],nums[r] = nums[r],nums[i]
                r-=1
                i-=1 

            i+=1    



# time :O(n)
# space :O(1)
# single pass solution 






class Solution(object):
    def sortColors(self, nums):
        counts =  [0,0,0]

        for i in nums:
            counts[i] +=1

        R, W, B  = counts
        nums[:R] = [0]*R
        nums[R:W+R] = [1]*W  
        #or use nums[R:W+1]
        nums[R+W:] = [2]*B

# time :O(n)
# space :O(1)


