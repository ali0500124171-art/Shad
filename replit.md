# R3D Telegram Bot

## Overview

This is an Arabic Telegram bot built with Pyrogram, designed for group management and entertainment features. The bot provides extensive functionality including user rank management, custom commands, games, media downloading (YouTube, Shazam), welcome messages, filters, and moderation tools. It's primarily targeted at Arabic-speaking Telegram communities.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Framework
- **Pyrogram**: The bot uses Pyrogram 2.0.97 as the Telegram client library, leveraging both synchronous (threading) and asynchronous patterns for message handling
- **Plugin Architecture**: Modular plugin system in the `Plugins/` directory where each file handles specific functionality (games, ranks, downloads, etc.)
- **Message Group Handlers**: Uses Pyrogram's group parameter to organize message handlers with different priorities (group=1, group=7, group=12, etc.)

### Data Storage
- **Redis**: Primary data store for all bot state, user data, ranks, permissions, custom commands, and settings. Uses a key-value pattern with composite keys like `{bot_id}:rankADMIN:{user_id}{Dev_Zaid}`
- **KVSQLite**: Secondary storage for specific features (YouTube downloads cache, Sound database, Whisper database) using `kvsqlite.sync.Client`

### Concurrency Model
- **Threading**: Most message handlers spawn new threads using `Thread(target=func, args=()).start()` for non-blocking execution
- **Async/Await**: Some features (whispers, inline queries, shell execution) use native asyncio

### Rank/Permission System
The bot implements a hierarchical permission system stored in Redis:
1. Dev (Bot Owner)
2. Dev² (Secondary developers)
3. Myth (Trusted users)
4. Group Owner (المالك الاساسي)
5. Owner (المالك)
6. Moderator (المدير)
7. Admin (ادمن)
8. Premium (مميز)
9. Member (عضو)

Helper functions in `helpers/Ranks.py` manage permission checks (`admin_pls`, `mod_pls`, `owner_pls`, etc.)

### Key Features Architecture
- **Custom Commands**: Stored in Redis with pattern `{chat_id}:Custom:{chat_id}{Dev_Zaid}&text={command}`
- **Filters/Auto-replies**: Pattern-based responses stored per group
- **Welcome Messages**: Customizable templates with placeholder substitution
- **Games**: Interactive games with currency system (فلوس/Riyal)
- **Media Downloads**: YouTube/audio downloads using yt_dlp, Shazam integration

### Configuration
- `config.py`: Contains Redis connection, bot token, owner ID, and database clients
- `information.py`: Stores bot token and owner ID (generated on first run)
- `main.py`: Entry point with interactive setup if configuration is missing

## External Dependencies

### Required Services
- **Redis Server**: Must be running locally on default port. The bot attempts to start Redis automatically if not running
- **Telegram Bot Token**: Required from BotFather
- **Telegram API Credentials**: Uses hardcoded API ID (13251350) and API hash

### Third-Party APIs
- **ARQ API** (`arq.hamker.dev`): For additional bot functionality
- **HTMLCSSToImage** (`htmlcsstoimage.com`): For screenshot generation
- **Restore Access API** (`restore-access.indream.app`): For account creation date lookup

### Python Package Dependencies (from r3d.txt)
- `pyrogram==2.0.97`, `tgcrypto`: Telegram client
- `redis`: Data storage
- `yt_dlp`, `pytube`, `youtube_search`: YouTube downloads
- `shazamio`: Music recognition
- `pillow`, `mutagen`: Media processing
- `aiohttp`, `httpx`: HTTP clients
- `kvsqlite`: SQLite key-value storage
- `akinator`: Game integration
- `gTTS`, `SpeechRecognition`, `pydub`: Voice features
- `telegraph`: Article publishing
- `meval`: Python code evaluation