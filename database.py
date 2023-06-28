from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


# connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=sqlaib;DATABASE=IA;UID=usuario;PWD=Contraseña;"
# connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
# engine = create_engine(connection_url)
engine = create_engine("sqlite:///data.db", echo=True, future=True)


# Crear la sesión para interactuar con la base de datos
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
