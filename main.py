import os
import discord
from discord.ext import commands
from discord import app_commands
import praw
import random
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Get your server (guild) ID from env
GUILD_ID = discord.Object(id=int(os.getenv("GUILD_ID")))


# Load prompts from prompts.txt
def load_prompts(path):
    prompts = {}
    current_key = None
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()
            if line.startswith("===") and line.endswith("==="):
                current_key = line.strip("=").strip()
                prompts[current_key] = ""
            elif current_key:
                prompts[current_key] += line + "\n"
    return {k: v.strip() for k, v in prompts.items()}


PROMPTS = load_prompts("prompts.txt")

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# Reddit setup
reddit = praw.Reddit(client_id=os.getenv("REDDIT_CLIENT_ID"),
                     client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                     user_agent='aita-game-bot')

# Memory for last post per user
last_post = {}


# Function to summarize comments with OpenAI
def get_top_comments_summary(post_id):
    submission = reddit.submission(id=post_id)
    submission.comments.replace_more(limit=0)
    top_comments = [
        comment.body for comment in submission.comments[:10]
        if len(comment.body) < 1000
    ]

    prompt = PROMPTS["AITA_COMMENT_SUMMARY_PROMPT"].format(
        comments="\n\n".join(f"- {c}" for c in top_comments))

    response = openai.chat.completions.create(model="gpt-4.1-nano",
                                              messages=[{
                                                  "role": "user",
                                                  "content": prompt
                                              }],
                                              max_tokens=400)

    return response.choices[0].message.content


@bot.event
async def on_ready():
    synced = await tree.sync(guild=GUILD_ID)
    print(f"✅ Synced {len(synced)} commands to guild {GUILD_ID.id}")
    print(f"🤖 Logged in as {bot.user}")


@tree.command(name="aita",
              description="Get a random AITA post",
              guild=GUILD_ID)
async def aita(interaction: discord.Interaction):
    submissions = reddit.subreddit('AmItheAsshole').hot(limit=50)
    posts = [
        post for post in submissions if not post.stickied
        and len(post.selftext) > 100 and len(post.selftext) < 5000
    ]
    post = random.choice(posts)

    # Remove "EDIT"/"UPDATE" sections
    original_text = post.selftext.split("EDIT")[0].split("Update")[0].strip()

    # Chunk post into ~1000 character segments
    chunk_size = 1000
    chunks = [
        original_text[i:i + chunk_size]
        for i in range(0, len(original_text), chunk_size)
    ]

    # Send first chunk as initial embed
    first_embed = discord.Embed(title=post.title,
                                description=chunks[0],
                                color=0xff4500)
    first_embed.set_footer(
        text="Type /verdict when you're ready to reveal Reddit’s judgment.")
    await interaction.response.send_message(embed=first_embed)

    # Send remaining chunks
    for chunk in chunks[1:]:
        embed = discord.Embed(description=chunk, color=0xff4500)
        await interaction.followup.send(embed=embed)

    # AI Host Recap
    try:
        prompt = PROMPTS["AITA_POST_SUMMARY_PROMPT"].format(
            post_text=original_text)
        summary_response = openai.chat.completions.create(model="gpt-4.1-nano",
                                                          messages=[{
                                                              "role":
                                                              "user",
                                                              "content":
                                                              prompt
                                                          }],
                                                          max_tokens=120)
        ai_summary = summary_response.choices[0].message.content.strip()
    except Exception as e:
        ai_summary = "_AI summary unavailable._"

    await interaction.followup.send(f"🎙️ **Host Recap:** {ai_summary}")

    last_post[interaction.user.id] = {
        "title": post.title,
        "verdict": post.link_flair_text or "Unknown",
        "id": post.id
    }


@tree.command(name="verdict",
              description="Reveal the Reddit verdict",
              guild=GUILD_ID)
async def verdict(interaction: discord.Interaction):
    post = last_post.get(interaction.user.id)
    if not post:
        await interaction.response.send_message(
            "⛔ Whoa there, contestant! You need to draw a case first with `/aita`!"
        )
        return

    await interaction.response.send_message(
        "🎬 Buckle up! Gathering spicy hot takes from Reddit... 🍿",
        ephemeral=True)

    try:
        summary = get_top_comments_summary(post["id"])
        await interaction.followup.send(
            f"🎭 **Time to face the judgment!**\n\n"
            f"📜 **Post:** _{post['title']}_\n"
            f"🧠 **The Crowd Roars! Here's the top takes:**\n{summary}")
    except Exception as e:
        await interaction.followup.send(f"❌ Error summarizing comments: {e}")


# Run the bot
bot.run(os.getenv("DISCORD_TOKEN"))
