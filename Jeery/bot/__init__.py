from pyrogram import Client, types
from info import *
from typing import Union, Optional, AsyncGenerator
from aiohttp import web

Raj_Website_RoBot = Client(name=SESSION, api_id=API_ID, api_hash=API_HASH, bot_token=BACKUP_BOT_TOKEN, workers=150, sleep_threshold=5)

class Raj_Website_RoBot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=150,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )
    
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """ɪᴛᴇʀᴀᴛᴇ ᴛʜʀᴏᴜɢʜ ᴀ ᴄʜᴀᴛ ꜱᴇQᴜᴇɴᴛɪᴀʟʟʏ.
        ᴛʜɪꜱ ᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ ᴍᴇᴛʜᴏᴅ ᴅᴏᴇꜱ ᴛʜᴇ ꜱᴀᴍᴇ ᴀꜱ ʀᴇᴘᴇᴀᴛᴇᴅʟʏ ᴄᴀʟʟɪɴɢ :ᴍᴇᴛʜ:`~pyrogram.Client.get_messages` ɪɴ ᴀ ʟᴏᴏᴘ, ᴛʜᴜꜱ ꜱᴀᴠɪɴɢ
        ʏᴏᴜ ꜰʀᴏᴍ ᴛʜᴇ ʜᴀꜱꜱʟᴇ ᴏꜰ ꜱᴇᴛᴛɪɴɢ ᴜᴘ ʙᴏɪʟᴇʀᴘʟᴀᴛᴇ ᴄᴏᴅᴇ. ɪᴛ ɪꜱ ᴜꜱᴇꜰᴜʟ ꜰᴏʀ ɢᴇᴛᴛɪɴɢ ᴛʜᴇ ᴡʜᴏʟᴇ ᴄʜᴀᴛ ᴍᴇꜱꜱᴀɢᴇꜱ ᴡɪᴛʜ ᴀ
        ꜱɪɴɢʟᴇ ᴄᴀʟʟ.
        Parameters:
            ᴄʜᴀᴛ_ɪᴅ (``ɪɴᴛ`` | ``ꜱᴛʀ``):
                ᴜɴɪQᴜᴇ ɪᴅᴇɴᴛɪꜰɪᴇʀ (ɪɴᴛ) ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ (ꜱᴛʀ) ᴏꜰ ᴛʜᴇ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ.
                ꜰᴏʀ ʏᴏᴜʀ ᴘᴇʀꜱᴏɴᴀʟ ᴄʟᴏᴜᴅ (ꜱᴀᴠᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ) ʏᴏᴜ ᴄᴀɴ ꜱɪᴍᴘʟʏ ᴜꜱᴇ "ᴍᴇ" ᴏʀ "ꜱᴇʟꜰ".
                ꜰᴏʀ ᴀ ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴀᴛ ᴇxɪꜱᴛꜱ ɪɴ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴅᴅʀᴇꜱꜱ ʙᴏᴏᴋ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ʜɪꜱ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ (ꜱᴛʀ).
                
            ʟɪᴍɪᴛ (``ɪɴᴛ``):
                ɪᴅᴇɴᴛɪꜰɪᴇʀ ᴏꜰ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙᴇ ʀᴇᴛᴜʀɴᴇᴅ.

                
            ᴏꜰꜰꜱᴇᴛ (``ɪɴᴛ``, *ᴏᴘᴛɪᴏɴᴀʟ*):
                ɪᴅᴇɴᴛɪꜰɪᴇʀ ᴏꜰ ᴛʜᴇ ꜰɪʀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʙᴇ ʀᴇᴛᴜʀɴᴇᴅ.
                ᴅᴇꜰᴀᴜʟᴛꜱ ᴛᴏ 0.
        ʀᴇᴛᴜʀɴꜱ:
            ``ɢᴇɴᴇʀᴀᴛᴏʀ``: ᴀ ɢᴇɴᴇʀᴀᴛᴏʀ ʏɪᴇʟᴅɪɴɢ :ᴏʙᴊ:`~ᴘʏʀᴏɢʀᴀᴍ.ᴛʏᴘᴇꜱ.ᴍᴇꜱꜱᴀɢᴇ` ᴏʙᴊᴇᴄᴛꜱ.
        ᴇxᴀᴍᴘʟᴇ:
            .. ᴄᴏᴅᴇ-ʙʟᴏᴄᴋ:: ᴘʏᴛʜᴏɴ
                ꜰᴏʀ ᴍᴇꜱꜱᴀɢᴇ ɪɴ ᴀᴘᴘ.ɪᴛᴇʀ_ᴍᴇꜱꜱᴀɢᴇꜱ("pyrogram", 1, 15000):
                    print(message.text)

        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
      
TechVJBot = TechVJXBot()

multi_clients = {}
work_loads = {}
