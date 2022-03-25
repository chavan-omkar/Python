"""
it is used in documentation
"""
# f = open('MyData','r')
# print(f.readline(),end="")
# print(f.readline())

# f1 = open('abc','w')
# f1 = open('abc', 'a')
# f1.write("Something we have to write here")
# f1.write(' people please suggest something ')

# for data in f:
#     f1.write(data)


i1 = open('IMG_0382.JPG','rb')

i2 = open("PIC.JPG",'wb')

for i in i1:
    # print(i)
    i2.write(i)