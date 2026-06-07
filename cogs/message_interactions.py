import discord
from discord.ext import commands
from utils.helpers import random_number
import logging

logger = logging.getLogger(__name__)


class MessageInteractions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        # Starter keyword triggers. Expand this mapping as needed.
        self.keyword_responses = {
            "good bot": "Thanks. I am doing my best.",
            "hello bot": "Hello. Use /help-style commands to explore what I can do.",
        }

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info('MessageInteractions cog loaded')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Ignore messages from bots (including this bot) to avoid loops.
        if message.author.bot:
            return

        # Optional: limit passive interactions to servers only.
        if message.guild is None:
            return

        # Let prefix commands pass through untouched.
        if message.content.startswith("!"):
            return

        content = message.content.strip().lower()

        # Exact-match keyword triggers.
        if content in self.keyword_responses:
            await message.channel.send(self.keyword_responses[content])
            return
        

        # Mention trigger example.
        if self.bot.user and self.bot.user in message.mentions:
            await message.reply(
                "Need something? Try /ping, /hello, or /ask_ai.",
                mention_author=False,
            )

        # Fun random number trigger.
        if random_number(0, 100) == 0:  # 1% chance to trigger on any message
            await message.add_reaction("👍")
            await message.add_reaction("👎")

async def setup(bot: commands.Bot):
    await bot.add_cog(MessageInteractions(bot))
