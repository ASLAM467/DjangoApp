# from django.test import TestCase
#
# # Create your tests here.
# #This is a comment
# x="awesome"
# print("python is "+x)
# def myfunc():
#     global x
#     x="fantastic"
#     print("python is "+x)
# myfunc()
# print("python is "+x)
#
#
# a="hello world"
# print("length of a is ",len(a))
# print(a[2:5])
#
# """
# for x in "banana":
#     print(x)
#
# txt="The best things in life are free!"
# if "best" not in txt:
#     print("No. expensive is not present.")
#
# """
# quantity = 3
# itemno = 500
# price = 50.50
# myorder="I want {} pieces of itemno {} for {} dollars"
# print(myorder.format(quantity,itemno,price))
#
#
#
#
#
#
#
#
#

# lst = [1,2,3,4]
# lst.append(6)
# print(lst)
# print(lst)
#
#
#
# lt =(1,2,3,3,4,1,2)
# v = list(lt)
# v.append(5)
# x= set(v)
# x.add(9)
# print(x)
# a = 2
# while a < 5 :
#     print("printing")
#     a = a+1
#
#
#
# l=[1,2,3,4,5]
# for j in l:
#     if j%3==0:
#         print("even "+ str(j))
#     elif j%3==1:
#         print("somethin")
#     else:
#         print("came here")
#
# d = ([{"name":"sudheer","age":23},{"name":"bujji"},{"name":"tarun"}])
#
# # for i in d:
# #     i['name'] = i['name'] + " Gorle"
# #     try:
# #         print(i['age'])
# #     except Exception as e:
# #         print("no key")
#
7

rows=int(input("Enter number of rows:"))
for i in range(rows+1):
     for j in range(i):
         print(j,end=" ")
     print(" ")

