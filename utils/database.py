import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils import (
    Config
)


def init_engine(conf: Config):
    _engine = create_engine(f"sqlite:///{conf.SQLITE_DBNAME}")
    return _engine


engine = init_engine(Config())
SessionLocal = sessionmaker(bind=engine)
