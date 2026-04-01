import discord
from discord.ext import commands
from discord import app_commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'General cog loaded')

    # Slash command example
    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! Latency: {round(self.bot.latency * 1000)}ms')

    # Slash command with parameter
    @app_commands.command(name="hello", description="Say hello to someone")
    @app_commands.describe(name="The name of the person to greet")
    async def hello(self, interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f'Hello, {name}!')

    # Regular prefix command
    @commands.command(name='info')
    async def info(self, ctx):
        """Get bot information"""
        embed = discord.Embed(
            title="Bot Information",
            description="A simple Discord bot",
            color=discord.Color.blue()
        )
        embed.add_field(name="Servers", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Users", value=len(self.bot.users), inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
