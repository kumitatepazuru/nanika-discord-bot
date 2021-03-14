import json
import random


class hannou:
    def __init__(self,file="./data/hannou.json"):
        with open(file) as f:
            self.hannou_list = json.load(f)

    async def msg(self,message,mc):
        if mc.find("おはよう") != -1:
            await message.channel.send(random.choice(self.hannou_list["ohayo_list"]))
        elif mc.find("ただいま") != -1:
            await message.channel.send(random.choice(self.hannou_list["tadaima_list"]))
        elif mc.find("どやぁ") != -1 or mc.find("どやあ") != -1 or mc.find("どや") != -1 or mc.find("どやどや") != -1:
            await message.channel.send("wwwwwwwwwwwwwwwwwwwww")
        elif mc.find("うんち") != -1 or mc.find("うんこ") != -1:
            await message.channel.send("トイレに行ってこい！(圧")
        elif mc.find("やかましいわ") != -1:
            await message.channel.send("w")
        elif mc.find("くさ") != -1 or mc.find("草") != -1 or mc.find("笑") != -1 or mc.find("www") != -1:
            await message.channel.send(random.choice(self.hannou_list["sorena_list"]))