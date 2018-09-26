# Load our conf
from . import Env
import environ

env = Env()

READ_DOT_ENV_FILE = env('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    ROOT_DIR = environ.Path(__file__) - 2
    env.read_env(str(ROOT_DIR.path('.env')))

DEBUG = env('DEBUG', default=False, cast=bool)
GITHUB_USER = env('GITHUB_USER')
GITHUB_PSX = env('GITHUB_PSX')
