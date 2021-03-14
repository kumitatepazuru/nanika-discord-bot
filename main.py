# インストールした discord.py を読み込む
import os
import random
import subprocess
import sys

import discord

from hannou import hannou
from kinou import keisan
from kinou.bmi import bmi
from kinou.help import help
from kinou.jyanken import jyanken
from kinou.waribashi import waribashi
from out import out

with open("token") as tk:
    TOKEN = tk.read().splitlines()[0]

# 接続に必要なオブジェクトを生成
client = discord.Client()


async def process_output(p, m, msg, message):
    for line in iter(p.stdout.readline, b''):
        msg += line.rstrip().decode("utf-8") + "\n"
        try:
            await m.edit(content=msg)
        except discord.errors.HTTPException:
            msg = msg.splitlines()[-1]
            m = await message.channel.send(msg)
    return msg, m


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
doya_list = (
    "(๑⁼̴̀д⁼̴́๑)ﾄﾞﾔｯ‼", "(๑• ̀д•́ )✧+°ﾄﾞﾔｯ", "o(`･ω´･+o) ﾄﾞﾔｧ…！", "(　-`ω-)どや！", "(●´ิ∀´ิ●)ﾄﾞﾔｧ", "( ´´ิ∀´ิ` )",
    "( ｰ̀ωｰ́ )",
    "o(`･ω´･+o) ﾄﾞﾔ", "( *｀ω´) ﾄﾞﾔｧ")
sorena_list = (
    '(╭☞• ⍛• )╭☞それな', '(╭☞•́∀•̀)╭☞\u3000それな！', '(╭☞•́•̀)╭☞', '(╭☞•́ﾛ•̀)╭☞', '(☞◑ω◑)☞', '( ﾐΦﻌΦ)╭☞', '(╭☞’ω’)╭☞',
    '☜（ﾟ∀ﾟ☜）',
    'σﾟﾛﾟ)σ', '(´ー`)σ', '(σ･ω･)σ', '(σ≧∀≦)σ', '(つ >ω●)つ', 'σﾟﾛﾟ)σソレナ', '(´ー`)σソレナ', '(σ･ω･)σソレナ', '(σ≧∀≦)σソレナ',
    '(σﾟ∀ﾟ)σソレナ', '(σ*’3`)σソレナ')
j = jyanken()
w = waribashi()
h = hannou()
o = out()

# メッセージ受信時に動作する処理
@client.event
async def on_message(message: discord.Message):
    global jyanken_f
    mc = message.content
    await o.msg(message, mc)
    await h.msg(message, mc)
    if mc.split(" ")[0] == "!jyanken":
        await j.jyanken_cmd(client, message)
    # elif mc == "/waribashi":
    #     await w.waribashi_start(client, message)
    elif mc == "!restart":
        if 799842587909423146 in list(map(lambda n: n.id, message.author.roles)):
            msg = "You had the required permissions for this command.\nExecute the command.\n***The bot will be " \
                  "temporarily unavailable!***\n------------- LOG -------------\n"
            m: discord.Message = await message.channel.send(msg)
            p = subprocess.Popen(["git", "pull"],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            msg, m = await process_output(p, m, msg, message)
            msg += "------------- EXITED -------------\nrestarting..."
            try:
                await m.edit(content=msg)
            except discord.errors.HTTPException:
                msg = msg.splitlines()[-1]
                await message.channel.send(msg)
            print("exit.")
            with open("ID_DISCORD_CL", "w") as f:
                f.write(str(message.channel.id))
            sys.exit()
        else:
            await message.channel.send(
                "***You do not have the required permissions to execute this command. Please contact admin.***"
            )
    elif mc == "!doya":
        await message.channel.send(random.choice(doya_list))
    elif mc.split(" ")[0] == "!cmd":
        if 799842587909423146 in list(map(lambda n: n.id, message.author.roles)):
            msg = "You had the required permissions for this command.\nExecute the command.\n------------- LOG " \
                  "-------------\n "
            m: discord.Message = await message.channel.send(msg)
            p = subprocess.Popen(mc.split(" ")[1:],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            msg, m = await process_output(p, m, msg, message)
            msg += "------------- EXITED -------------"
            await m.edit(content=msg)
        else:
            await message.channel.send(
                "***You do not have the required permissions to execute this command. Please contact admin.***"
            )
    elif mc == "!help":
        await help(message)
    elif mc.split(" ")[0] == "!bmi":
        await bmi(mc, message)
    elif mc == "!keisan":
        await keisan.keisan(client,message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
