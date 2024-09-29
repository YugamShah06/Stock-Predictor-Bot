import asyncio
from telethon import TelegramClient
import pandas as pd
import re

# Replace with your own values
api_id = '21772785'
api_hash = '1b577b7d6812340efe867167946d16ec'
phone_number = '+919106189709'  # Your phone number with country code

# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# A more advanced function to extract information using keywords and patterns
def parse_message(message):
    stock_exchange = None
    company_name = None
    price = None
    country = None
    
    # Example stock exchanges and companies (expand this list or load from a database)
    stock_exchanges = ['NSE', 'BSE', 'NASDAQ', 'NYSE']
    countries = ['India', 'USA', 'UK', 'Germany', 'Canada']  # Example country list

    # Look for stock exchange mentions
    for exchange in stock_exchanges:
        if exchange in message:
            stock_exchange = exchange
            break

    # Simple pattern to capture stock prices (may need refinement based on actual messages)
    price_match = re.search(r'\b(?:Price|₹|$|USD|INR)[:\s]*([\d,.]+)', message)
    if price_match:
        price = price_match.group(1).replace(',', '')

    # Assuming company names are usually capitalized words and common financial terms may precede or follow
    company_match = re.search(r'([A-Z][a-zA-Z\s]+)\s*(?:Ltd|Inc|Corp|Co|Company)', message)
    if company_match:
        company_name = company_match.group(1)

    # Search for country mentions
    for country in countries:
        if country in message:
            country = country
            break

    return stock_exchange, company_name, price, country

# Define a function to fetch messages and save them as a CSV
async def fetch_messages_to_csv():
    # Replace 'channel_name' with the actual name or ID of the group/channel you want to scrape
    target_channel = 'https://t.me/stocks'

    messages_data = []

    async with client:
        # Iterate over messages in the target channel/group
        async for message in client.iter_messages(target_channel, limit=100):  # Set your limit here
            if message.text:
                # Parse the message text for stock details
                stock_exchange, company_name, price, country = parse_message(message.text)

                # Store message details in a dictionary
                messages_data.append({
                    "message": message.text,
                    "date": message.date,
                    "sender_id": message.sender_id,
                    "stock_exchange": stock_exchange,
                    "company_name": company_name,
                    "price": price,
                    "country": country
                })

    # Convert the list of messages into a pandas DataFrame
    df = pd.DataFrame(messages_data)

    # Save the DataFrame to a CSV file
    df.to_csv("telegram_messages.csv", index=False)
    print("Messages saved to telegram_messages.csv successfully!")

# Start the client and run the fetching function
async def main():
    await client.start(phone=phone_number)
    print("Signed in successfully!")
    await fetch_messages_to_csv()

if __name__ == '__main__':
    # Run the main function
    asyncio.run(main())
