# Telegram Property Bot 🏠

A Telegram bot that helps users browse and search for property listings. Perfect for real estate agents, property managers, or anyone looking to share property information via Telegram.

## Features

- 📋 **List Properties**: Browse all available properties
- 🔍 **Search**: Filter properties by type (Apartment, House, Condo, Studio, Estate)
- 📊 **Statistics**: View property market statistics
- 💬 **Interactive**: User-friendly commands and responses

## Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (get one from [@BotFather](https://t.me/botfather) on Telegram)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BHARATH-7732/telegram_bot.git
   cd telegram_bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your Telegram Bot Token:
     ```
     TELEGRAM_BOT_TOKEN=your_bot_token_here
     ```

4. **Get a Telegram Bot Token**:
   - Open Telegram and search for [@BotFather](https://t.me/botfather)
   - Send `/newbot` and follow the instructions
   - Copy the token provided by BotFather
   - Paste it in your `.env` file

## Running the Bot

Start the bot with:

```bash
python bot.py
```

The bot will start polling for messages. You should see:
```
🤖 Bot is running! Press Ctrl+C to stop.
```

## Usage

Once the bot is running, open Telegram and search for your bot by the username you created. Then you can use these commands:

### Available Commands

- `/start` - Welcome message and overview
- `/help` - Display help information
- `/list` - Show all available properties
- `/search <type>` - Search for properties by type
  - Example: `/search Apartment`
  - Available types: Apartment, House, Condo, Studio, Estate
- `/stats` - View property statistics (total count, average price, etc.)

### Example Usage

1. Start a conversation with your bot on Telegram
2. Send `/start` to see the welcome message
3. Send `/list` to browse all properties
4. Send `/search House` to find houses only
5. Send `/stats` to see market statistics

## Property Data

Properties are stored in `properties.json`. You can edit this file to add, remove, or modify property listings.

### Property Structure

```json
{
  "id": 1,
  "title": "Property Title",
  "type": "Apartment",
  "location": "City, Area",
  "price": 350000,
  "bedrooms": 3,
  "bathrooms": 2,
  "area_sqft": 1500,
  "description": "Property description..."
}
```

## Customization

### Adding New Properties

Edit `properties.json` and add new property objects following the structure above.

### Modifying Commands

Edit `bot.py` to add new commands or modify existing ones. The bot uses the `python-telegram-bot` library.

## Dependencies

- `python-telegram-bot==20.7` - Telegram Bot API wrapper
- `python-dotenv==1.0.0` - Environment variable management

## Project Structure

```
telegram_bot/
├── bot.py              # Main bot application
├── properties.json     # Property listings database
├── requirements.txt    # Python dependencies
├── .env.example       # Example environment configuration
├── .env               # Your environment configuration (not in git)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Development

To contribute or modify:

1. Make your changes to the code
2. Test thoroughly with your bot
3. Submit a pull request with a clear description

## Security Notes

- Never commit your `.env` file or expose your bot token
- The `.env` file is already in `.gitignore` to prevent accidental commits
- Keep your bot token secret and regenerate if compromised

## Troubleshooting

### Bot doesn't respond
- Check that your bot token is correct in `.env`
- Ensure the bot is running (`python bot.py`)
- Verify you're messaging the correct bot

### Properties not showing
- Ensure `properties.json` exists in the same directory as `bot.py`
- Check that the JSON file is valid (use a JSON validator)

### Import errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Use Python 3.8 or higher

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please open an issue on GitHub.