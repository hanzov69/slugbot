# 🐌 Slugbot

A Discord bot for people who have gazed into the abyss of slug culture and decided to embrace it.

## What Does It Do?

Users can opt into **slug mode** via `/slugmode on`. Once activated, every message they send is intercepted, deleted, and replaced with an authoritative translation from Human to Slug — because clearly what they *meant* to say was `schluuuuurppp gluuuurrrp`.

If a user sends more than 249 characters, the bot correctly identifies this as **too much yapping** and declines to translate.

On startup, the bot strips the slug role from everyone. No one gets to be a slug just because the bot was offline. You earn that every time.

## Setup

### Prerequisites
- Docker
- A Discord bot token
- A server role designated for slug victims
- The willingness to do this to your friends

### Configuration

Copy `.env.example` to `.env` and fill in the values:

```env
DISCORD_TOKEN=your_bot_token_here
SLUG_ROLE_ID=the_role_id
GUILD_ID=your_server_id  # optional, but speeds up slash command registration
```

### Bot Permissions

In the Discord Developer Portal, your bot needs:
- **Privileged Gateway Intents**: Message Content, Server Members
- **Bot Permissions**: Manage Messages, Send Messages
- **OAuth2 Scopes**: `bot`, `applications.commands`

### Running

```bash
docker compose up -d --build
```

It will restart automatically on system boot. You're welcome.

## Commands

| Command | Effect |
|---|---|
| `/slugmode on` | You are now a slug. Good luck. |
| `/slugmode off` | You are no longer a slug. For now. |

## Slug Vocabulary

The bot selects two words at random from `slugwords.txt`, a hand-curated lexicon of 102 deeply important slug utterances including classics like `Fllllllllpppppppfftttttttt` and `schloooorrrggg`. Linguistics scholars have yet to weigh in.

## License

Do whatever you want with this. It's a slug bot.
