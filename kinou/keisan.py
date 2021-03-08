import json
import os
import random
import time

import discord


async def keisan(client: discord.client, message: discord.Message):
    embed = discord.Embed()
    embed.add_field(name="計算ゲーム(β)", value="説明しよう。このゲームはどのくらい計算が早くできるかを競うゲームなのであーる。(βなので多分バグあり)", inline=False)
    embed.add_field(name="OKボタンを押すとスタートします。", value=":x:ボタンを押すとキャンセルできます。", inline=False)
    msg: discord.Message = await message.channel.send(embed=embed)
    await msg.add_reaction("🆗")
    await msg.add_reaction("❌")
    suuzi_btn = ("0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🆗")
    time_list = []

    def check(r: discord.Reaction, user: discord.User) -> bool:
        # リアクション先のメッセージや追加された絵文字が適切かどうか判断する。
        return str(r.emoji) in ("🆗", "❌") and r.message == msg and user == message.author

    reaction, _ = await client.wait_for("reaction_add", check=check)
    if "🆗" == reaction.emoji:
        await msg.clear_reactions()
        embed.clear_fields()
        embed.add_field(name="読み込み中...", value="ちょっとまってね")
        await msg.edit(embed=embed)
        for i in suuzi_btn:
            await msg.add_reaction(i)
        embed.clear_fields()
        embed.add_field(name="3秒後に開始します！", value="下の数字ボタンで解答してください。")
        await msg.edit(embed=embed)
        time.sleep(3)
        t = time.time()

        def check_num(r: discord.Reaction, user: discord.User) -> bool:
            # リアクション先のメッセージや追加された絵文字が適切かどうか判断する。
            return str(r.emoji) in suuzi_btn and r.message == msg and user == message.author

        kekka_msg = ""
        i = 0
        j = 0
        k1 = random.randint(0, 100)
        k2 = random.randint(0, 100)
        while i < 5:
            suuzi = ""
            embed.clear_fields()
            embed.add_field(name="5問中" + str(i + 1) + "問目",
                            value="経過時間:" + str(int(sum(time_list))) + "秒\n" + str(k1) + "+" + str(k2) +
                                  "\n終わったら:OK:を選択してください。")
            if kekka_msg != "":
                embed.add_field(name="結果", value=kekka_msg, inline=True)
            await msg.edit(embed=embed)
            ok = False
            while not ok:
                reaction, _ = await client.wait_for("reaction_add", check=check_num)
                await msg.remove_reaction(reaction.emoji, message.author)
                await msg.add_reaction(reaction.emoji)
                if suuzi_btn.index(reaction.emoji) != 10:
                    suuzi += str(suuzi_btn.index(reaction.emoji))
                else:
                    ok = True
                    if int(suuzi) == k1 + k2:
                        time_list.append(time.time() - t)
                        t = time.time()
                        kekka_msg = "正解！"
                        k1 = random.randint(0, 100)
                        k2 = random.randint(0, 100)
                        i += 1
                    else:
                        time_list.append(time.time() - t)
                        kekka_msg = "はずれ...\nもういちど"
                        j += 1
        embed.clear_fields()
        if not os.path.isfile("./data/keisan_rank.json"):
            with open("./data/keisan_rank.json", "w") as f:
                f.write("[]")
        with open("./data/keisan_rank.json") as f:
            d = json.load(f)
        d.append(sum(time_list))
        embed.add_field(name="総合結果！", value=str(i) + "問中" + str(i - j) + "問正解" + str(j) + "問はずれ！\n時間:" + str(
            int(sum(time_list))) + "秒!")
        embed.add_field(name="ランキング", value=str(sorted(d).index(sum(time_list))+1) + "位!\n1位を目指して頑張ろう！")
        await msg.edit(embed=embed)
        await msg.clear_reactions()
        with open("./data/keisan_rank.json", "w") as f:
            f.write(json.dumps(sorted(d)))
    else:
        embed.clear_fields()
        embed.add_field(name="キャンセルされました", value="終了します。")
        await msg.edit(embed=embed)
        await msg.clear_reactions()
