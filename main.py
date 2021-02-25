# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
from jyanken import jyanken
from waribashi import waribashi

TOKEN = 'ODExNzI1NDQxNzAxMjQ5MDU0.YC2YOg.dTmGJ8vOToA1zQEnEgvu39oOkoQ'

# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='ひまだよーあそんでよー'))


ohayo_list = ("おはようございまーす！", "おはよう★", "おはようでございます！", "ぉは(σ。ゝω・)σYO!!", "チャオ♪(´・ω・`)ノ")
tadaima_list = ("ｵｶｴﾘ～!!ヽ(*≧ω≦)ﾉ", "ヾ(*ゝω・*)ノおかえり～", "帰って来た!?Σ(｀ω゜´*)三｡:+.゜ヽ(*′ﾟω`)ﾉﾞ｡:+.゜おかえりん")
j = jyanken()
w = waribashi()


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global jyanken_f
    mc = message.content
    if mc.find("おはよう") != -1:
        await message.channel.send(random.choice(ohayo_list))
    elif mc.find("ただいま") != -1:
        await message.channel.send(random.choice(tadaima_list))
    elif mc.split(" ")[0] == "/jyanken":
        await j.jyanken_cmd(client, message)
    elif mc == "/waribashi":
        await w.waribashi_start(client, message)


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
