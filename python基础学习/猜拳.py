#导入随机工具包，在顶部导入方便下面继续使用
import random
#输入要出的拳/石头/剪刀/布
player=int(input('请输入您要出的拳 1石头/2剪刀/3布:'))
#电脑随机出拳，随机整数randint()
computer=random.randint(1,3)
print('玩家出的拳是 %s  - 电脑出的拳是%s' % (player,computer))
#比较胜负
#1石头胜剪刀
#2剪刀胜布
#3布胜石头
#if () or () or ()
if ((player==1 and computer==2)
        or (player==2 and computer==3)
        or  (player==3 and computer==1)):
    print('恭喜你胜利了！')
elif player==computer:
    print('平局')
else:
    print('败北')


