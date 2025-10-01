#!/usr/bin/env python3
"""
Telegram Bot for Property Updates
Allows users to browse, search, and subscribe to property listings.
"""

import json
import logging
import os
from typing import List, Dict, Any

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load properties data
PROPERTIES_FILE = "properties.json"


def load_properties() -> List[Dict[str, Any]]:
    """Load properties from JSON file."""
    try:
        with open(PROPERTIES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Properties file {PROPERTIES_FILE} not found!")
        return []


def format_property(property_data: Dict[str, Any]) -> str:
    """Format property data for display."""
    return (
        f"🏠 *{property_data['title']}*\n"
        f"📍 Location: {property_data['location']}\n"
        f"🏷️ Type: {property_data['type']}\n"
        f"💰 Price: ${property_data['price']:,}\n"
        f"🛏️ Bedrooms: {property_data['bedrooms']}\n"
        f"🚿 Bathrooms: {property_data['bathrooms']}\n"
        f"📐 Area: {property_data['area_sqft']} sqft\n"
        f"📝 Description: {property_data['description']}\n"
    )


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    welcome_message = (
        "👋 Welcome to the Property Bot!\n\n"
        "I can help you find your dream property. Here's what I can do:\n\n"
        "🔍 /list - Browse all available properties\n"
        "🔎 /search - Search properties by type\n"
        "📊 /stats - View property statistics\n"
        "ℹ️ /help - Show this help message\n\n"
        "Let's find your perfect home! 🏡"
    )
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_message = (
        "🤖 *Property Bot Help*\n\n"
        "*Available Commands:*\n"
        "/start - Start the bot and see welcome message\n"
        "/list - View all available properties\n"
        "/search - Search properties by type (Apartment, House, Condo, Studio, Estate)\n"
        "/stats - View statistics about available properties\n"
        "/help - Show this help message\n\n"
        "*How to Search:*\n"
        "Use /search followed by property type, for example:\n"
        "• /search Apartment\n"
        "• /search House\n"
        "• /search Condo\n\n"
        "Need assistance? Just send me a message!"
    )
    await update.message.reply_text(help_message, parse_mode="Markdown")


async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """List all available properties."""
    properties = load_properties()
    
    if not properties:
        await update.message.reply_text("No properties available at the moment.")
        return
    
    await update.message.reply_text(
        f"📋 Found {len(properties)} available properties:\n"
    )
    
    for prop in properties:
        formatted_property = format_property(prop)
        await update.message.reply_text(formatted_property, parse_mode="Markdown")


async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Search properties by type."""
    if not context.args:
        await update.message.reply_text(
            "Please specify a property type to search.\n"
            "Example: /search Apartment\n\n"
            "Available types: Apartment, House, Condo, Studio, Estate"
        )
        return
    
    search_type = " ".join(context.args).title()
    properties = load_properties()
    
    # Filter properties by type
    filtered_properties = [
        prop for prop in properties 
        if prop["type"].lower() == search_type.lower()
    ]
    
    if not filtered_properties:
        await update.message.reply_text(
            f"No properties found of type '{search_type}'.\n"
            "Available types: Apartment, House, Condo, Studio, Estate"
        )
        return
    
    await update.message.reply_text(
        f"🔍 Found {len(filtered_properties)} {search_type}(s):\n"
    )
    
    for prop in filtered_properties:
        formatted_property = format_property(prop)
        await update.message.reply_text(formatted_property, parse_mode="Markdown")


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show property statistics."""
    properties = load_properties()
    
    if not properties:
        await update.message.reply_text("No properties available for statistics.")
        return
    
    # Calculate statistics
    total_properties = len(properties)
    avg_price = sum(prop["price"] for prop in properties) / total_properties
    min_price = min(prop["price"] for prop in properties)
    max_price = max(prop["price"] for prop in properties)
    
    # Count by type
    types_count = {}
    for prop in properties:
        prop_type = prop["type"]
        types_count[prop_type] = types_count.get(prop_type, 0) + 1
    
    types_breakdown = "\n".join([f"  • {ptype}: {count}" for ptype, count in types_count.items()])
    
    stats_message = (
        f"📊 *Property Statistics*\n\n"
        f"Total Properties: {total_properties}\n"
        f"Average Price: ${avg_price:,.0f}\n"
        f"Price Range: ${min_price:,} - ${max_price:,}\n\n"
        f"*Properties by Type:*\n"
        f"{types_breakdown}"
    )
    
    await update.message.reply_text(stats_message, parse_mode="Markdown")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages."""
    message_text = update.message.text.lower()
    
    if any(word in message_text for word in ["hello", "hi", "hey"]):
        await update.message.reply_text(
            "Hello! 👋 Use /help to see what I can do for you."
        )
    elif any(word in message_text for word in ["property", "properties", "house", "apartment"]):
        await update.message.reply_text(
            "Looking for properties? Use /list to see all available properties "
            "or /search to find specific types!"
        )
    else:
        await update.message.reply_text(
            "I'm not sure what you mean. Type /help to see available commands."
        )


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors."""
    logger.error(f"Update {update} caused error {context.error}")
    if update and update.message:
        await update.message.reply_text(
            "Sorry, an error occurred while processing your request."
        )


def main() -> None:
    """Start the bot."""
    # Get bot token from environment variable
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables!")
        print("Error: Please set TELEGRAM_BOT_TOKEN in .env file")
        return
    
    # Create the Application
    application = Application.builder().token(token).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("list", list_command))
    application.add_handler(CommandHandler("search", search_command))
    application.add_handler(CommandHandler("stats", stats_command))
    
    # Register message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Register error handler
    application.add_error_handler(error_handler)
    
    # Start the bot
    logger.info("Starting bot...")
    print("🤖 Bot is running! Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
