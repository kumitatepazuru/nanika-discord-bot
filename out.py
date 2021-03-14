import json

import discord


class out:
    def __init__(self, file="./data/out.json"):
        with open(file) as f:
            self.out_list = json.load(f)

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
            mc = "ポリシーに抵触しかねない単語が発言されました。\n問題のある単語はクリックで確認できます。\n" + mc
            await message.delete()
            await message.channel.send(content=mc)
            await message.author.send(
                "今回の表現はサーバーのポリシーに抵触しかねません。発言に気をつけてください。\n今回抵触した単語\n" + "\n".join(out_list) + "\n\n"
                                                                                             "この事柄はすべて記録されます。")
