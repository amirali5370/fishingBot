from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# ایجاد Base برای مدل‌ها
Base = declarative_base()

# تنظیم اتصال به پایگاه داده (SQLite در اینجا)
engine = create_engine('sqlite:///bot_database.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# تابعی برای ایجاد جداول
def init_db():
    Base.metadata.create_all(bind=engine)
