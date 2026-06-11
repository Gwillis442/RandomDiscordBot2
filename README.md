# RandomDiscordBot2

A Discord bot built with Python and discord.py featuring slash commands and modular cog system.

## Features

- Slash commands support
- Modular cog system for organizing commands
- General commands (ping, hello, info)
- Fun commands (roll, flip, 8ball)
- Easy to extend and customize

## Prerequisites

- Python 3.8 or higher
- A Discord Bot Token ([Get one here](https://discord.com/developers/applications))

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd RandomDiscordBot2
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
    - Create a `.env` file
    - Add your Discord bot token to the `.env` file:
     ```
     DISCORD_TOKEN=your_actual_bot_token_here
     ```
    - Configure AI backend (choose one):
       - Local Ollama (default model example):
          ```
          AI_PROVIDER=ollama
          OLLAMA_BASE_URL=http://localhost:11434/v1
          AI_MODEL=llama3.1:8b
          ```
       - OpenAI:
          ```
          AI_PROVIDER=openai
          OPENAI_API_KEY=your_openai_key
          AI_MODEL=gpt-4o-mini
          ```

5. **Run the bot**
   ```bash
   python main.py
   ```

## Project Structure

```
RandomDiscordBot2/
├── cogs/               # Command modules (cogs)
│   ├── __init__.py
│   ├── general.py      # General commands
│   └── fun.py          # Fun commands
├── utils/              # Utility functions
│   ├── __init__.py
│   └── helpers.py      # Helper functions for embeds, etc.
├── main.py             # Main bot file
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── .env                # Your actual environment variables (not tracked by git)
└── README.md           # This file
```

## Available Commands

### Slash Commands
- `/ping` - Check bot latency
- `/hello <name>` - Greet someone
- `/roll [sides]` - Roll a dice (default: 6 sides)
- `/flip` - Flip a coin
- `/8ball <question>` - Ask the magic 8-ball

### Prefix Commands
- `!info` - Get bot information

## Ollama Quick Start

1. Install Ollama from https://ollama.com/download
2. Pull a model:
   ```bash
   ollama pull llama3.1:8b
   ```
3. Start Ollama server (if not already running):
   ```bash
   ollama serve
   ```
4. Ensure your `.env` has:
   ```
   AI_PROVIDER=ollama
   OLLAMA_BASE_URL=http://localhost:11434/v1
   AI_MODEL=llama3.1:8b
   ```
5. Start the bot and use `/ask_ai`.

## Adding New Commands

To add new commands, create a new cog in the `cogs/` directory or add commands to an existing cog:

```python
import discord
from discord.ext import commands
from discord import app_commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mycommand", description="My custom command")
    async def mycommand(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

## Contributing

Feel free to submit issues and pull requests!

## License

This project is open source and available under the ISC License.