import json
import random
import logging

import discord
from discord.ext import commands  # Bot Commands Frameworkのインポート


class hannou(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

        with open("./data/hannou.json") as f:
            self.hannou_list = json.load(f)
        self.doya_list = (
            "(๑⁼̴̀д⁼̴́๑)ﾄﾞﾔｯ‼", "(๑• ̀д•́ )✧+°ﾄﾞﾔｯ", "o(`･ω´･+o) ﾄﾞﾔｧ…！", "(　-`ω-)どや！", "(●´ิ∀´ิ●)ﾄﾞﾔｧ", "( ´´ิ∀´ิ` )",
            "( ｰ̀ωｰ́ )",
            "o(`･ω´･+o) ﾄﾞﾔ", "( *｀ω´) ﾄﾞﾔｧ")

    @commands.Cog.listener(name='on_message')
    async def msg(self, message: discord.Message):
        mc = message.content
        if not message.author.bot:
            if mc.find("おはよう") != -1:
                self.logger.info("message found おはよう message: "+mc)
                await message.channel.send(random.choice(self.hannou_list["ohayo_list"]))
            elif mc.find("ただいま") != -1:
                self.logger.info("message found ただいま message: " + mc)
                await message.channel.send(random.choice(self.hannou_list["tadaima_list"]))
            elif mc.find("どやぁ") != -1 or mc.find("どやあ") != -1 or mc.find("どや") != -1 or mc.find("どやどや") != -1:
                self.logger.info("message found どやぁ,どやあ,どや,どやどや message: " + mc)
                await message.channel.send("wwwwwwwwwwwwwwwwwwwww")
            elif mc.find("うんち") != -1 or mc.find("うんこ") != -1:
                self.logger.info("message found うんち,うんこ message: " + mc)
                await message.channel.send("トイレに行ってこい！(圧")
            elif mc.find("やかましいわ") != -1:
                self.logger.info("message found やかましいわ message: " + mc)
                await message.channel.send("w")
            elif mc.find("くさ") != -1 or mc.find("草") != -1 or mc.find("笑") != -1 or mc.find("www") != -1:
                self.logger.info("message found くさ,草,笑,www message: " + mc)
                await message.channel.send(random.choice(self.hannou_list["sorena_list"]))
            elif mc.find("やりますねぇ！！") != -1 or mc.find("やりますねぇ！") != -1:
                self.logger.info("message found やりますねぇ！！,やりますねぇ！ message: " + mc)
                await message.channel.send(random.choice(self.doya_list))
            elif mc.find("エーミール") != -1:
                self.logger.info("message found エーミール message: " + mc)
                with open("./data/a615b4ca.jpg", "rb") as f:
                    await message.channel.send("エーミール（我々だ）", file=discord.File(f))
            elif message.author.id == 159985870458322944:
                if message.content.find("you just advanced to ") != -1:
                    await message.channel.send("おしゃべりレベル" + message.content.split(" ")[-1][:-1] + "!!!")

    @commands.command(aliases=["d"])
    async def doya(self,ctx):
        ctx.send(random.choice(self.doya_list))


def setup(bot):
    bot.add_cog(hannou(bot))
