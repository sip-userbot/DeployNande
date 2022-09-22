##Copyright Ilham Mansiz
##To prime Userbot

from asyncio.exceptions import TimeoutError
from text import Data
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
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

REPO_URL = "https://terpantaukah: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@github.com/terpantaukah/Prime-Userbot"
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

def rm_r(path):
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)






async def prime(bot, msg, en=False):
    startt = await msg.reply("`Start Deploy......🚀🚀...`")
    await startt.delete()
    await msg.reply(
          "Silakan Kirim Donasi buat Pemabaruan bot ini Semakin banyak donasi semakin aktif botnya",
      reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("💎 Click here 💎", url="https://t.me/sip-Userbot/2")
        ]]))
    await asyncio.sleep(10)
    abb = await msg.reply("Terimakasih Sudah donasi ☺")
    await asyncio.sleep(2)
    await abb.delete()
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, 'Please send  `Heroku api`', filters=filters.text)
    if en:
        ilham = api_id_msg.text.replace(" ", "")
        heroku_conn = heroku3.from_key(ilham) 
    try:
        heroku_conn.apps()
    except:
        await msg.reply("`Heroku Api key Valid.. ❌`")
        return
    Nande = await msg.reply("`✅ Login Heroku successfully `")
    await asyncio.sleep(2)
    await Nande.delete()
    mongotext = await bot.ask(user_id, 'Please send  `Mongo Url`', filters=filters.text)
    mongourlll = mongotext.text.replace(" ", "")
    ham = await msg.reply("`Start Generate String Auto`")
    await asyncio.sleep(2)
    await ham.delete()
    
    appi_id_msg = await bot.ask(user_id, 'Please send mobile number to get automatic StringSesion', filters=filters.text)
    try:
        phone = appi_id_msg.text
    except ValueError:
        await appi_id_msg.reply('wrong number, please send the number with the format +62xxxxxx.')    
        return
    await asyncio.sleep(2)
    await msg.reply(
          "Check the code here",
      reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Click here", url="tg://openmessage?user_id=777000")
        ]]))
    app_id = 3742818
    api_hash = "46bc8c6fb788bca35d1cc29823f29cd0"
    client = Client(":memory:", app_id, api_hash)
    await client.connect()
    try:
        if en:
            code = await client.send_code(phone)
    except (PhoneNumberInvalid):
        await msg.reply("`PHONE_NUMBER` is invalid")
        return
    try:
        phone_code_msg = await bot.ask(user_id, "Please send the code, how to write it in 1 2 4 5 6 format, don't be like this 12456", filters=filters.text, timeout=600)
    except TimeoutError:
        await msg.reply('Time limit reached of 10 minutes. Valid :)')
        return
    phone_code = phone_code_msg.text.replace(" ", "")
    try:
        if en:
            await client.sign_in(phone, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid):
        await msg.reply('OTP is invalid. Please ulangi deploy dari awal')
        return
    except (SessionPasswordNeeded):
        try:
            two_step_msg = await bot.ask(user_id, 'Your account has enabled two-step verification. Please provide the password.', filters=filters.text, timeout=300)
        except TimeoutError:
            await msg.reply('Time limit reached of 5 minutes. Tolong ulangi dari awal :)')
            return
        try:
            password = two_step_msg.text
            if en:
                await client.check_password(password=password)
        except (PasswordHashInvalid):
            await two_step_msg.reply('Invalid Password Provided.. :)')
            return
    if en:
        string_session = await client.export_session_string()
    hamz = await msg.reply("`Starting...`")
    await asyncio.sleep(2)
    await hamz.delete()
    who = await client.get_me()
    try:
        await client.join_chat("@suportNande")
        await client.join_chat("@suportsipuserbot")
    except BaseException:
        pass
    await client.disconnect()
    appname = "prime" + str(time() * 1000)[-4:].replace(".", "") + str(random.randint(0,500))
    try:
        heroku_conn.create_app(name=appname, stack_id_or_name='container', region_id_or_name="eu")
    except requests.exceptions.HTTPError:
        await msg.reply("❌ Gagal membuat Heroku baru karena melebihi 5 Apps")
        return
    await msg.reply("✅ Process deploy Nande - 𝚄𝚜𝚎𝚛𝚋𝚘𝚝, Please wait.. There will be a message from me when it's ready to deploy ✅... Waiting 3-5 minute")
    if os.path.isdir("./Nande-Telethon-"):
        rm_r("./Nande-Telethon-/")
    repo = Repo.clone_from(REPO_URL,"./Nande-Telethon-/", branch="Nande-Telethon")
    app = heroku_conn.apps()[appname]
    giturl = app.git_url.replace("https://", "https://api:" + Nande + "@")
    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(giturl)
    else:
        remote = repo.create_remote("heroku", giturl)
    try:
        remote.push(refspec="HEAD:refs/heads/master", force=True)
    except Exception as e:
        await msg.reply(f"❌ There is an error : {e}")
        
    app.install_addon(plan_id_or_name='062a1cc7-f79f-404c-9f91-135f70175577', config={})
    buildpack_urls = ['heroku/python'] 
    app.update_buildpacks(buildpack_urls)
    config = app.config()
     
    config['MONGO_URI'] = mongourlll
    config['API_HASH'] = api_hash
    config['API_ID'] = app_id
    config['HEROKU_API'] = ilham
    config['HEROKU_APP_NAME'] = appname
    config['SESSION'] = string_session
   
    


    aktif = await msg.reply(f"✅ Successfully Mendeploy Nande-Userbot")
    await asyncio.sleep(3)
    await aktif.delete()
    aktifkannn = await msg.reply(f"✅ Nande-Userbot is Active. Ready to use ✅")
    await aktifkannn.delete()
    await msg.reply(
          "Silakan Kirim Donasi buat Pemabaruan bot ini Semakin banyak donasi semakin aktif botnya",
      reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("💎 Click here 💎", url="https://t.me/sip-Userbot/2")
        ]]))
    try:
        app.process_formation()["nande"].scale(1)
    except:
        await msg.reply(f"❌ There is an error")
        return
