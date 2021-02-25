# インストールした discord.py を読み込む
import os
import random
import subprocess
import sys

import discord

from jyanken import jyanken
from waribashi import waribashi

with open("token") as tk:
    TOKEN = tk.read().splitlines()[0]

# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    if len(sys.argv) == 2:
        with open("ID_DISCORD_CL") as f:
            channel = client.get_channel(int(f.read().splitlines()[0]))
            await channel.send("restarted. command completed.")
        os.remove("ID_DISCORD_CL")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='ひまだよーあそんでよー'))


ohayo_list = ("おはようございまーす！", "おはよう★", "おはようでございます！", "ぉは(σ。ゝω・)σYO!!", "チャオ♪(´・ω・`)ノ")
tadaima_list = ("ｵｶｴﾘ～!!ヽ(*≧ω≦)ﾉ", "ヾ(*ゝω・*)ノおかえり～", "帰って来た!?Σ(｀ω゜´*)三｡:+.゜ヽ(*′ﾟω`)ﾉﾞ｡:+.゜おかえりん")
j = jyanken()
w = waribashi()


# メッセージ受信時に動作する処理
@client.event
async def on_message(message:discord.Message):
    global jyanken_f
    mc = message.content
    if mc.find("おはよう") != -1:
        await message.channel.send(random.choice(ohayo_list))
    elif mc.find("ただいま") != -1:
        await message.channel.send(random.choice(tadaima_list))
    elif mc.split(" ")[0] == "/jyanken":
        await j.jyanken_cmd(client, message)
    # elif mc == "/waribashi":
    #     await w.waribashi_start(client, message)
    elif mc == "/restart":
        if 799842587909423146 in list(map(lambda n: n.id, message.author.roles)):
            msg = "You had the required permissions for this command.\nExecute the command.\n***The bot will be " \
                  "temporarily unavailable!***\n------------- LOG -------------\n"
            m: discord.Message = await message.channel.send(msg)
            p = subprocess.Popen(["git","pull"],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            for line in iter(p.stdout.readline, b''):
                msg += line.rstrip().decode("utf-8")+"\n"
                await m.edit(content=msg)
            msg += "------------- EXITED -------------\nrestarting..."
            await m.edit(content=msg)
            print("exit.")
            with open("ID_DISCORD_CL","w") as f:
                f.write(str(message.channel.id))
            sys.exit()
        else:
            await message.channel.send(
                "***You do not have the required permissions to execute this command. Please contact admin.***"
            )


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
