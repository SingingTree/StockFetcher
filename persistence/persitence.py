from sqlalchemy import Column, String, Date, Float, ForeignKey, create_engine
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
    price_earnings_ratio = Column(Float)

class Persistor:
    def __init__(self):
        self.engine = create_engine('sqlite:///stocks.db', echo=True)
        self.session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.session()