
from config import Config
from database.database import Database

kyawwa = Database(Config.DATABASE_URL, Config.SESSION_NAME)
