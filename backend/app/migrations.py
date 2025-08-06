from alembic.config import Config
from alembic import command
import os

def run_migrations():
    alembic_cfg = Config("alembic.ini")  # path to your alembic.ini
    command.upgrade(alembic_cfg, "head")
