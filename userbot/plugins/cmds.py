import asyncio

import requests
from userbot.utils import admin_cmd
from userbot import CMD_HELP


@borg.on(admin_cmd(pattern="cmds", outgoing=True))
async def install(event):
    if event.fwd_from:
        return
    tele = await event.edit("`Searching for all plugins...`")
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = (
        OUTPUT
    ) = f"Here is the list of plugins found in 'master' branch of ur USERBOT.\n{o}\n\nUse .help <plugin_name> to learn how a paticular plugin works.\nOr use .check <plugin_name>"
    await tele.edit("`Plugins extracted, pasting it...`")
    message = OUTPUT
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    await tele.edit(
        f"`All plugins available in ur` **USERBOT** `can be found` [here]({url})!!"
    )


CMD_HELP.update(
    {"cmds": ".cmds\nUse - Get the list of all plugins in the bot."}
)
