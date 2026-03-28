# x = int(input())
# res = 0

# while x:
#     dight = x%10
#     x = x//10
#     res = (res*10) +dight

# print(res)


# def reverse(x):
#     res = 0
#     while x:
#         dight = x%10
#         x = x//10
#         res = (res*10) +dight
#     return res 


# num = int(input())
# print (reverse(num))




# class reverse:
#     def __init__(self, x):
#         self.original_number = x
#         self.reversed_number = self.reverse_num()

#     def reverse_num(self):
#         num = self.original_number
#         res = 0
#         while num:
#             last = num %10
#             num = num//10
#             res = (res *10) +last
#         return res    

#     def  get_reversed_num(self):
#         return self.reversed_number
    
#     def __str__(self):
#         return f"The original number{self.original_number} and the reversed number {self.reverse_num()}"

        

# x = int(input("enter number"))

# rev = reverse(x)
# print(rev)





# class Student:
#    def __init__(self, fname, lname, age, section):
#        self.firstname = fname
#        self.lastname = lname
#        self.age = age
#        self.section = section
# # creating a new object
# stu1 = Student("Sara", "Ansh", 22, "A2")

# print(stu1.firstname)



# class Solution: 
#     def frequency(self, nums):
#         self.hashmap = {}
#         for i in nums:
#             if i in self.hashmap:
#                 self.hashmap[i] +=1
#             else: 
#                 self.hashmap[i] = 1

#     def display(self):

#         for i,v in self.hashmap.items():
#             print(f"value{i} , count{v}")


# nums =  [8,2,3,4,5,6,6,6,6,3,1,3,8,5,9]

# sol1 = Solution()
# sol1.frequency(nums)

# sol1.display()


# def rev(num):
#     res = 0
#     is_neg = False

#     if num<0:
#         num = abs(num)
#         is_neg = True

#     while num:
#         d = num%10 
#         num = num//10
#         res = (res*10)+d

#     if is_neg:
#         return -res    
#     return res


# num = 123

# print(rev(num))



# def rev(s):
#     s = list(s)

#     l,r = 0,len(s)-1

#     while l<r :
#         s[l],s[r] = s[r],s[l]
#         l+=1
#         r-=1
#     return "".join(s)

# s = "hello does this work"

# print(rev(s))




# def rev(s):
#     s = list(s)

#     l,r = 0,len(s)-1

#     while l<r :
#         s[l],s[r] = s[r],s[l]
#         l+=1
#         r-=1
#     return "".join(s)

# s = "hello does this work"

    

# print(rev(s))



# def rev(s):
#     s = s.split()

#     l,r = 0,len(s)-1

#     while l<r :
#         s[l],s[r] = s[r],s[l]
#         l+=1
#         r-=1

#     return " ".join(s)
  



# s = "hello does this work"

# print(rev(s))



s= ["h","e","l","l","o"]


def rev(l,r):
    if l<r:
        s[l],s[r] = s[r],s[l] 
        return rev(l+1,r-1)
    else:
        return s    

print(rev(0,len(s)-1))











