import csv
import logging

import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

        data = csv.reader(open("./data/help-kinou.csv"))
        data2 = csv.reader(open("./data/help-hannou.csv"))
        self.l1 = [row for row in data]
        self.l2 = [row for row in data2]
        logging.info(f"kinou data:{self.l1}")
        logging.info(f"hannou data:{self.l2}")

    @commands.command(aliases=['h'])
    async def help(self, ctx):
        embed = discord.Embed()
        embed.add_field(name="こんにちは！ @discordを快適ライフに です！", value="このbotは多機能botと呼ばれ、いろんなことができます。\nほしい機能等は #普通のチャット で。",
                        inline=False)
        embed.add_field(name="コマンド機能", value="そのままんまです。ミニゲームとかできます。", inline=False)
        for i in self.l1:
            embed.add_field(name=i[0] + " (" + i[2] + ")", value=i[1], inline=True)
        embed.add_field(name="特定の単語に反応する機能", value="そのままんまです。下ネタとか好きなのでよく反応します。", inline=False)
        for i in self.l2:
            embed.add_field(name=i[0], value=i[1], inline=True)
        embed.add_field(name="作成者", value="Create by Riku Ueda\nhttps://github.com/kumitatepazuru/", inline=False)
        embed.add_field(name="ソースコード", value="https://github.com/kumitatepazuru/nanika-discord-bot/", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))
