
import random
from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import admin_cmd
from telethon import events, types, functions, utils


def choser(cmd, pack, blacklist={}):
    docs = None
    @borg.on(events.NewMessage(pattern=rf'\.{cmd}', outgoing=True))
    async def handler(event):
        await event.delete()

        nonlocal docs
        if docs is None:
            docs = [
                utils.get_input_document(x)
                for x in (await borg(functions.messages.GetStickerSetRequest(types.InputStickerSetShortName(pack)))).documents
                if x.id not in blacklist
            ]

        await event.respond(file=random.choice(docs))


choser('sgirls', 'cutegirls00_by_fStikBot')
choser('solo', 'SungJinWoo')
choser('scat', 'Jshshsbdbdbev')
choser('sjay', 'Jayu_Animated', {
    1653974154589768377,
    1653974154589768312,
    1653974154589767857,
    1653974154589768311,
    1653974154589767816,
    1653974154589767939,
    1653974154589767944,
    1653974154589767912,
    1653974154589767911,
    1653974154589767910,
    1653974154589767909,
    1653974154589767863,
    1653974154589767852,
    1653974154589768677
})

def choser(cmd, pack, blacklist={}):
    docs = None
    @borg.on(events.NewMessage(pattern=rf'\.{cmd}', outgoing=True))
    async def handler(event):
        await event.delete()

        nonlocal docs
        if docs is None:
            docs = [
                utils.get_input_document(x)
                for x in (await borg(functions.messages.GetStickerSetRequest(types.InputStickerSetShortName(pack)))).documents
                if x.id not in blacklist
            ]

        await event.respond(file=random.choice(docs))


choser('brain', 'supermind')
choser('dab', 'DabOnHaters', {
    1653974154589768377,
    1653974154589768312,
    1653974154589767857,
    1653974154589768311,
    1653974154589767816,
    1653974154589767939,
    1653974154589767944,
    1653974154589767912,
    1653974154589767911,
    1653974154589767910,
    1653974154589767909,
    1653974154589767863,
    1653974154589767852,
    1653974154589768677
})

CMD_HELP.update(
    {
        "randomsticker": "**Plugin :** `randomsticker`\
        \n**Syntax : **`.scat`\
        \n**Usage: **random cat sticks \
        \n\n**Syntax : **`.solo`\
        \n**Usage: **random solo leveling sticks\
        \n\n**Syntax : **`.sgirls`\
        \n**Usage: **random cute girls sticks\
        \n\n**Syntax : **`.sani`\
        \n**Usage: **random animated sticks\
        \n\n**Syntax : **`.brain`\
        \n**Usage: **random brain sticks\
        \n\n**Syntax : **`.dab`\
        \n**Usage: **random dab sticks\
  " }
)
