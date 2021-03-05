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
    elif mc == "/doya":
        await message.channel.send("o(`･ω´･+o) ﾄﾞﾔ")
    elif mc.find("どやぁ") != -1 or mc.find("どやあ") != -1 or mc.find("どや") != -1 or mc.find("どやどや") != -1:
        await message.channel.send("wwwwwwwwwwwwwwwwwwwww")
    elif mc.find("うんち") != -1 or mc.find("うんこ") != -1:
        await message.channel.send("トイレに行ってこい！(圧")
    elif mc.split(" ")[0] == "/cmd":
        if 799842587909423146 in list(map(lambda n: n.id, message.author.roles)):
            msg = "You had the required permissions for this command.\nExecute the command.\n------------- LOG -------------\n"
            m: discord.Message = await message.channel.send(msg)
            p = subprocess.Popen(mc.split(" ")[1:],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            for line in iter(p.stdout.readline, b''):
                msg += line.rstrip().decode("utf-8")+"\n"
                await m.edit(content=msg)
            msg += "------------- EXITED -------------"
            await m.edit(content=msg)
        else:
            await message.channel.send(
                "***You do not have the required permissions to execute this command. Please contact admin.***"
            )
    elif mc == "/help":
        pass
    elif mc.split(" ")[0] == "/bmi":
        if len(mc.split(" ")) != 3:
            await message.channel.send("BMI変換\n体重と身長からBMIを測定してくれます。\n/bmi [体重] [身長]")
        else:
            bmi = int(float(mc.split(" ")[1])/(float(mc.split(" ")[2])**2)*100.0)/100.0
            say = "あなたのBMI: "
            say += bmi
            say += "\n***日本肥満学会の判断基準的には...***\n"
            if bmi < 18.5:
                say += "やせすぎ！ちび！\n*低体重（痩せ型）*"
            elif bmi < 25:
                say += "チェッ。普通かよ。面白くねえなぁ\n*普通体重*"
            elif bmi < 30:
                say += "ん？デブ？ああ、熊木と一緒か。\n肥満（1度）"
            elif bmi < 35:
                say += "こんにちはデブ！（圧\n肥満（2度）"
            elif bmi < 40:
                say += "お前絶対モテないぞ\n肥満（3度）"
            else:
                say += "一生独身でいるつもりか？？\n肥満（4度）"
            say += "\n***WHOの判断基準的には...***\n"
            if bmi <= 16:
                say += "ほっっそ。スケルトンやん。\n*痩せすぎ*"
            elif bmi <= 16.99:
                say += "やせてんなぁ\n*痩せ*"
            elif bmi <= 18.49:
                say += "ん？普通？\n*痩せぎみ*"
            elif bmi <= 24.99:
                if bmi <= 25.00:
                    say += "チェッ。普通かよ。面白くねえなぁ\n*普通体重*"
                else:
                    say += "多分普通？おもしろくねえなぁ\n*前肥満*"
            elif bmi <= 34.99:
                say += "ん？デブ？気のせいか。\n肥満（1度）"
            elif bmi <= 39.99:
                say += "ふとってんなぁ。\n肥満（2度）"
            else:
                say += "一生独身でいるつもりか？？\n肥満（3度）"
            say += "\nBMI22を目指して頑張ろう！\n差分:"
            say += 22-bmi


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
