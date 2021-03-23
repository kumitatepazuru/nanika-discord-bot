import asyncio
import json
import logging

import discord
from discord.ext import commands


class out(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

        self.file = "./data/out.json"
        with open(self.file) as f:
            self.out = json.load(f)

    @commands.command(aliases=["o"])
    async def out(self, ctx:commands.Context, _id):
        if ctx.author.guild_permissions.administrator:
            out_msg: discord.Message = await ctx.channel.fetch_message(int(_id))
            await self.send_msg(ctx, "||" + out_msg.content + "||",
                                ["> **運営側が違反していると考えた任意の文字列**", "> *詳しくは運営にご確認ください。*"])
        else:
            await ctx.send("このコマンドは運営専用です!")

    @commands.Cog.listener(name='on_message')
    async def msg(self,message:discord.Message):
        if not message.author.bot:
            mc = message.content
            ok = False
            out_list = []
            for i in self.out["data"]:
                ok = ok or mc.find(i) != -1
                if mc.find(i) != -1:
                    out_list.append(i)
            if ok:
                for i in self.out["data"]:
                    mc = mc.replace(i, "||" + i + "||")
                ctx = await self.bot.get_context(message)
                await self.send_msg(ctx, mc, out_list)

    async def send_msg(self, ctx:commands.Context, mc, out_list):
        if self.out["player"].get(str(ctx.author.id)) is None:
            self.out["player"][str(ctx.author.id)] = 1
        else:
            self.out["player"][str(ctx.author.id)] += 1

        mc = "ポリシーに抵触しかねない単語が発言されました。\n問題のある単語はクリックで確認できます。\n" + mc
        await ctx.message.delete()
        await ctx.send(content=mc)
        await ctx.author.send(
            "今回の表現はサーバーのポリシーに抵触しかねません。発言に気をつけてください。\n今回抵触した単語\n" + "\n".join(out_list))
        await ctx.author.send(
            "この事柄はすべて記録されます。\n\n今回は、" + str(self.out["player"][str(ctx.author.id)]) + "分発言禁止になります。"
        )
        guild: discord.Guild = ctx.channel.guild
        with open("./data/out-role.json") as f:
            a = json.load(f)
            for i in a:
                r = guild.get_role(i)
                if r is not None:
                    await ctx.author.add_roles(r)
                    await asyncio.sleep(self.out["player"][str(ctx.author.id)] * 60)
                    await ctx.author.send(
                        "発言禁止が解除されました。"
                    )
                    await ctx.author.remove_roles(r)
        with open(self.file, "w") as f:
            json.dump(self.out, f)


def setup(bot):
    bot.add_cog(out(bot))
