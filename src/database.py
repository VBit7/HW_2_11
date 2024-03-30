import contextlib

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine
# from src.conf.config import config


class Config:
    DB_URL = "postgresql+asyncpg://postgres:Example1234@localhost:5432/hw11"


config = Config


class DatabaseSessionManager:
    def __init__(self, url: str):
        self._engine: AsyncEngine | None = create_async_engine(url)
        self._session_maker: async_sessionmaker = async_sessionmaker(autoflush=False, autocommit=False,
                                                                     bind=self._engine)

    @contextlib.asynccontextmanager
    async def session(self):
        if self._session_maker is None:
            raise Exception("Session is not initialized")
        session = self._session_maker()
        try:
            yield session
        except Exception as err:
            print(err)
            await session.rollback()
        finally:
            await session.close()


sessionmanager = DatabaseSessionManager(config.DB_URL)


async def get_db():
    async with sessionmanager.session() as session:
        yield session





# import contextlib
# from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine, async_sessionmaker
#
#
# class Config:
#     DB_URL = "postgresql+asyncpg://postgres:Example1234@localhost:5432/hw11"
#
# config = Config()
#
# class DatabaseSessionManager:
#     def __init__(self, url: str):
#         self._engine: AsyncEngine | None = create_async_engine(url)
#         self._session_maker: async_sessionmaker = async_sessionmaker(autoflush=False, autocommit=False, bind=self._engine)
#
#     @contextlib.asynccontextmanager
#     async def session(self):
#         if self._session_maker is None:
#             raise Exception("Session is not initialized")
#         session = self._session_maker()
#         try:
#             yield session
#         except Exception as err:
#             print(err)
#             await session.rollback()
#         finally:
#             await session.close()
#
# sessionmanager = DatabaseSessionManager(config.DB_URL)
#
# async def get_db():
#     async with sessionmanager.session() as session:
#         yield session


# import sqlalchemy
# import sqlalchemy.orm as orm
#
# import contacts.models
#
# BASES = [
#     contacts.models.Base.metadata
# ]
#
# DBSession = None
#
# def connect():
#     global DBSession
#
#     engine = sqlalchemy.create_engine('sqlite:///planes.sqlite')
#
#     for base_meta in BASES:
#         base_meta.drop_all(engine)
#         base_meta.create_all(engine)
#         base_meta.bind = engine
#
#     DBSession = orm.sessionmaker(bind=engine)
#
# def get_database():
#     if DBSession is None:
#         connect()
#
#     db = DBSession()
#
#     try:
#         yield db
#     finally:
#         db.close()
