import logging
import random

from discord.ext import commands


class jyanken(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

        self.jyanken_f = []

    @commands.command(aliases=['j'])
    async def jyanken(self, ctx: commands.Context, *t_):
        if ctx.author.id not in self.jyanken_f:
            self.jyanken_f.append(ctx.author.id)
            self.logger.info("start jyanken")
            await ctx.send("じゃんけんを開始します。`!jyanken [p|g|c]` でじゃんけんをしてください。\nじゃんけん...")
        elif len(t_) == 0:
            await ctx.channel.send("じゃんけんは `" + ctx.channel.name + "` ですでに開始しています。`!jyanken [p|g|c]` でじゃんけんをしてください。")
        else:
            say = ""
            te = ["ぐー", "ちょき", "ぱー"]
            t = random.choice(te)
            j = t_[0].lower()
            if j == "p":
                say += "*あなた* > **ぱー**\n"
            elif j == "g":
                say += "*あなた* > **ぐー**\n"
            else:
                say += "*あなた* > **ちょき**\n"
            say += f"*BOT* > **{t}**\n"
            toexit = True

            if t == "ぐー" and j == "p":
                say += "**あなたのかち！** (ちょっとくやしい...)\n"
            elif t == "ぐー" and j == "g":
                say += "**あいこ！** (もういちど、`/jyanken [p|g|c]` でじゃんけんできます。)\n"
                toexit = False
            elif t == "ぐー" and j == "c":
                say += "**あなたのまけ！** (やったー！)\n"
            elif t == "ちょき" and j == "p":
                say += "**あなたのまけ！** (やったー！)\n"
            elif t == "ちょき" and j == "g":
                say += "**あなたのかち！** (ちょっとくやしい...)\n"
            elif t == "ちょき" and j == "c":
                say += "**あいこ！** (もういちど、`!jyanken [p|g|c]` でじゃんけんできます。)\n"
                toexit = False
            elif t == "ぱー" and j == "p":
                say += "**あいこ！** (もういちど、`!jyanken [p|g|c]` でじゃんけんできます。)\n"
                toexit = False
            elif t == "ぱー" and j == "g":
                say += "**あなたのまけ！** (やったー！)\n"
            elif t == "ぱー" and j == "c":
                say += "**あなたのかち！** (ちょっとくやしい...)\n"

            if toexit:
                self.logger.info("end jyanken")
                say += "じゃんけんを終了します。まったねー！"
                self.jyanken_f.remove(ctx.author.id)
            else:
                self.logger.info("it 'aiko' jyanken")
            await ctx.send(say)


def setup(bot):
    bot.add_cog(jyanken(bot))
