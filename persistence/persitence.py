from sqlalchemy import create_engine, Table, Column, String, Date, MetaData, ForeignKey


def ensure_schema():
    engine = create_engine('sqlite:///stocks.db', echo=True)
    metadata = MetaData()
    stocks = Table('stocks', metadata,
                   Column('code', String, primary_key=True),
                   Column('name', String),
                   )


    stock_info = Table('stock_info', metadata,
                       Column('code', String, ForeignKey('stocks.code'), primary_key=True),
                       Column('date', Date, primary_key=True),
                       )

    metadata.create_all(engine)