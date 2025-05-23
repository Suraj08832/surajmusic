import os
import aiohttp
import random
import re
import string
import lyricsgenius as lg
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import app, GENIUS_API_TOKEN, lyrical

# Initialize Genius API
genius = lg.Genius(
    GENIUS_API_TOKEN,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
genius.verbose = False

async def get_lyrics(song_name: str) -> str:
    """Get lyrics from Genius API"""
    if not GENIUS_API_TOKEN:
        return "Lyrics functionality is not configured. Please set GENIUS_API_TOKEN in config.py"
    
    async with aiohttp.ClientSession() as session:
        # Search for the song
        search_url = f"https://api.genius.com/search?q={song_name}"
        headers = {"Authorization": f"Bearer {GENIUS_API_TOKEN}"}
        
        async with session.get(search_url, headers=headers) as response:
            if response.status != 200:
                return "Failed to fetch lyrics. Please try again later."
            
            data = await response.json()
            if not data.get("response", {}).get("hits"):
                return "No lyrics found for this song."
            
            # Get the first result
            song_id = data["response"]["hits"][0]["result"]["id"]
            
            # Get the lyrics
            lyrics_url = f"https://api.genius.com/songs/{song_id}"
            async with session.get(lyrics_url, headers=headers) as song_response:
                if song_response.status != 200:
                    return "Failed to fetch lyrics. Please try again later."
                
                song_data = await song_response.json()
                song_path = song_data["response"]["song"]["path"]
                
                # Get the actual lyrics from the song page
                song_url = f"https://genius.com{song_path}"
                async with session.get(song_url) as page_response:
                    if page_response.status != 200:
                        return "Failed to fetch lyrics. Please try again later."
                    
                    page_text = await page_response.text()
                    # Extract lyrics from the page
                    # This is a simple implementation - you might want to use a proper HTML parser
                    lyrics_start = page_text.find('"Lyrics__Container-sc-')
                    if lyrics_start == -1:
                        return "Could not extract lyrics from the page."
                    
                    lyrics_end = page_text.find('</div>', lyrics_start)
                    if lyrics_end == -1:
                        return "Could not extract lyrics from the page."
                    
                    lyrics = page_text[lyrics_start:lyrics_end]
                    # Clean up the lyrics
                    lyrics = lyrics.replace('<br/>', '\n')
                    lyrics = lyrics.replace('</div>', '')
                    lyrics = lyrics.replace('<div>', '')
                    lyrics = lyrics.replace('&amp;', '&')
                    lyrics = lyrics.replace('&quot;', '"')
                    lyrics = lyrics.replace('&#x27;', "'")
                    
                    return lyrics

@app.on_message(filters.command(["lyrics", "lyric"]))
async def lyrics_command(client, message: Message):
    """Handle /lyrics command"""
    if len(message.command) < 2:
        await message.reply_text("Please provide a song name. Usage: /lyrics <song name>")
        return
    
    title = " ".join(message.command[1:])
    m = await message.reply_text("Searching for lyrics...")
    
    try:
        song = genius.search_song(title, get_full_info=False)
        if song is None:
            return await m.edit(f"No lyrics found for {title}")
        
        # Generate a random hash for storing lyrics
        ran_hash = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        lyric = song.lyrics
        
        # Clean up lyrics
        if "Embed" in lyric:
            lyric = re.sub(r"\d*Embed", "", lyric)
        
        # Store lyrics in the global dictionary
        lyrical[ran_hash] = lyric
        
        # Create inline keyboard with button to view lyrics
        upl = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="View Lyrics",
                        url=f"https://t.me/{app.username}?start=lyrics_{ran_hash}",
                    ),
                ]
            ]
        )
        
        await m.edit("Lyrics found! Click the button below to view them.", reply_markup=upl)
        
    except Exception as e:
        await m.edit(f"Error fetching lyrics: {str(e)}")

@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    """Handle /start command with lyrics parameter"""
    if len(message.command) > 1 and message.command[1].startswith("lyrics_"):
        # Extract the hash from the command
        hash = message.command[1].split("_")[1]
        
        # Get lyrics from the global dictionary
        lyrics = lyrical.get(hash)
        if not lyrics:
            return await message.reply_text("Lyrics not found or expired.")
        
        # Split lyrics into chunks if they're too long
        max_length = 4096
        if len(lyrics) > max_length:
            chunks = [lyrics[i:i + max_length] for i in range(0, len(lyrics), max_length)]
            for i, chunk in enumerate(chunks):
                if i == 0:
                    await message.reply_text(f"Lyrics:\n\n{chunk}")
                else:
                    await message.reply_text(chunk)
        else:
            await message.reply_text(f"Lyrics:\n\n{lyrics}")
        
        # Clean up the stored lyrics
        lyrical.pop(hash, None) 