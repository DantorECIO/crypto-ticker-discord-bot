from discord.ext import commands
from discord.ext import tasks
import discord
import pycoingecko


class TickerCog(commands.Cog, name='Ticker'):
    """Cog with the task to update the ticker"""

    def __init__(self, bot):
        self.bot = bot
        self.ticker_task.start()
        
    @tasks.loop(seconds=5)
    async def ticker_task(self):
        coingecko = pycoingecko.CoinGeckoAPI()
        prices = coingecko.get_price(ids=self.bot.config["cryptocurrency_id"], vs_currencies=self.bot.config["fiat_id"])
        history = coingecko.get_coin_market_chart_by_id(id='nano', vs_currency=[self.bot.config["fiat_id"]], days='1')
        price_usd = round(prices[self.bot.config["cryptocurrency_id"]][self.bot.config["fiat_id"]], 4)
        percentage = round(((prices[self.bot.config["cryptocurrency_id"]][self.bot.config["fiat_id"]] / history['prices'][0][1]) - 1) * 100, 2)
        difference = round(prices[self.bot.config["cryptocurrency_id"]][self.bot.config["fiat_id"]] - history['prices'][0][1], 2)
        c_name = self.bot.config["cryptocurrency_name"]
        f_name = self.bot.config["fiat_name"]
        for g in self.bot.guilds:
            await g.me.edit(nick=f"{c_name}: {f_name}{price_usd:.2f}")
        status = discord.Status.idle
        if percentage < 2:
            status = discord.Status.dnd
        elif percentage > 2:
            status = discord.Status.online
        status_string = f"+{f_name}{difference:.2f} (+{percentage:.2f}%)" if percentage >= 0 else f"-{f_name}{abs(difference):.2f} ({percentage:.2f}%)"
        await self.bot.change_presence(status=status, activity=discord.Activity(type=discord.ActivityType.watching, name=status_string))

    @ticker_task.before_loop
    async def before(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(TickerCog(bot))

