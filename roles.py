from enum import Enum
from dotenv import load_dotenv
import os
load_dotenv()


class Role(Enum):
    ADMIN=os.getenv("SYSTEM_ADMIN")
    USER=os.getenv("SYSTEM_USER")