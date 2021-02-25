import random

import discord


class jyanken:
    jyanken_f = False
    jyanken_channel = None

    async def jyanken_cmd(self, client, message):
        mc = message.content
        if not self.jyanken_f:
            self.jyanken_f = True
            await message.channel.send("じゃんけんを開始します。`/jyanken [p|g|c]` でじゃんけんをしてください。\nじゃんけん...")
            await client.change_presence(activity=discord.Game(message.channel.name + " でじゃんけん"))
            self.jyanken_channel = message.channel
        elif len(mc.split(" ")) == 1:
            await message.channel.send("じゃんけんは"+message.channel.name + " ですでに開始しています。`/jyanken [p|g|c]` でじゃんけんをしてください。")
        else:
            te = ["ぐー", "ちょき", "ぱー"]
            t = random.choice(te)
            if mc.split(" ")[1] == "p":
                await message.channel.send("*あなた* > **ぱー**")
            elif mc.split(" ")[1] == "g":
                await message.channel.send("*あなた* > **ぐー**")
            else:
                await message.channel.send("*あなた* > **ちょき**")
            await message.channel.send(f"*BOT* > **{t}**")
            toexit = True

            if t == "ぐー" and mc.split(" ")[1] == "p":
                await message.channel.send("**あなたのかち！** (ちょっとくやしい...)")
            elif t == "ぐー" and mc.split(" ")[1] == "g":
                await message.channel.send("**あいこ！** (もういちど、`/jyanken [p|g|c]` でじゃんけんできます。)")
                toexit = False
            elif t == "ぐー" and mc.split(" ")[1] == "c":
                await message.channel.send("**あなたのまけ！** (やったー！)")
            elif t == "ちょき" and mc.split(" ")[1] == "p":
                await message.channel.send("**あなたのまけ！** (やったー！)")
            elif t == "ちょき" and mc.split(" ")[1] == "g":
                await message.channel.send("**あなたのかち！** (ちょっとくやしい...)")
            elif t == "ちょき" and mc.split(" ")[1] == "c":
                await message.channel.send("**あいこ！** (もういちど、`/jyanken [p|g|c]` でじゃんけんできます。)")
                toexit = False
            elif t == "ぱー" and mc.split(" ")[1] == "p":
                await message.channel.send("**あいこ！** (もういちど、`/jyanken [p|g|c]` でじゃんけんできます。)")
                toexit = False
            elif t == "ぱー" and mc.split(" ")[1] == "g":
                await message.channel.send("**あなたのまけ！** (やったー！)")
            elif t == "ぱー" and mc.split(" ")[1] == "c":
                await message.channel.send("**あなたのかち！** (ちょっとくやしい...)")

            if toexit:
                await message.channel.send("じゃんけんを終了します。まったねー！")
                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.playing, name='ひまだよーあそんでよー'))
                self.jyanken_f = False
