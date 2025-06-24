# 🎭 AITA Game Bot

A Discord bot that grabs random posts from Reddit's r/AmItheAsshole and delivers dramatic game show-style summaries and verdicts powered by ChatGPT (OpenAI API).

---

## 🚀 Features

- Fetches a random AITA post with a juicy title and full description  
- Strips out post edits/updates to avoid spoilers  
- Uses GPT-4.1-Nano to summarize the post like a snarky game show host  
- Reveals Reddit's verdict on command  
- Summarizes top 10 comments with dramatic flair  
- Fun and shareable for group calls or game night  

---

## 🛠️ Setup Instructions

### Option A: Run Locally (Advanced)

#### 1. Clone the Repo

```bash
git clone https://github.com/your-username/self-aita-game-bot.git
cd self-aita-game-bot
```

#### 2. Create Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

#### 3. Install Requirements

```bash
pip install -r requirements.txt
```

#### 4. Create a `.env` file

Make a new `.env` file in the root directory with:

```env
DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_discord_server_id

REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret

OPENAI_API_KEY=your_openai_api_key
```

> Don’t share this file. It contains secrets.

#### 5. Run the Bot

```bash
python main.py
```

---

### Option B: Run on Replit (Easy & Free)

#### 1. Go to [Replit.com](https://replit.com/)

- Create an account if you don’t already have one.

#### 2. Click "Create Repl" → Choose "Python"

#### 3. Copy and paste the project files into your new Replit:
- `main.py`
- `prompts.txt` (contains your editable AI prompts)
- `requirements.txt` (make sure it's present)

#### 4. Add Secrets (your `.env` values)

Click the 🔐 **"Secrets"** tab in the left sidebar (called "Environment Variables")

Add the following keys and values (exact names):

```
DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_discord_server_id
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
OPENAI_API_KEY=your_openai_api_key
```

#### 5. Install Python Packages

In the Replit shell at the bottom, run:

```bash
pip install -r requirements.txt
```

> This ensures everything like `discord.py`, `praw`, `openai`, and `python-dotenv` is installed.

#### 6. Run It!

Hit the big green **"Run"** button at the top. You should see something like:

```
✅ Synced 2 commands to guild 123456789...
🤖 Logged in as AITA Game Bot#1234
```

If so — congrats! Your bot is live.

---

## 📁 File Structure

```
.
├── main.py                 # The bot logic
├── prompts.txt             # Editable AI prompts for summaries
├── .env / Replit secrets   # Your API keys (private!)
├── requirements.txt        # All the Python dependencies
└── README.md               # This file!
```

---

## 🧪 Example Commands

- `/aita` – Grab a fresh AITA post and a sassy AI summary  
- `/verdict` – Reveal Reddit's real verdict and get a spicy crowd-sourced summary  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
