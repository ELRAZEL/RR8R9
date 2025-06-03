from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("8924406"))
API_HASH = getenv("f99d5618d841b4e28763af685f7c0bce")
BOT_TOKEN = getenv("7658536851:AAGill85SQGuSVbPUyu0cp9M1jD9d8vyS-I")
SESSION_NAME = getenv("SESSION_NAME", "BAGrlpUAKQVbAkygtR0MJPI7JQiLlcgRBHYYY9iPjxv3QCRhzCBVMaJI3bwy6gPRJlMN25N1VSA0J2T4MnkxXGrCDCdC2q7FNhgw8VDBbEAEQkIizQS3UFDh5uSeSlXA37SxOiBs6v3xXqnet-NatczG0Xsiso6r-cOfhKzZC5-wxgcbJVaSoCyemBzlKmSQTbEmMg39xOjYvHMWpTPQgDHDvFDReW0gM-p8gg6lirrI-AMsLHkJ8mXLb9ILn43BSmQrr7BJr-3heJJ0DAI-co8TiYKghQPLFEj4vtHcF7_3LzfwDRYX5FLUSJEArOCdpUevSMy0XkfgYB8nd5-EfBZZSv6DiwAAAAHRq6cCAA")

# mandatory vars
OWNER_USERNAME = getenv("@H_A_8Z")
ALIVE_NAME = getenv("Hazem Emam")
BOT_USERNAME = getenv("@Zomaaa2025bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/V_E_0O")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/Z_D0_F")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
