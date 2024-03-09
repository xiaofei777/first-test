import  random
ch=["石头","剪刀","布"]
class  computers:
    def __init__(self,score):
        self.m=random.choice(ch)
        self.scorec=score
class players:
    def __init__(self,score):
        self.n=input("你出什么?:")
        self.scorep=score
class cc:
    def dd(self):
        print("欢迎来到游戏，游戏初始化中...")
        print("进入游戏选 1:")
        print("退出游戏选 2:")
    def game(self):
        number=int(input("请输入你想玩的局数："))
        h=1
        a=0
        b=0
        w=0
        while h<=number:
            co = computers(a)
            pl = players(b)
            computer = co.m
            player = pl.n
            if computer==player:
                print("平局")
                h+=1
            elif player=="石头":
                if computer == "布":
                    print("你输了!\n", computer, "克制", player)
                    co.scorec+=1
                    h += 1
                else :
                    print("你赢了\n",player,"克制",computer)
                    pl.scorep+=1
                    h += 1
            elif player=="剪刀":
                if computer=="石头":
                    print("你输了!\n", computer, "克制", player)
                    co.scorec+=1
                    h += 1
                else :
                    print("你赢了\n", player, "克制", computer)
                    pl.scorep+=1
                    h += 1
            elif player=="布":
                if computer=="剪刀":
                    print("你输了!\n", computer, "克制", player)
                    co.scorec+=1
                    h += 1
                else :
                    print("你赢了\n", player, "克制", computer)
                    pl.scorep+=1
                    h += 1
            else :
                w=w-1
                print("输错了，笨蛋，再重新输入")
            a=co.scorec
            b=pl.scorep
            w+=1
        print("********最后的结果********")
        print(f"总局数{w}局")
        print(f"电脑{co.scorec}分")
        print(f"玩家{pl.scorep}分")
        if co.scorec>pl.scorep:
            print("运气真的差，电脑赢了")
        elif co.scorec==pl.scorep:
            print("你和电脑势均力敌啊")
        else:
            print("运气不错，你赢了")
    def playgame (self):
        self.dd()
        i=int(input())
        if i==1:
            self.game()
        elif i==2:
            print("成功退出游戏")
        else :
            print("输错了，笨蛋,请在1和2之间输入一个")

m=cc()
cc().playgame()









