import asyncio
import logging
import os
import subprocess
import sys
import traceback

import discord
from discord.ext import commands

from lib import process_output

INITIAL_EXTENSIONS = [
    "cogs.hannou",
    "cogs.jyanken",
    "cogs.bmi",
    "cogs.help",
    "cogs.keisan",
    "cogs.out"
]
logging.basicConfig(level=logging.INFO,
                    format="\033[38;5;4m%(asctime)s \033[38;5;10m[%(module)s] [%(name)s]=>L%(lineno)d "
                           "\033[38;5;14m[%(levelname)s] \033[0m%(message)s")


class main(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # 起動時に動作する処理
    async def on_ready(self):
        # 起動したらターミナルにログイン通知が表示される
        logging.info('Bot logged')
        if len(sys.argv) == 2:
            with open("ID_DISCORD_CL") as f:
                channel = self.get_channel(int(f.read().splitlines()[0]))
                await channel.send("restarted. command completed.")
            os.remove("ID_DISCORD_CL")
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='v 2.0.0'
                                                                                                      '/powered by '
                                                                                                      'Riku Ueda'))

    @commands.command(aliases=['t'])
    async def timer(self, ctx):
        await ctx.send("100回送るよ！")
        for i in range(100):
            await asyncio.sleep(60)
            await ctx.send("1分たったよ！")

    @commands.command(aliases=["s"])
    async def say(self, ctx, *args):
        await ctx.message.delete()
        await ctx.send(" ".join(args))

    @commands.command(aliases=["m"])
    async def mac(self, ctx):
        with open("data/1360-Double-Cheese-Burger.png", "rb") as f:
            await ctx.send("ダブルチーズバーガー（おいしい）", file=discord.File(f))

    @commands.command()
    async def restart(self,ctx):
        if ctx.author.id == 635377375739248652:
            msg = "You had the required permissions for this command.\nExecute the command.\n***The bot will be " \
                  "temporarily unavailable!***\n------------- LOG -------------\n"
            m: discord.Message = await ctx.send(msg)
            p = subprocess.Popen(["git", "pull"],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            msg, m = await process_output(p, m, msg, ctx)
            msg += "------------- EXITED -------------\nrestarting..."
            try:
                await m.edit(content=msg)
            except discord.errors.HTTPException:
                msg = msg.splitlines()[-1]
                await ctx.send(msg)
            print("exit.")
            with open("ID_DISCORD_CL", "w") as f:
                f.write(str(ctx.channel.id))
            sys.exit()
        else:
            await ctx.send(
                "***You do not have the required permissions to execute this command. Please contact admin.***"
            )

    @commands.command()
    async def cmd(self,ctx,*args):
        if ctx.author.id == 635377375739248652:
            msg = "You had the required permissions for this command.\nExecute the command.\n------------- LOG " \
                  "-------------\n "
            m: discord.Message = await ctx.send(msg)
            p = subprocess.Popen(args,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            msg, m = await process_output(p, m, msg, ctx)
            msg += "------------- EXITED -------------"
            await m.edit(content=msg)
        else:
            await ctx.send(
                "***You do not have the required permissions to execute this command. Please contact admin.***"
            )

    @commands.command()
    async def ban(self,ctx,*args):
        with open("data/ban.png", "rb") as f:
            await ctx.send(file=discord.File(f))
            if len(args) == 1:
                args[0].send(file=discord.File(f))

    @commands.command(aliases=['u'])
    async def usseewa(self,ctx):
        with open("data/usseewa.mp3", "rb") as f:
            await ctx.send(file=discord.File(f))
# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    with open("token") as tk:
        TOKEN = tk.read().splitlines()[0]

    bot = main(command_prefix='!', help_command=None)  # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(TOKEN)  # Botのトークン
