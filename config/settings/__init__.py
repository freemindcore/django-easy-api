import os

from .base import *

current_env = os.environ.get("DJANGO_SETTINGS_MODULE")
if current_env == "config.settings.local":
    from .local import *
elif current_env == "config.settings.test":
    from .test import *
else:
    print("NO VALID ENV USED, make sure you know what you are doing")
