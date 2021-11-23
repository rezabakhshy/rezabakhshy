import discord
import googletrans

# Create a translator object
translator = googletrans.Translator()

# The discord client
client = discord.Client()
# The token that allows client to run the script
# token = ...
token = "2136835913:AAFp2UmOaw-qdLwrGtgCni4D0JlgD2_bU4o"

# Notify on console that the discord bot is ready
@client.event
async def on_ready():
    print("The bot is ready!")


# Responds to commands
@client.event
async def on_message(message):
    # Checks that the bot is not the one who sent a message
    if message.author == client.user:
        return

    # Hello test command
    if message.content.startswith("!hello"):
        await message.channel.send("Hello! {}".format(message.author.mention))

    if message.content.lower().startswith("!c "):
        # Grab the message after the command
        msg = message.content[3:]
        # Get the language of the file
        message_destination = translator.detect(msg).lang.lower()

        if message_destination == "en":
            # Directly converts English to Chinese (Traditional)
            translated_message = translator.translate(msg, dest="fa")
            await message.channel.send("`{}` -> `{}`".format(msg, translated_message.text))
        else:
            # Translates the language and converts it to English
            translated_message = translator.translate(msg)
            await message.channel.send("`{}` -> `{}`".format(msg, translated_message.text))

client.run(token)