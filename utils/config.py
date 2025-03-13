class Config:
    SQLITE_DBNAME = "pgbacker.db"


class ConfigDev(Config):
    pass


class ConfigProd(Config):
    pass
