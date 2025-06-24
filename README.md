# 🤖 AITA Game Show Bot


A Discord bot that turns Reddit's "Am I the A**hole?" posts into a hilarious, game-show-style showdown — powered by OpenAI, PRAW, and Discord's slash commands. Get juicy posts, AI-powered recaps, and verdicts based on top Reddit comments.

---

### 🤖 Project Attribution

All code, setup guides, and wiki content for this project were created in collaboration with [ChatGPT](https://openai.com/chatgpt) by OpenAI.

Special thanks to the AI assistant for helping turn chaotic Reddit drama into a Discord game night classic.

---

## 🚀 Replit Setup (Easiest Way to Run It)

Even if you've never coded before, you can run this bot for free using [Replit](https://replit.com):

### 🌱 1. Create a Replit Project from This Repo

- Go to [https://replit.com](https://replit.com)
- Click **"Create"** → choose **"Import from GitHub"**
- Paste the repo URL (e.g., `https://github.com/YOUR_USERNAME/self-discord-aita-gameshow-bot`)
- Click **"Import from GitHub"** to create the Repl

### 📦 2. Install Python Packages

Replit may auto-install everything listed in `requirements.txt`. If not:

- Open the **"Shell"** tab at the bottom and run:

```bash
pip install -r requirements.txt
```

This installs all the libraries like `discord`, `openai`, and `praw`.

### 🔐 3. Add Your Secrets (.env)

In the left sidebar:

- Click the **"Secrets"** tab (🔐 icon or labeled “Environment Variables”)
- Add the following keys, one at a time:

| Key | Description |
|-----|-------------|
| `DISCORD_TOKEN` | Your Discord bot token |
| `GUILD_ID` | Your Discord server (guild) ID |
| `REDDIT_CLIENT_ID` | Reddit app client ID |
| `REDDIT_CLIENT_SECRET` | Reddit app secret |
| `OPENAI_API_KEY` | Your OpenAI API key |

You do **not** need to manually create a `.env` file — Replit handles it for you with the Secrets tab.

### ▶️ 4. Run the Bot

- Click the big green **"Run"** button at the top
- Or, in the Shell tab, type:

```bash
python main.py
```

If successful, you’ll see something like:

```
✅ Synced 3 commands to guild 1234567890
🤖 Logged in as AITA Game Bot#1234
```

Now, in your Discord server, try `/aita` and enjoy the show!

---

## 🔐 Secrets Setup Guide

Here’s how to get each of those keys:

### 🗝️ DISCORD_TOKEN

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application → Go to **Bot** tab → Click **Add Bot**
3. Click **Reset Token** → Copy and use that value as `DISCORD_TOKEN`

> 🔗 [How to Add Your Bot to a Server](https://discordpy.readthedocs.io/en/stable/discord.html)

### 🏷️ GUILD_ID

1. In Discord, go to your server
2. Right-click the server name → Click **"Copy Server ID"**

> ⚙️ If you don’t see this option, turn on **Developer Mode** in Discord settings > Advanced

### 🔑 REDDIT_CLIENT_ID & REDDIT_CLIENT_SECRET

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Scroll down → Click **"Create App"**
3. Choose "script" type
4. Set a name, and for redirect URL just use `http://localhost`
5. After creating:
   - `client_id` is under the app name
   - `client_secret` is labeled as such

### 🔐 OPENAI_API_KEY

1. Go to [platform.openai.com](https://platform.openai.com/account/api-keys)
2. Click **Create new secret key**
3. Copy and use that as your `OPENAI_API_KEY`

> 🧠 Make sure your API key has access to `gpt-4.1-nano` or another supported model.

---

## 💻 Advanced Local Setup (VS Code, Terminal, etc.)

If you're running this locally, here’s how to set it up:

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/self-discord-aita-gameshow-bot.git
cd self-discord-aita-gameshow-bot
```

### 2. Create and Fill in `.env`

Create a file named `.env` in the root with this structure:

```
DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_discord_server_id
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
OPENAI_API_KEY=your_openai_api_key
```

### 3. Install Dependencies

We recommend using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python main.py
```

---

## 🧠 Project Structure

```
.
├── main.py                 # The main bot code
├── prompts.txt            # AI prompt templates (editable)
├── requirements.txt       # Python dependencies
├── .env                   # Secret API keys (not committed)
├── .gitignore             # Tells Git to ignore secrets, pyc files, etc
└── README.md              # This file!
```

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
