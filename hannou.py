class hannou:
    def __init__(self,file="./data/hannou.json"):
        with open(file) as f:
            self.hannou_list = json.load(f)

    def msg(self,message,mc):
        if mc.find("おはよう") != -1:
            await message.channel.send(random.choice(ohayo_list))
        elif mc.find("ただいま") != -1:
            await message.channel.send(random.choice(tadaima_list))
        elif mc.find("どやぁ") != -1 or mc.find("どやあ") != -1 or mc.find("どや") != -1 or mc.find("どやどや") != -1:
            await message.channel.send("wwwwwwwwwwwwwwwwwwwww")
        elif mc.find("うんち") != -1 or mc.find("うんこ") != -1:
            await message.channel.send("トイレに行ってこい！(圧")
        elif mc.find("やかましいわ") != -1:
            await message.channel.send("w")
        elif mc.find("くさ") != -1 or mc.find("草") != -1 or mc.find("笑") != -1 or mc.find("www") != -1:
            await message.channel.send(random.choice(sorena_list))