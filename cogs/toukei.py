import logging
from datetime import datetime

from discord.ext import commands, tasks


class toukei(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.Cog.listener(name='on_error')
    async def on_error(self, *args, **kwargs):
        self.bot.toukei["on_error"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_typing')
    async def on_typing(self, *args, **kwargs):
        self.bot.toukei["on_typing"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_message')
    async def on_message(self, *args, **kwargs):
        self.bot.toukei["on_message"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_raw_message_delete')
    async def on_raw_message_delete(self, *args, **kwargs):
        self.bot.toukei["on_raw_message_delete"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_raw_message_edit')
    async def on_raw_message_edit(self, *args, **kwargs):
        self.bot.toukei["on_raw_message_edit"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_raw_reaction_add')
    async def on_raw_reaction_add(self, *args, **kwargs):
        self.bot.toukei["on_raw_reaction_add"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_raw_reaction_remove')
    async def on_raw_reaction_remove(self, *args, **kwargs):
        self.bot.toukei["on_raw_reaction_remove"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_raw_reaction_clear')
    async def on_raw_reaction_clear(self, *args, **kwargs):
        self.bot.toukei["on_raw_reaction_clear"] += 1
        self.bot.save()

    @commands.Cog.listener(name='on_guild_channel_pins_update')
    async def on_guild_channel_pins_update(self, *args, **kwargs):
        self.bot.toukei["on_guild_channel_pins_update"] += 1
        self.bot.save()

    @commands.command()
    async def toukei(self, ctx):
        await ctx.send(f"""これまでの功績!!!!
botが諸事情（更新等）で起動・再起動した回数: **{self.bot.toukei['on_ready']}回**
botがバグった回数: **{self.bot.toukei['on_error']}回**
botを使用してる鯖のメンバーがタイピング中になった回数: **{self.bot.toukei['on_typing']}回**
botを使用してる鯖のメンバーがメッセージを投稿した回数: **{self.bot.toukei['on_message']}回**
botを使用してる鯖のメンバーがメッセージを削除した回数: **{self.bot.toukei['on_raw_message_delete']}回**
botを使用してる鯖のメンバーがメッセージを編集した回数: **{self.bot.toukei['on_raw_message_edit']}回**
botを使用してる鯖のメンバーがメッセージにリアクションを追加した回数: **{self.bot.toukei['on_raw_reaction_add']}回**
botを使用してる鯖のメンバーがメッセージにリアクションを削除した回数: **{self.bot.toukei['on_raw_reaction_remove']}回**
botを使用してる鯖のメンバーがメッセージにリアクションを全消去した回数: **{self.bot.toukei['on_raw_reaction_clear']}回**
botを使用してる鯖のメンバーがメッセージをピンどめした回数: **{self.bot.toukei['on_guild_channel_pins_update']}回**""")

    @tasks.loop(seconds=1)
    async def loop(self):
        now = datetime.now().strftime('%H:%M')
        if now == '00:00':
            # TODO: マルチ鯖化。
            channel = self.bot.get_channel(822303992343953432)
            if channel is not None:
                say = f"""今日の功績!!!!

botが諸事情（更新等）で起動・再起動した回数: **{self.bot.toukei['on_ready']}回**
botがバグった回数: **{self.bot.toukei['on_error']}回**
botを使用してる鯖のメンバーがタイピング中になった回数: **{self.bot.toukei['on_typing']}回**
botを使用してる鯖のメンバーがメッセージを投稿した回数: **{self.bot.toukei['on_message']}回**
botを使用してる鯖のメンバーがメッセージを削除した回数: **{self.bot.toukei['on_raw_message_delete']}回**
botを使用してる鯖のメンバーがメッセージを編集した回数: **{self.bot.toukei['on_raw_message_edit']}回**
botを使用してる鯖のメンバーがメッセージにリアクションを追加した回数: **{self.bot.toukei['on_raw_reaction_add']}回**
botを使用してる鯖のメンバーがメッセージにリアクションを削除した回数: **{self.bot.toukei['on_raw_reaction_remove']}回**
botを使用してる鯖のメンバーがメッセージにリアクションを全消去した回数: **{self.bot.toukei['on_raw_reaction_clear']}回**
botを使用してる鯖のメンバーがメッセージをピンどめした回数: **{self.bot.toukei['on_guild_channel_pins_update']}回**
"""
                await channel.send(say)
                self.bot.toukei = None


def setup(bot):
    bot.add_cog(toukei(bot))
