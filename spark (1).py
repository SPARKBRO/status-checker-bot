from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the client with credentials
app = Client(
    name="botstatus_spark",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    session_string=os.getenv("SESSION_STRING"),
)

TIME_ZONE = os.getenv("TIME_ZONE", "UTC")
BOT_LIST = [i.strip() for i in os.getenv("BOT_LIST", "").split()]
CHANNEL_OR_GROUP_ID = int(os.getenv("CHANNEL_OR_GROUP_ID"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID"))
BOT_ADMIN_IDS = list(map(int, os.getenv("BOT_ADMIN_IDS", "").split(",")))


async def check_bot_status():
    while True:
        print("Checking...")
        xxx_spark = f"**📊 𝗦𝗧𝗘𝗩𝗘 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦**"
        for bot in BOT_LIST:
            try:
                
                yyy_spark = await app.send_message(bot, "/start")
                aaa = yyy_spark.id
                await asyncio.sleep(10)
                zzz_spark = app.get_chat_history(bot, limit=1)
                async for ccc in zzz_spark:
                    bbb = ccc.id
                if aaa == bbb:
                    
                    bot_name = (await app.get_chat(bot)).first_name
                    bot_username = f"@{bot}"
                    xxx_spark += f"\n\n<blockquote>**__🤖 {bot_name} |  {bot_username} ❄️\n        └ Down ❌__**</blockquote>"
                    for bot_admin_id in BOT_ADMIN_IDS:
                        try:
                            await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!!\n\nHi Steve Bro This Measaage From FBI Your bot :- **{bot_name}** is down😄💀** ❌\n\n**__powered by : SPARKBRO ⚡__**")
                        except Exception:
                            pass
                    await app.read_chat_history(bot)
                else:
                    
                    bot_name = (await app.get_chat(bot)).first_name
                    bot_username = f"@{bot}"
                    xxx_spark += f"\n\n<blockquote>**__🤖 {bot_name} |  {bot_username} ❄️\n        └ Alive ✅__**</blockquote>"
                    await app.read_chat_history(bot)
            except FloodWait as e:
                await asyncio.sleep(e.x)
        time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
        last_update = time.strftime(f"%d %b %Y at %I:%M %p")
        xxx_spark += f"\n\n\n\n\n__⏳ Last checked on: {last_update}\n🌐{TIME_ZONE}__\n\n**__♻️ Refreshes Every 15 Minutes Automatically...__**"
        await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_spark)
        print(f"Last checked on: {last_update}")
        await asyncio.sleep(900)


async def main():
    await app.start()  
    await check_bot_status()


if __name__ == "__main__":
    app.run(main())  
