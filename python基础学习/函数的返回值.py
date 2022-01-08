def sum_numb(numb1,numb2):
    '''对两个数字求和'''
    result=numb1+numb2
    #可以用返回值告诉调用一方的结果
    return result
#return表示被返回的值，下方的代码不会被执行

#可以用变量，来接收函数执行返回的结果
result_sum=sum_numb(10,20)
print('计算结果：%s' % result_sum )

# 计算面积函数
def area(width, height):
    return width * height

def print_welcome(name):
    print("Welcome", name)

print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))