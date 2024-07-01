import threading

import discord
from discord.ext import commands

from api.models.base import db
from api.models.models import ReactionLink, Quote, Teacher

TOKEN = ''

APPROVE_CHANNEL_ID = 1255505224274153503
BOT_ID = 1255251185817096324

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

app_context = None


def init_approve_bot(ctx):
    global app_context
    app_context = ctx
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()


async def trigger_approval_request(quote_id, quote_string, instance_id):
    channel = bot.get_channel(APPROVE_CHANNEL_ID)
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
async def on_ready():
    await bot.tree.sync()


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


@bot.tree.command(name="new_teacher")
async def new_teacher(interaction: discord.Interaction, teacher_name: str):
    with app_context:
        try:
            teacher = Teacher(name=teacher_name)

            db.session.add(teacher)
            db.session.commit()

            await interaction.response.send_message(f"Successfully added the '{teacher_name}'! Teacher ID: {teacher.id}")

        except Exception as e:
            await interaction.response.send_message(f"Failed to create teacher")


def run_bot():
    bot.run(TOKEN)
