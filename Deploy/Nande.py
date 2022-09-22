
## Copyright Ilham Mansiz


from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
import asyncio
import os
import sys
import subprocess
import requests
import bs4
os.system("clear")
loop = asyncio.get_event_loop()

import sys
import heroku3
from time import time
import random
import requests
from git import Repo
import functools
import shlex
from typing import Tuple
import urllib3
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
import os, shutil
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest
from random import choice, randint

from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
)

from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
LOGS = getLogger("Heroku")

REPO_URL = "https://github.com/sip-userbot/Nande-Telethon"
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
BOT_USER = os.environ.get("BOT_USER", None)

def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)



async def nande(bot, msg, dev=False):
    ax = await msg.reply("`Memulai Deploy......🚀🚀...`")
    user_id = msg.chat.id
    await asyncio.sleep(2)
    REPO_FROK = "https://github.com/sip-userbot/Nande-Telethon"
    await ax.delete()
    api_id_msg = await bot.ask(user_id, 'Tolong Kirim  `Heroku api`', filters=filters.text)
    if dev:
        ilham = api_id_msg.text.replace(" ", "")
        heroku_conn = heroku3.from_key(ilham) 
    try:
        heroku_conn.apps()
    except:
        await msg.reply("`Heroku Api key Salah.. ❌`")
        return
    panda = await msg.reply("`✅ Berhasil Login Heroku`")
    await asyncio.sleep(2)
    await panda.delete()
    
    ham = await msg.reply("`Memulai Generate String Auto`")
    await asyncio.sleep(2)
    await ham.delete()
    await msg.delete()

    appi_id_msg = await bot.ask(user_id, 'Silahkan kirimkan  `No HP` Untuk mendapatkan StringSession auto', filters=filters.text)
    try:
        phone = int(appi_id_msg.text)
    except ValueError:
        await appi_id_msg.reply('Tidak Benar No hp Gunakan +62xxxxxxx. Please deploy lagi.')    
        return
    await asyncio.sleep(5)
    await msg.reply(
          "Cek Kode disini",
      reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Click here", url="tg://openmessage?user_id=777000")
        ]]))
    app_id = 3742818
    api_hash = "46bc8c6fb788bca35d1cc29823f29cd0"
    client = TelegramClient(StringSession(), app_id, api_hash)
    await client.connect()
    try:
        if dev:
            code = await client.send_code_request(phone)
        else:
            code = await client.send_code(phone)
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply("`PHONE_NUMBER` is invalid")
        return
    try:
        phone_code_msg = await bot.ask(user_id, "Mohon Kirim Code dengan ketik yang bener . CONTOHNYA : 1.2.3.6.7 JANGAN GINI 122367 Ngertikan", filters=filters.text, timeout=600)
    except TimeoutError:
        await msg.reply('Time limit reached of 10 minutes. Gagal Kelamaan :)')
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if dev:
            await client.sign_in(phone, phone_code, password=None)
        else:
            await client.sign_in(phone, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply('OTP is invalid. Please ulangi deploy dari awal')
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(user_id, 'Your account has enabled two-step verification. Please provide the password.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('Time limit reached of 5 minutes. Tolong ulangi dari awal :)')
            return
        try:
            password = two_step_msg.text
            if dev:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply('Invalid Password Provided..Ulangi deploy kok bisa salah :)')
            return
    if dev:
        string_session = client.session.save()
    hamz = await msg.reply("`Memulai Auto Bot Asisten di @Botfather`")
    await asyncio.sleep(5)
    await hamz.delete()
    who = await client.get_me()
    name = "Assistant " + who.first_name
    if who.username:
        username = who.username + "_nandebot"
    else:
        username = "Nande" + (str(who.id))[5:] + "_nandebot"
    bf = "Botfather"
    await client(UnblockRequest(bf))
    await asyncio.sleep(1)
    await client.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await client.send_message(bf, "/deletebot")
    await asyncio.sleep(1)
    await client.send_message(bf, f"@{username}")
    await asyncio.sleep(1)
    await client.send_message(bf, "Yes, I am totally sure.")
    await asyncio.sleep(1)
    await client.send_message(bf, "/start")
    await asyncio.sleep(1)
    await client.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await client.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Silakan buat Bot dari @BotFather dan tambahkan tokennya di var BOT_TOKEN"
        )
        sys.exit(1)
    await client.send_message(bf, name)
    await asyncio.sleep(1)
    await client.send_message(bf, username)
    isdone = (await client.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await asyncio.sleep(1)
        isdone = (await client.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            token = isdone.split("`")[1]
            await client.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_message(bf, "Search")
            await asyncio.sleep(3)
            await client.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_file(bf, "Deploy/IMG-20220923-WA0000.jpg")
            await asyncio.sleep(3)
            await client.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_message(bf, f"Managed With By {who.first_name}")
            await asyncio.sleep(3)
            await client.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_message(
                bf, f"Owner ~ {who.first_name} \nPowered By ~ @PandaUserbot and @suportNande "
            )
    isdone = (await client.get_messages(bf, limit=1))[0].text
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "Nande_" + (str(who.id))[6:] + str(ran) + "_nandebot"
        await client.send_message(bf, name)
        await asyncio.sleep(1)
        await client.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await client.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            await client.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_message(bf, "Search")
            await asyncio.sleep(3)
            await client.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_file(bf, "Deploy/IMG-20220923-WA0000.jpg")
            await asyncio.sleep(3)
            await client.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_message(bf, f"Managed With By {who.first_name}")
            await asyncio.sleep(3)
            await client.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await client.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await client.send_message(
                bf, f"Owner ~ {who.first_name} \nPowered By ~ @PandaUserbot and @suportsipuserbot"
            )
    bottoken = f"{token}"
    try:
        await client(JoinChannelRequest("@PandaUserbot"))
        await client(JoinChannelRequest("@suportNande"))
    except BaseException:
        pass
    await client.disconnect()
    appname = "nande" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        heroku_conn.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        await msg.reply("❌ Gagal membuat Heroku baru karena melebihi 5 Apps")
        return
    await msg.reply("✅ Sedang mendeploy Nande Userbot, Mohon tunggu..Nanti akan Ada pesan dari saya jika Sudah Siap Deploy...Tunggu 3-5 menit Sabar ya 😊✅")
    if os.path.isdir("./Nande-Telethon"):
        rm_r("./Nande-Telethon/")
    repo = Repo.clone_from(REPO_FROK,"./Nande-Telethon/", branch="Nande-Telethon")
    app = heroku_conn.apps()[appname]
    giturl = app.git_url.replace("https://", "https://api:" + ilham + "@")
    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        await msg.reply(f"❌ Terjadi kesalahan : {e}")
        

    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    buildpack_urls = ['heroku/python'] 
    app.update_buildpacks(buildpack_urls)
    config = app.config()
     
    config['ALIVE_NAME'] = f"{who.first_name}"
    config['API_HASH'] = api_hash
    config['API_KEY'] = app_id
    config['BOT_TOKEN'] = f"{bottoken}"
    config['BOT_USERNAME'] = f"@{username}"
    config['HEROKU_API_KEY'] = ilham
    config['HEROKU_APP_NAME'] = appname
    config['STRING_SESSION'] = string_session
    config['PM_AUTO_BAN'] = "True"


    aktif = await msg.reply(f"✅ Berhasil Mendeploy Nande Userbot")
    await asyncio.sleep(5)
    await aktif.delete()
    await msg.reply(f"✅ Nande Userbot Telah Aktif. Siap digunakan ✅")
    await msg.delete()
    try:
        app.process_formation()["worker"].scale(1)
    except:
        await msg.reply(f"❌ Terjadi kesalahan")
        return
    

