# BMIを計算(体重[kg], 身長[m])
import logging

from discord.ext import commands


def calc_bmi(weight, height):
    return round(weight / (height ** 2))


class bmi(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.command(aliases=['b'])
    async def bmi(self, ctx, *args):
        if len(args) != 2:
            await ctx.send("BMI変換\n体重と身長からBMIを測定してくれます。\n!bmi [体重] [身長]")
        else:
            bmi_math = calc_bmi(float(args[0]), float(args[1]) / 100.0)
            say = "あなたのBMI: "
            say += str(bmi_math)
            say += "\n***日本肥満学会の判断基準的には...***\n"
            if bmi_math < 18.5:
                say += "やせすぎ！ちび！\n*低体重（痩せ型）*"
            elif bmi_math < 25:
                say += "チェッ。普通かよ。面白くねえなぁ\n*普通体重*"
            elif bmi_math < 30:
                say += "ん？デブ？\n肥満（1度）"
            elif bmi_math < 35:
                say += "こんにちはデブ！（圧\n肥満（2度）"
            elif bmi_math < 40:
                say += "お前絶対モテないぞ\n肥満（3度）"
            else:
                say += "一生独身でいるつもりか？？\n肥満（4度）"
            say += "\n***WHOの判断基準的には...***\n"
            if bmi_math <= 16:
                say += "ほっっそ。スケルトンやん。\n*痩せすぎ*"
            elif bmi_math <= 16.99:
                say += "やせてんなぁ\n*痩せ*"
            elif bmi_math <= 18.49:
                say += "ん？普通？\n*痩せぎみ*"
            elif bmi_math <= 24.99:
                if bmi_math <= 25.00:
                    say += "チェッ。普通かよ。面白くねえなぁ\n*普通体重*"
                else:
                    say += "多分普通？おもしろくねえなぁ\n*前肥満*"
            elif bmi_math <= 34.99:
                say += "ん？デブ？気のせいか。\n肥満（1度）"
            elif bmi_math <= 39.99:
                say += "ふとってんなぁ。\n肥満（2度）"
            else:
                say += "一生独身でいるつもりか？？\n肥満（3度）"
            say += "\nBMI22を目指して頑張ろう！\n差分:"
            say += str(22 - bmi_math)
            self.logger.info("run bmi command. msg:" + say)
            await ctx.send(say)


def setup(bot):
    bot.add_cog(bmi(bot))
