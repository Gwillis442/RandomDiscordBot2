import discord
from discord.ext import commands
import os
import sys
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def configure_logging() -> None:
    log_level_name = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_level = getattr(logging, log_level_name, logging.INFO)

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        stream=sys.stdout,
        force=True,
    )

    # Keep discord internals quieter by default while preserving bot-level logs.
    logging.getLogger('discord').setLevel(logging.INFO)
    logging.getLogger('discord.http').setLevel(logging.WARNING)


configure_logging()
logger = logging.getLogger(__name__)

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    logger.info('%s has connected to Discord', bot.user)
    logger.info('Bot is in %s guilds', len(bot.guilds))
    try:
        synced = await bot.tree.sync()
        logger.info('Synced %s command(s)', len(synced))
    except Exception:
        logger.exception('Failed to sync commands')

# Load cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                logger.info('Loaded cog: %s', filename)
            except Exception:
                logger.exception('Failed to load cog %s', filename)

# Main function
async def main():
    token = os.getenv('DISCORD_TOKEN') or os.getenv('discord_token')
    if not token:
        raise RuntimeError('Missing Discord token. Set DISCORD_TOKEN or discord_token in the environment.')

    async with bot:
        await load_cogs()
        await bot.start(token)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
