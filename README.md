# Discord AI Bot with Gemini Pro

A Discord bot that uses Google's Gemini Pro model through OpenRouter to provide AI-powered responses to user queries.

## Features

- AI-powered responses using Gemini Pro
- Simple command interface (`!ask`)
- Easy setup and configuration
- Error handling and user feedback

## Prerequisites

- Python 3.8 or higher
- Discord Bot Token
- OpenRouter API Key

## Setup

1. Clone this repository:
```bash
git clone <your-repo-url>
cd discord-ai-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your credentials:
```env
OPENROUTER_API_KEY=your_openrouter_api_key
DISCORD_BOT_TOKEN=your_discord_bot_token
```

4. Set up your Discord bot:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" section and create a bot
   - Enable "Message Content Intent" under Privileged Gateway Intents
   - Copy the bot token to your `.env` file

5. Invite the bot to your server:
   - Go to OAuth2 > URL Generator in Discord Developer Portal
   - Select "bot" scope and the following permissions:
     - Send Messages
     - Read Messages/View Channels
   - Use the generated URL to invite the bot to your server

## Usage

1. Start the bot:
```bash
python bot.py
```

2. In Discord, use the following command:
```
!ask <your question>
```

Example:
```
!ask What is the capital of France?
```

## Environment Variables

- `DISCORD_BOT_TOKEN`: Your Discord bot token
- `OPENROUTER_API_KEY`: Your OpenRouter API key

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 