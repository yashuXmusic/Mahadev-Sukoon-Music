from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "17273188"))
API_HASH = getenv("API_HASH", "a2e5bb2b69d13ba7553941af16cc2d5b")
BOT_TOKEN = getenv("BOT_TOKEN", "5754399511:AAFAQMd8eW42LrGUvW8SkSw6wM8C8UNa8HI")
BOT_NAME = getenv("BOT_NAME","𝗦𝗨𝗞𝗢𝗢𝗡 𝗠𝗨𝗦𝗜𝗖")
BOT_USERNAME = getenv("BOT_USERNAME", "SUKOON_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "NULL_CODER_BOT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "INDIAN_STUDY_WARRIORS")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "link_ki_duniya")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
START_IMG = getenv("START_IMG", "https://graph.org/file/a3eabb1a41a8040561b1b.jpg")
PING_IMG = getenv("PING_IMG", "https://graph.org/file/a3eabb1a41a8040561b1b.jpg")
SESSION_NAME = getenv("SESSION_NAME", "AQBmHPqDYZajc-eTBq3QU9d0tg9YGkWMfNAIvijclsMv44ZUVx2HSGiLBnOx5b4D1LMBSqh3FO__xmZIjUIXvzDBguY2wL2ZrMaeaoaWSaK4jnT3aVziC79p_ZMZiigh2U3pclidPtQQ0K7b4_mLJcDVdx2uS8oJVubNbC4hwUgUH4G2fdq0hDPsn-LTne85GdrOaxyZiiNeV0YkVeMCL9xqoyBrJ8GExXgPfD1f0Z9ExOeiL8cv_kFJaYej1pQP4hEkssxzFNwwcrIdeY2jp5wmCARKtfJk0JyaxjYBHaSLyoQmI7rF6dPwEfeZFtKPoukuysuk_eY7JEVcBS_hBMQ9AAAAAUQaO7AA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5956494225").split()))
