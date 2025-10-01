#!/bin/bash
# Quick start script for Telegram Property Bot

echo "======================================"
echo "Telegram Property Bot - Quick Start"
echo "======================================"
echo

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Please install pip."
    exit 1
fi

echo "✓ pip found"
echo

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 .env file not found. Creating from template..."
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✓ Created .env file"
        echo
        echo "⚠️  IMPORTANT: Edit .env and add your Telegram bot token!"
        echo "   Get your token from @BotFather on Telegram"
        echo
        read -p "Press Enter to continue after you've added your token..."
    else
        echo "❌ .env.example not found!"
        exit 1
    fi
else
    echo "✓ .env file exists"
fi

# Check if token is set
if grep -q "your_bot_token_here" .env 2>/dev/null; then
    echo
    echo "⚠️  WARNING: Bot token not configured!"
    echo "   Please edit .env and replace 'your_bot_token_here' with your actual token"
    echo
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo

# Install dependencies
echo "📦 Installing dependencies..."
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt
else
    pip install -r requirements.txt
fi

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed"
echo

# Run tests
echo "🧪 Running tests..."
python3 test_bot.py

if [ $? -ne 0 ]; then
    echo "❌ Tests failed"
    exit 1
fi

echo
echo "======================================"
echo "✅ Setup complete!"
echo "======================================"
echo
echo "To start the bot, run:"
echo "  python3 bot.py"
echo
echo "Or run this script again to check everything is working."
echo
