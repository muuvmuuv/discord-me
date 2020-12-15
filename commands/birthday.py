import logging
import dateparser

from discord.ext import commands
from discord.ext.commands import Bot, Context, Cog


class Birthday(Cog):
    """
    Save a users birthday and provide function to interact with it.
    """

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.group(name="birthday", invoke_without_command=True)
    async def group(self, ctx: Context):
        await ctx.send_help(self.qualified_name)

    @group.command(name="set")
    async def cmd_set(self, ctx: Context, *, date: str):
        """
        Define your birthday.

        Example:
        ```txt
          birthday set 13.06.1996
        ```
        """

        birthday = dateparser.parse(date, settings={"STRICT_PARSING": True})

        if birthday is None:
            await ctx.send("This is not a valid date")
            return

        logging.info(f"{ctx.author} birthday is on {birthday.isoformat()}")

        await ctx.send(
            "Cool we now know your birthday to and can send you cool stuff when it happens."
        )


def setup(bot: Bot):
    bot.add_cog(Birthday(bot))
