import os
import logging

from pathlib import Path
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

BOT_PREFIX = "&"  # do not set this to `#` or `/`
BOT_COMMANDS = [
    "commands.birthday",
    "commands.games",
]


class DiscordMe(Bot):
    def __init__(self):
        super().__init__(command_prefix=BOT_PREFIX, description="description")

        for command in BOT_COMMANDS:
            try:
                self.load_extension(command)
            except Exception as error:
                logging.error(error)

    async def on_ready(self):
        logging.info("Connected to the following guilds:")
        for guild in self.guilds:
            # async update those in the db for analytics
            logging.info(f"- {guild.name} ({guild.id})")

    async def close(self):
        await super().close()
        # close db etc.


def main():
    Path("./logs").mkdir(exist_ok=True)

    logging.basicConfig(
        format="%(asctime)s [%(levelname)s] (%(name)s:%(lineno)d) %(message)s",
        # filename="logs/default.log",
        encoding="utf-8",
        level=logging.INFO,
    )

    logging.info('Starting "Discord Me"...')

    bot = DiscordMe()
    bot.run(DISCORD_TOKEN, reconnect=True)


if __name__ == "__main__":
    main()
