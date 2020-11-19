from telethon import events
import asyncio
from collections import deque
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"flower"))
async def meme(event):
    if event.fwd_from:
        return   
    flower ="✨ 🌹✨"
    sleepValue = 1
           
    await event.edit(flower+"        ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+"       ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+"      ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+"     ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+"    ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+"   ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+"  ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+" ")
    await asyncio.sleep(sleepValue)
    await event.edit(flower+flower+flower+flower+flower+flower+flower+flower+flower+flower)
    await asyncio.sleep(sleepValue)
        
    
