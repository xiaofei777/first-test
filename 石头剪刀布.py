import  random
ch=["石头","剪刀","布"]
class  computers:
    def __init__(self):
        self.m=random.choice(ch)
    scorec=0

class players:
    def __init__(self):
        self.n=input("你出什么?:")
    scorep=0
class cc:
    def dd(self):
        print("欢迎来到游戏，输了就要挨打")
        print("进入游戏选1:")
        print("退出游戏选2:")
    def game(self):
        sh=computers()
        pl=players()
        computer = sh.m
        player=pl.n
        if computer==player:
            print("平局")
        elif player=="石头":
            if computer == "布":
                print("你输了!\n", computer, "克制", player)
            else :
                print("你赢了\n",player,"克制",computer)
        elif player=="剪刀":
            if computer=="石头":
                print("你输了!\n", computer, "克制", player)
            else :
                print("你赢了\n", player, "克制", computer)
        else :
            if computer=="剪刀":
                print("你输了!\n", computer, "克制", player)
            else :
                print("你赢了\n", player, "克制", computer)
    def playgame (self):
        self.dd()
        i=int(input())
        if i==1:
            self.game()
        elif i==2:
            print("成功退出游戏")
        else :
            print("输错了，笨蛋")

m=cc()
cc().playgame()









