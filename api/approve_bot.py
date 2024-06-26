import threading

import discord
from discord.ext import commands

from api.models.base import db
from api.models.models import ReactionLink, Quote

TOKEN = ''

CHANNEL_ID = 1255505224274153503
BOT_ID = 1255251185817096324

intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

app_context = None


def init_approve_bot(ctx):
    global app_context
    app_context = ctx
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()


async def trigger_approval_request(quote_id, quote_string, instance_id):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title=f"Quote ID: {quote_id};Instance ID: {instance_id}",
            description=quote_string,
            color=discord.Color.blue()
        )
        message = await channel.send(embed=embed)

        db.session.add(ReactionLink(discord_message_id=message.id, quote_id=quote_id))
        db.session.commit()

        await message.add_reaction("✅")
        await message.add_reaction("❌")


@bot.event
async def on_reaction_add(reaction, user):
    if not user.id == BOT_ID:
        with app_context:
            reaction_link = db.session.query(ReactionLink).filter(
                ReactionLink.discord_message_id == reaction.message.id).first()

            if reaction_link:
                try:
                    if str(reaction.emoji) == "✅":
                        reaction_link.quote.approved = 1
                        await reaction.message.delete()

                    if str(reaction.emoji == "❌"):
                        await reaction.message.delete()

                except discord.errors.NotFound:
                    pass

                db.session.delete(reaction_link)

                db.session.commit()


async def trigger_function(message, user):
    # Your custom function here
    await message.channel.send(f'{user.mention} reacted with 👍!')


def run_bot():
    bot.run(TOKEN)



