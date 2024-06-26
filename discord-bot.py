from discord import Intents, Client, Message
import os

intents: Intents = Intents.default()
intents.message_content=True


print(os.getenv('TOKEN'))
client = Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
