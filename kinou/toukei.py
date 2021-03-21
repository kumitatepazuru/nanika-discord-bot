import json
import os

import discord


class toukei:
    def __init__(self, client: discord.Client):
        self.toukei = None

        client.on_ready = self.on_ready
        client.on_error = self.on_error
        client.on_typing = self.on_typing
        client.on_message = self.on_message
        client.on_raw_message_delete = self.on_raw_message_delete

        if not os.path.isfile("./data/toukei.json"):
            self.save()

        with open("./data/toukei.json") as f:
            self.toukei = json.load(f)
    async def on_ready(self, *args, **kwargs):
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
        print(self.toukei)
        if self.toukei is None:
            self.toukei = {"on_ready": 0, "on_error": 0, "on_typing": 0, "on_message": 0, "on_raw_message_delete": 0,
                           "on_raw_message_edit": 0, "on_raw_reaction_add": 0, "on_raw_reaction_remove": 0,
                           "on_raw_reaction_clear": 0, "on_guild_channel_pins_update": 0}
        with open("./data/toukei.json", "w") as f:
            json.dump(self.toukei, f)
