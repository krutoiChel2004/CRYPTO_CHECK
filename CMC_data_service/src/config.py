from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# connect DB
API_KEY_COINMARKETCAP = os.environ.get("API_KEY_COINMARKETCAP")
