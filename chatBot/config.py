
from enum import IntEnum


class BotMode(IntEnum):
     TEXT = 1
     AUDIO = 2

class Config:
  def __init__(self):
    self.mode = BotMode.AUDIO
    self.name = "sim"

# Bot initial Settings
default_config = Config()
