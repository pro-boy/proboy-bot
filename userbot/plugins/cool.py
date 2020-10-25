
from telethon import events
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern='cool ?(.*) '))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.4
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "cool":
        await event.edit(input_str)
        animation_chars = [
            "CooL",
            "🤩🤩",
            "cOOl",
            "🤩🤩",
            "🆒",
            "#coO0l",
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 6])
