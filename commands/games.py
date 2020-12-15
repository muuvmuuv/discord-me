import logging

from discord.ext import commands
from discord.ext.commands import Bot, Context, Cog
from services.igdb import IGDBService


class Games(Cog):
    """
    Save a users favorite game he plays.
    """

    def __init__(self, bot: Bot):
        self.bot = bot
        self.igdbService = IGDBService()

    @commands.group(name="games", invoke_without_command=True)
    async def group(self, ctx: Context):
        await ctx.send_help(self.qualified_name)

    @group.command(name="search")
    async def cmd_search_game(self, ctx: Context, *, query: str):
        """
        Search for a game using IGDB database.

        Example:
        ```txt
          games search counter strike
        ```
        """

        results = self.igdbService.search(query)
        games = self.igdbService.games([i["game"] for i in results if "game" in i])

        print(games)

        await ctx.send("here are games")


def setup(bot: Bot):
    bot.add_cog(Games(bot))
