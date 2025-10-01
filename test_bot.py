#!/usr/bin/env python3
"""
Test script for the property bot functionality
Tests the core functions without requiring a Telegram bot token
"""

import json
from bot import load_properties, format_property


def test_load_properties():
    """Test loading properties from JSON file."""
    print("Testing load_properties()...")
    properties = load_properties()
    assert len(properties) > 0, "Should load at least one property"
    print(f"✓ Successfully loaded {len(properties)} properties")
    return properties


def test_format_property(properties):
    """Test property formatting."""
    print("\nTesting format_property()...")
    if not properties:
        print("✗ No properties to test")
        return
    
    formatted = format_property(properties[0])
    assert "🏠" in formatted, "Should contain house emoji"
    assert "Location:" in formatted, "Should contain location"
    assert "Price:" in formatted, "Should contain price"
    print("✓ Property formatting works correctly")
    print("\nSample formatted property:")
    print("-" * 50)
    print(formatted)
    print("-" * 50)


def test_property_structure():
    """Test that all properties have required fields."""
    print("\nTesting property structure...")
    properties = load_properties()
    required_fields = ['id', 'title', 'type', 'location', 'price', 
                      'bedrooms', 'bathrooms', 'area_sqft', 'description']
    
    for prop in properties:
        for field in required_fields:
            assert field in prop, f"Property {prop.get('id')} missing field: {field}"
    
    print(f"✓ All {len(properties)} properties have required fields")


def test_search_functionality():
    """Test search functionality."""
    print("\nTesting search functionality...")
    properties = load_properties()
    
    # Test searching by type
    search_type = "Apartment"
    filtered = [p for p in properties if p['type'].lower() == search_type.lower()]
    print(f"✓ Found {len(filtered)} {search_type}(s)")
    
    # Test different types
    types = set(prop['type'] for prop in properties)
    print(f"✓ Available property types: {', '.join(types)}")


def test_statistics():
    """Test statistics calculation."""
    print("\nTesting statistics calculation...")
    properties = load_properties()
    
    total = len(properties)
    avg_price = sum(p['price'] for p in properties) / total
    min_price = min(p['price'] for p in properties)
    max_price = max(p['price'] for p in properties)
    
    print(f"✓ Total properties: {total}")
    print(f"✓ Average price: ${avg_price:,.0f}")
    print(f"✓ Price range: ${min_price:,} - ${max_price:,}")
    
    # Count by type
    types_count = {}
    for prop in properties:
        prop_type = prop['type']
        types_count[prop_type] = types_count.get(prop_type, 0) + 1
    
    print("✓ Properties by type:")
    for ptype, count in types_count.items():
        print(f"  • {ptype}: {count}")


def main():
    """Run all tests."""
    print("=" * 50)
    print("Property Bot Function Tests")
    print("=" * 50)
    
    try:
        properties = test_load_properties()
        test_format_property(properties)
        test_property_structure()
        test_search_functionality()
        test_statistics()
        
        print("\n" + "=" * 50)
        print("✅ All tests passed!")
        print("=" * 50)
        print("\nTo run the bot with Telegram:")
        print("1. Get a bot token from @BotFather")
        print("2. Create .env file with: TELEGRAM_BOT_TOKEN=your_token")
        print("3. Run: python bot.py")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
