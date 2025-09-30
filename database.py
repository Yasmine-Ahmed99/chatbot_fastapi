from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker  , declarative_base

sqlite_url = "sqlite:///database.db"
engine = create_engine(sqlite_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()