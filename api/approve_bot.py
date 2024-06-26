import threading

import discord
from discord.ext import commands

from api.models.base import db
from api.models.models import ReactionLink, Quote

TOKEN = ''

CHANNEL_ID = 1255253103918190687
BOT_ID = 1255251185817096324

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)


async def trigger_approval_request(quote, instance_id):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title=f"Quote ID: {quote.id};Instance ID: {instance_id}",
            description=quote.quote,
            color=discord.Color.blue()
        )
        message = await channel.send(embed=embed)

        db.session.add(ReactionLink(discord_message_id=message.id, quote_id=quote.id, quote=quote))

        db.session.commit()

        await message.add_reaction("✅")
        await message.add_reaction("❌")


@bot.event
async def on_reaction_add(reaction, user):
    if not user.id == BOT_ID:
        reaction_link = ReactionLink.query.filter(ReactionLink.discord_message_id == reaction.message.id).first()

        print(reaction_link)

        if reaction_link:
            db.session.delete(reaction_link.quote)

            if str(reaction.emoji) == "✅":
                reaction_link.quote.approved = True
                await reaction.message.delete()

            if str(reaction.emoji == "❌"):
                await reaction.message.delete()

            db.session.commit()


async def trigger_function(message, user):
    # Your custom function here
    await message.channel.send(f'{user.mention} reacted with 👍!')


def run_bot():
    bot.run(TOKEN)

bot_thread = threading.Thread(target=run_bot)
bot_thread.start()
