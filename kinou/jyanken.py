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
            say = ""
            te = ["ぐー", "ちょき", "ぱー"]
            t = random.choice(te)
            j = mc.split(" ")[1].lower()
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
                say += "**あいこ！** (もういちど、`/jyanken [p|g|c]` でじゃんけんできます。)\n"
                toexit = False
            elif t == "ぱー" and j == "p":
                say += "**あいこ！** (もういちど、`/jyanken [p|g|c]` でじゃんけんできます。)\n"
                toexit = False
            elif t == "ぱー" and j == "g":
                say += "**あなたのまけ！** (やったー！)\n"
            elif t == "ぱー" and j == "c":
                say += "**あなたのかち！** (ちょっとくやしい...)\n"

            if toexit:
                say += "じゃんけんを終了します。まったねー！"
                await client.change_presence(
                    activity=discord.Activity(type=discord.ActivityType.playing, name='ひまだよーあそんでよー'))
                self.jyanken_f = False
            await message.channel.send(say)
