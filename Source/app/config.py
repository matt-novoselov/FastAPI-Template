from os import getenv
import dotenv

# Load secrets from environment
dotenv.load_dotenv()

# Load Root Path for API
ROOT_PATH = getenv("API_ROOT_PATH")
