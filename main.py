import json
import logging
import os
import sys
import traceback

import discord
from discord.ext import commands

INITIAL_EXTENSIONS = [
    "cogs.hannou",
    "cogs.jyanken",
    "cogs.bmi",
    "cogs.help",
    "cogs.keisan",
    "cogs.out",
    "cogs.main"
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
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='v 2.1.0'
                                                                                                      '/powered by '
                                                                                                      'Riku Ueda'))
        self.toukei["on_ready"] += 1
        self.save()

    async def on_error(self, *args, **kwargs):
        self.toukei["on_error"] += 1
        self.save()

    async def on_typing(self, *args, **kwargs):
        self.toukei["on_typing"] += 1
        self.save()

    async def on_message(self, *args, **kwargs):
        self.toukei["on_message"] += 1
        self.save()

    async def on_raw_message_delete(self, *args, **kwargs):
        self.toukei["on_raw_message_delete"] += 1
        self.save()

    async def on_raw_message_edit(self, *args, **kwargs):
        self.toukei["on_raw_message_edit"] += 1
        self.save()

    async def on_raw_reaction_add(self, *args, **kwargs):
        self.toukei["on_raw_reaction_add"] += 1
        self.save()

    async def on_raw_reaction_remove(self, *args, **kwargs):
        self.toukei["on_raw_reaction_remove"] += 1
        self.save()

    async def on_raw_reaction_clear(self, *args, **kwargs):
        self.toukei["on_raw_reaction_clear"] += 1
        self.save()

    async def on_guild_channel_pins_update(self, *args, **kwargs):
        self.toukei["on_guild_channel_pins_update"] += 1
        self.save()

    def save(self):
        logging.info(self.toukei)
        if self.toukei is None:
            self.toukei = {"on_ready": 0, "on_error": 0, "on_typing": 0, "on_message": 0, "on_raw_message_delete": 0,
                           "on_raw_message_edit": 0, "on_raw_reaction_add": 0, "on_raw_reaction_remove": 0,
                           "on_raw_reaction_clear": 0, "on_guild_channel_pins_update": 0}
        with open("./data/toukei.json", "w") as f:
            json.dump(self.toukei, f)


# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    with open("token") as tk:
        TOKEN = tk.read().splitlines()[0]

    bot = main(command_prefix='!', help_command=None)  # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(TOKEN)  # Botのトークン
