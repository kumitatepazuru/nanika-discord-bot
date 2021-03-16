import json

import discord


class out:
    def __init__(self, file="./data/out.json"):
        with open(file) as f:
            out = json.load(f)
        self.out_list = out["data"]
        self.out_player:dict = out["player"]

    async def msg(self, message: discord.Message, mc: str):
        ok = False
        out_list = []
        for i in self.out_list:
            ok = ok or mc.find(i) != -1
            if mc.find(i) != -1:
                out_list.append(i)
        if ok and not message.author.bot:
            for i in self.out_list:
                mc = mc.replace(i, "||" + i + "||")
            await self.send_msg(message, mc, out_list)

    async def send_msg(self,message,mc,out_list):
        mc = "ポリシーに抵触しかねない単語が発言されました。\n問題のある単語はクリックで確認できます。\n" + mc
        await message.delete()
        await message.channel.send(content=mc)
        await message.author.send(
            "今回の表現はサーバーのポリシーに抵触しかねません。発言に気をつけてください。\n今回抵触した単語\n" + "\n".join(out_list) + "\n\n"
                                                                                         "この事柄はすべて記録されます。")
        if self.out_player.get(message.author.id) is None:
            self.out_player[message.author.id] = 1
        else:
            self.out_player[message.author.id] += 1
