import tkinter.messagebox as me
from tkinter import *


class myGUI:
    def __init__(self, web_name):
        self.web_name = web_name
        self.web_name.title("词语接龙v1.0")
        self.web_name.geometry("300x200")
        self.last_one = ""  # 上一个单词
        self.temp = ""  # 当前单词
        self.long = 0  # 词语长度
        self.base = ""  # 单词库
        self.num = 0  # 统计接上了多少个
        self.prompt = StringVar()  # 提示语

    def interface(self):
        # 界面模块
        self.prompt.set("请输入第一个词语（字数不限）：")
        self.L1 = Label(self.web_name, textvariable=self.prompt)
        self.L1.pack()
        self.E1 = Entry(self.web_name)
        self.E1.pack()
        # B1 = Button(self.web_name, text="确定", command=self.next_action)
        # B1.pack()
        self.web_name.bind("<Return>", self.next_action)
        B2 = Button(self.web_name, text="结束游戏", command=self.game_over)
        B2.pack()
        self.web_name.mainloop()

    def function(self):
        # 校验最后一个字能不能接上上一个
        if self.temp[0] == self.last_one[-1]:
            return True
        else:
            return False

    def next_action(self, event):
        self.temp = self.E1.get()
        # 输入为空时
        if not self.temp:
            me.showinfo("提示", "都没输入我怎么接")
        else:
            # 输入第一个单词时，此时base为空
            if not self.base:
                self.base = self.temp
                self.long = len(self.temp)
                self.last_one = self.temp
                me.showinfo("提升", "输入成功，后面记得都按这个格式哦~出了bug不修复的")
                self.E1.delete(0, END)
            # 输入长度不规范时
            elif len(self.temp) != self.long:
                me.showinfo("提示", f"需要输入{self.long}个字！重来")
                self.E1.delete(0, END)
            # 只有两个字的时候字也不能重复
            elif self.long == 2 and self.temp[-1] in self.base:
                me.showinfo("提示", "如果是两个字的词语，后一个字之前不能出现过哦")
                self.E1.delete(0, END)
            # 输入重复的单词时
            elif self.temp in self.base:
                me.showinfo("提示", "之前有这个词语了，重新想一个")
                self.E1.delete(0, END)
            # 输入正确时
            else:
                self.prompt.set("请输入接龙词语：")
                flag = self.function()
                if flag:
                    self.base += self.temp
                    self.last_one = self.temp
                    self.num += 1
                    me.showinfo("提示", "完美！继续加油")
                else:
                    me.showinfo("提示", "都不是一个字，重新输入")
                self.E1.delete(0, END)

    def game_over(self):
        if 0 <= self.num < 10:
            me.showinfo("成就", f"此次一共接了{self.num}个词，你识字吗？")
        elif 10 <= self.num < 30:
            me.showinfo("成就", f"此次一共接了{self.num}个词，连小学生都不如")
        elif 30 <= self.num < 50:
            me.showinfo("成就", f"此次一共接了{self.num}个词，恭喜你，赶上小学生了")
        elif 50 <= self.num < 70:
            me.showinfo("成就", f"此次一共接了{self.num}个词，比小学生厉害一点")
        elif 70 <= self.num < 100:
            me.showinfo("成就", f"此次一共接了{self.num}个词，可以参加高考了")
        else:
            me.showinfo("成就", f"此次一共接了{self.num}个词，哇大神，让我膜拜一下")
        me.showinfo("退出", "游戏结束")
        self.web_name.destroy()


if __name__ == '__main__':
    top = Tk()
    mg = myGUI(top)
    mg.interface()
