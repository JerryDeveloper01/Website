import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'Raj_Website_RoBot')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '21563841'))
API_HASH = environ.get('API_HASH', 'aa468717ecb3153d47dba2d9be6eb90d')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "7774159193:AAFmutND0WGfMY8kGGkVO7yFObbJgGBql-8")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '6443740402'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "Raj_Website_RoBot")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002769552465'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://kingrajashish43211:rOYviMdPMPfCvSlR@cluster0.j3o3sbf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", None)

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", None)

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
