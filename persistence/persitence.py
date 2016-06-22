from sqlalchemy import Column, String, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class StockSymbolAndName(Base):
    __tablename__ = 'stocks'
    symbol = Column(String(10), primary_key=True)
    name = Column(String(255))

class StockInfo(Base):
    __tablename__ = 'sotck_info'
    symbol = Column(String(10), ForeignKey('stocks.symbol'), primary_key=True)
    date = Column(Date, primary_key=True)

class Persistor:
    def __init__(self):
        self.engine = create_engine('sqlite:///stocks.db', echo=True)
        self.session = sessionmaker(bind=self.engine)

    def session(self):
        return self.session()