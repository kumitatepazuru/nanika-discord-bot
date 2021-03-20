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

doya_list = (
    "(๑⁼̴̀д⁼̴́๑)ﾄﾞﾔｯ‼", "(๑• ̀д•́ )✧+°ﾄﾞﾔｯ", "o(`･ω´･+o) ﾄﾞﾔｧ…！", "(　-`ω-)どや！", "(●´ิ∀´ิ●)ﾄﾞﾔｧ", "( ´´ิ∀´ิ` )",
    "( ｰ̀ωｰ́ )",
    "o(`･ω´･+o) ﾄﾞﾔ", "( *｀ω´) ﾄﾞﾔｧ")
j = jyanken()
w = waribashi()
h = hannou()
o = out()


# メッセージ受信時に動作する処理
@client.event
async def on_message(message: discord.Message):
    if not message.author.bot:
        global jyanken_f
        mc = message.content
        await o.msg(message, mc)
        await h.msg(message, mc)
        if mc.split(" ")[0] == "!jyanken":
            await j.jyanken_cmd(client, message)
        # elif mc == "/waribashi":
        #     await w.waribashi_start(client, message)
        elif mc == "!restart":
            if message.author.id == 635377375739248652:
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
            if message.author.id == 635377375739248652:
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
            await keisan.keisan(client, message)
        elif mc.split(" ")[0] == "!ban":
            with open("data/ban.png", "rb") as f:
                await message.channel.send(file=discord.File(f))
                if len(mc.split(" ")) == 2:
                    client.get_user(int(mc.split(" ")[1])).send(file=discord.File(f))
        elif mc == "!usseewa":
            with open("data/usseewa.mp3", "rb") as f:
                await message.channel.send(file=discord.File(f))
        elif mc.split(" ")[0] == "!out":
            if 799842587909423146 in list(map(lambda n: n.id, message.author.roles)):
                out_msg: discord.Message = await message.channel.fetch_message(int(mc.split(" ")[1]))
                await o.send_msg(out_msg, "||" + out_msg.content + "||",
                                 ["> **運営側が違反していると考えた任意の文字列**", "> *詳しくは運営にご確認ください。*"])
            else:
                await message.channel.send("このコマンドは運営専用です!")
        elif mc == "!mac":
            with open("data/1360-Double-Cheese-Burger.png", "rb") as f:
                await message.channel.send("ダブルチーズバーガー（おいしい）",file=discord.File(f))


# @client.event
# async def on_guild_join(guild:discord.Guild):
#     await guild.create_role(name="発言禁止!!!!")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
