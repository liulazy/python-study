#


import cards_tools

#无限循环由用户决定什么时候退出循环
while True:
    #显示菜单功能
    cards_tools.show_num()
    action_str=input("你想选择的操作是：")
    print("您选择的操作是【%s】" % action_str)
    #1,2,3针对名片的操作
    if action_str in ["1","2","3"]:
        #1.新增名片
        if action_str=="1":
            cards_tools.new_card()
        #2.显示名片
        elif action_str=="2":
            cards_tools.show_all()
        #3.查询名片
        elif action_str=="3":
            cards_tools.serach_card()

    #0退出系统
    elif action_str =="0":
        print("欢迎再次使用【名片管理系统】")
        break
        #如果在开发，时不希望立刻编写分支内部的代码
        #可以使用pass关键字，是一个占位符，能够保证代码结构正确
        #程序运行时pass关键字不会进行任何的操作
        #pass
    #其他内容输入错误需要提示用户
    else:
        print("您输入的不正确，请重新选择")