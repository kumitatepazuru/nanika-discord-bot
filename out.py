import asyncio
import json

import discord


class out:
    def __init__(self, file="./data/out.json"):
        self.file = file
        with open(file) as f:
            self.out = json.load(f)

    async def msg(self, message: discord.Message, mc: str):
        ok = False
        out_list = []
        for i in self.out["data"]:
            ok = ok or mc.find(i) != -1
            if mc.find(i) != -1:
                out_list.append(i)
        if ok:
            for i in self.out["data"]:
                mc = mc.replace(i, "||" + i + "||")
            await self.send_msg(message, mc, out_list)

    async def send_msg(self, message, mc, out_list):
        if self.out["player"].get(str(message.author.id)) is None:
            self.out["player"][str(message.author.id)] = 1
        else:
            self.out["player"][str(message.author.id)] += 1

        mc = "ポリシーに抵触しかねない単語が発言されました。\n問題のある単語はクリックで確認できます。\n" + mc
        await message.delete()
        await message.channel.send(content=mc)
        await message.author.send(
            "今回の表現はサーバーのポリシーに抵触しかねません。発言に気をつけてください。\n今回抵触した単語\n" + "\n".join(out_list))
        await message.author.send(
            "この事柄はすべて記録されます。\n\n今回は、" + str(self.out["player"][str(message.author.id)]) + "分発言禁止になります。"
        )
        guild: discord.Guild = message.channel.guild
        role = guild.get_role(820478751871729695)
        await message.author.add_roles(role)
        await asyncio.sleep(self.out["player"][str(message.author.id)] * 60)
        await message.author.send(
            "発言禁止が解除されました。"
        )
        await message.author.remove_roles(role)
        with open(self.file, "w") as f:
            json.dump(self.out, f)
