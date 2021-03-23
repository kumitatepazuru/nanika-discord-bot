import asyncio
import logging
import subprocess
import sys

import discord
from discord.ext import commands

from lib import process_output


class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

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
    async def restart(self, ctx):
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
            self.logger.info("exit.")
            with open("ID_DISCORD_CL", "w") as f:
                f.write(str(ctx.channel.id))
            sys.exit()
        else:
            await ctx.send(
                "***You do not have the required permissions to execute this command. Please contact admin.***"
            )

    @commands.command()
    async def cmd(self, ctx, *args):
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
    async def ban(self, ctx, *args):
        with open("data/ban.png", "rb") as f:
            await ctx.send(file=discord.File(f))
            if len(args) == 1:
                args[0].send(file=discord.File(f))

    @commands.command(aliases=['u'])
    async def usseewa(self, ctx):
        with open("data/usseewa.mp3", "rb") as f:
            await ctx.send(file=discord.File(f))