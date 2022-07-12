
from enum import IntEnum

# Bot initial Settings
class BotMode(IntEnum):
     TEXT = 1
     AUDIO = 2

class Config:
  def __init__(self):
    self.mode = BotMode.TEXT
    self.name = "sim"

default_config = Config()
