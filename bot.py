import discord
from discord import app_commands
import os
import random
from dotenv import load_dotenv

__version__ = "1.0.0"

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SLUG_ROLE_ID = int(os.getenv("SLUG_ROLE_ID"))
GUILD_ID = os.getenv("GUILD_ID")

with open("slugwords.txt", "r") as f:
    SLUG_WORDS = [line.strip() for line in f if line.strip()]


class SlugBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.messages = True
        intents.members = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        else:
            await self.tree.sync()


client = SlugBot()


@client.event
async def on_ready():
    for guild in client.guilds:
        role = guild.get_role(SLUG_ROLE_ID)
        if role is None:
            continue
        for member in role.members:
            await member.remove_roles(role)
    print(f"Ready. Cleared slug role on startup.")


@client.tree.command(name="slugmode", description="Toggle slug mode for yourself")
@app_commands.describe(mode="Turn slug mode on or off")
@app_commands.choices(
    mode=[
        app_commands.Choice(name="on", value="on"),
        app_commands.Choice(name="off", value="off"),
    ]
)
async def slugmode(interaction: discord.Interaction, mode: str):
    role = interaction.guild.get_role(SLUG_ROLE_ID)
    if role is None:
        await interaction.response.send_message("Slug role not found. Check SLUG_ROLE_ID.", ephemeral=True)
        return

    if mode == "on":
        await interaction.user.add_roles(role)
        await interaction.response.send_message(":snail: Slug mode activated. You are now a slug.", ephemeral=True)
    else:
        await interaction.user.remove_roles(role)
        await interaction.response.send_message(":snail: Slug mode deactivated. You are no longer a slug.", ephemeral=True)


@client.event
async def on_message(message: discord.Message):
    if message.author.bot or message.guild is None:
        return

    role = message.guild.get_role(SLUG_ROLE_ID)
    if role is None or role not in message.author.roles:
        return

    original = message.content
    slug_words = f"{random.choice(SLUG_WORDS)} {random.choice(SLUG_WORDS)}"

    try:
        await message.delete()
    except discord.Forbidden:
        return

    if len(original) > 249:
        text = f":snail: {message.author.mention} is a slug. They said: {slug_words}.\nToo much yapping to translate"
    else:
        text = f":snail: {message.author.mention} is a slug. They said: {slug_words}.\nThis translates to: {original}"

    await message.channel.send(text)


client.run(TOKEN)
