import discord
from discord.ext import commands
from discord import app_commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Fun cog loaded')

    @app_commands.command(name="roll", description="Roll a dice")
    @app_commands.describe(sides="Number of sides on the dice (default: 6)")
    async def roll(self, interaction: discord.Interaction, sides: int = 6):
        if sides < 1:
            await interaction.response.send_message("Please provide a valid number of sides!")
            return
        result = random.randint(1, sides)
        await interaction.response.send_message(f'🎲 You rolled a {result}!')

    @app_commands.command(name="flip", description="Flip a coin")
    async def flip(self, interaction: discord.Interaction):
        result = random.choice(['Heads', 'Tails'])
        await interaction.response.send_message(f'🪙 {result}!')

    @app_commands.command(name="8ball", description="Ask the magic 8-ball a question")
    @app_commands.describe(question="Your question for the 8-ball")
    async def eightball(self, interaction: discord.Interaction, question: str):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
            "Cannot predict now.", "Concentrate and ask again.",
            "Don't count on it.", "My reply is no.", "My sources say no.",
            "Outlook not so good.", "Very doubtful."
        ]
        await interaction.response.send_message(f'🎱 {random.choice(responses)}')

    @app_commands.command(name="ship", description="Calculate the compatibility between two names")
    @app_commands.describe(name1="First person", name2="Second person")
    async def ship(self, interaction: discord.Interaction, name1: str, name2: str):
        pair_key = ''.join(sorted([name1.strip().lower(), name2.strip().lower()]))
        seeded_rng = random.Random(pair_key)
        compatibility = seeded_rng.randint(1, 100)

        if compatibility >= 85:
            verdict = 'Soulmates detected.'
        elif compatibility >= 60:
            verdict = 'Great match.'
        elif compatibility >= 40:
            verdict = 'There is potential.'
        else:
            verdict = 'This ship may need some work.'

        await interaction.response.send_message(
            f'💘 **{name1} + {name2}** = **{compatibility}%**\n{verdict}'
        )

async def setup(bot):
    await bot.add_cog(Fun(bot))
