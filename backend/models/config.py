import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # можно заменить на PostgreSQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False