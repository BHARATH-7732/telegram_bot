# Usage Guide

## Getting Your Bot Token

1. Open Telegram and search for `@BotFather`
2. Start a chat and send `/newbot`
3. Follow the prompts:
   - Choose a name for your bot (e.g., "My Property Bot")
   - Choose a username (must end in 'bot', e.g., "my_property_bot")
4. BotFather will give you a token that looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`
5. Copy this token to your `.env` file

## Setting Up

```bash
# 1. Copy the environment template
cp .env.example .env

# 2. Edit .env and paste your bot token
# TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the bot
python bot.py
```

## Bot Commands

### /start
Shows welcome message with available commands.

**Example:**
```
User: /start
Bot: 👋 Welcome to the Property Bot!
     I can help you find your dream property...
```

### /list
Displays all available properties in the database.

**Example:**
```
User: /list
Bot: 📋 Found 5 available properties:
     
     🏠 *Luxury Apartment in Downtown*
     📍 Location: Downtown, City Center
     🏷️ Type: Apartment
     💰 Price: $350,000
     ...
```

### /search [type]
Search for properties by type.

**Available types:**
- Apartment
- House
- Condo
- Studio
- Estate

**Example:**
```
User: /search House
Bot: 🔍 Found 1 House(s):
     
     🏠 *Spacious Family Home*
     📍 Location: Suburbs, Green Valley
     ...
```

### /stats
View statistics about available properties.

**Example:**
```
User: /stats
Bot: 📊 Property Statistics
     
     Total Properties: 5
     Average Price: $475,000
     Price Range: $150,000 - $950,000
     
     Properties by Type:
       • Apartment: 1
       • House: 1
       • Studio: 1
       • Condo: 1
       • Estate: 1
```

### /help
Displays detailed help information.

## Adding Properties

Edit `properties.json` to add new properties:

```json
{
  "id": 6,
  "title": "Your Property Title",
  "type": "Apartment",
  "location": "City, Area",
  "price": 250000,
  "bedrooms": 2,
  "bathrooms": 1,
  "area_sqft": 900,
  "description": "Description of your property..."
}
```

**Important:** Restart the bot after modifying `properties.json` for changes to take effect.

## Tips

1. **Keep your token secret**: Never share your bot token publicly
2. **Test locally first**: Make sure everything works before deploying
3. **Customize properties**: Edit `properties.json` with your actual listings
4. **Monitor logs**: The bot logs activities to help with debugging
5. **Stop the bot**: Press `Ctrl+C` to stop the bot gracefully

## Common Issues

### "TELEGRAM_BOT_TOKEN not found"
- Make sure you created the `.env` file
- Check that the token is on a line like: `TELEGRAM_BOT_TOKEN=your_token`
- No spaces around the `=` sign

### Bot doesn't respond
- Verify the bot is running (you should see "🤖 Bot is running!")
- Make sure you're messaging the correct bot
- Check that your token is valid

### Properties not loading
- Ensure `properties.json` is in the same directory as `bot.py`
- Validate your JSON syntax (use a JSON validator online)
- Check file permissions

## Advanced Usage

### Running in Background
```bash
# Using nohup (Linux/Mac)
nohup python bot.py > bot.log 2>&1 &

# Using screen (Linux/Mac)
screen -S telegram_bot
python bot.py
# Press Ctrl+A then D to detach
```

### Running with systemd (Linux)
Create `/etc/systemd/system/telegram-bot.service`:

```ini
[Unit]
Description=Telegram Property Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/telegram_bot
ExecStart=/usr/bin/python3 /path/to/telegram_bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
sudo systemctl status telegram-bot
```

### Environment Variables

You can also set the token via environment variable:
```bash
export TELEGRAM_BOT_TOKEN="your_token"
python bot.py
```

## Next Steps

- Customize property data in `properties.json`
- Add more commands to `bot.py`
- Implement a database for dynamic property management
- Add image support for properties
- Create admin commands for adding/removing properties
- Add user subscription features for property alerts
