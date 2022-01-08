for num in  [1,2,3]:
    print(num)
    if num==2:
        break
#如果循环体内部使用了break退出了循环，那么else下方的代码几不会被执行
else:
    print("会执行吗")

print("循环结束")
