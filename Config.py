import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5872844484:AAFdFV1vU6yQnGMRk9ET2YmnSaTSZe3NHUA")
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOKgBu0ZWCxoGzpjwkFpPanPuC6UUYPwpyk_9Lk5YnLtv6Zn4UpK4-RSVdGnNwibLbIA1gT7uTs8uKQr8jUs1GixNb-cguFSoAb14kIOpixCz_r_lP45Dx0GiNzPRFQCDdlw3ZAaQERvlu3v0vTNgFmaJCIo61TXj250VbsL2KhZzfpsF93oCtAO4CynXe-0ydYbwd5sZZNoVmkgIRszha0_JhZGoduj6hhWdPoWObv_7qRrP6YNJArEK2SqU8a3fgOWfNcutTcW79LozqRdUlllBuQTP56a_VFQETXX2XP83XA8xgbuGhOJzGf-nyuV6_zixnB66j5azOEqiILpt-NHbMts= )
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
