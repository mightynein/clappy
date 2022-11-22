import os

from dotenv import load_dotenv

load_dotenv()

print(f'DISCORD_BOT_CLIENT_ID: {os.getenv("DISCORD_BOT_CLIENT_ID")}')
print(f'DISCORD_BOT_SECRET: {os.getenv("DISCORD_BOT_SECRET")}')
