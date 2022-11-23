import os















import discord
from dotenv import load_dotenv

load_dotenv()


class Client(discord.Client):
    async def on_ready(self):
        print(f"logged in as {self.user}")

    async def on_message(self, message):
        print(f"message fromm {message.author}: {message.content}")


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

token = os.getenv("DISCORD_BOT_TOKEN", "")

client.run(token)
