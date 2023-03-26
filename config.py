from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "6017693735:AAEoCfZiKzUcMIcZnj2RtIm2zg17x_YB1-Q")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuys0JCKUCYORD1NymdWNs3ZykOOjWGd1499dXCzjw_-WpxQTCwvYJkFUas_fhxLGs29gt9cnfMh_OCA6t1oz6QPhXuzKXow1bhjphT-CUr7_B_vWzTmj440Gj8-AAa-xvMvaVDTveRBKU_sZ3_mP9OHtQdhF62LAMIoz9nDHvhlrUqCbMQTSS7WoQPPnHXki_WIaToaLgHU2PuIHOn0bZoeAJvgUrXSRZyAJdqQsVb6K9KcHN3Dsxyr9FfLtt6cesuOp1RgjJblXJWKg5F1IYdkRFum2VNNzB53XUYsMhxkQ4OFYwH6A1BUEPk_L-e74NhqFHG5P3Z_eEcCTFZmSt0c=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "MHB531") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "MOHAMMED") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "MHB531PBOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "MHB531X") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BAIO21") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "18818614").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "18818614").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/f5b364ed9e94449dee565.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/f5b364ed9e94449dee565.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f5b364ed9e94449dee565.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/f5b364ed9e94449dee565.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/f5b364ed9e94449dee565.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/f5b364ed9e94449dee565.jpg")
