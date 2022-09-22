from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo 🙋 {}
Saya adalah {}
Bot ini berfungsi untuk menjalankan Panda Userbot Diheroku.
Dengan Mudah\n
#Wajib
❗INFO MEMBUATNYA MEMBUTUHKAN AKUN HEROKU\n
Terimakasih ...
Disini ada Uda opsi pilihan:
Pilihan Pertama Berbasis Telethon Yang hanya bisa digunakan akun tertentu contoh id Awalan 50 langsung terbanned/Akun Terhapus\n
Pilihan Kedua Berbasis Pyrogram Yang bisa digunakan kesemua akun asalkan jangan spam/gcast berlebihan 
Maintened bot by @PandaUserbot
Fork Kasih Bintang Ya
    """


    NANDE = """
Halo 🙋 {}
Saya adalah {}
Bot ini berfungsi untuk menjalankan Nande Userbot Diheroku.
Dengan Mudah\n
#Wajib
❗INFO MEMBUATNYA MEMBUTUHKAN AKUN HEROKU\n
Terimakasih ...
Maintened bot by @PandaUserbot
    """


    # 
    buttonsn = [     
        [InlineKeyboardButton("Nande-Userbot", callback_data="nande")],]
   
    buttons = [     
        [InlineKeyboardButton("BasisTelethon", callback_data="bahasa")],
        [InlineKeyboardButton("BasisPyrogram", callback_data="pyropanda")],
   ]
