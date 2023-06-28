from sqlalchemy import Column, Integer, String,DateTime,Float,Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Global_Category(Base):
    __tablename__="tbl_Speech_global_word_category"
    ID = Column(Integer(),primary_key=True,index=True,autoincrement=True)
    CATEGORY = Column(String(100),nullable=False)
    word_categorys = relationship('Word_Category',back_populates='global_categorys')

class Word_Category(Base):
    __tablename__="tbl_Speech_word_category"
    ID = Column(Integer(),primary_key=True,index=True,autoincrement=True)
    CATEGORY = Column(String(100),nullable=False)
    GLOBAL_CATEGORY_ID = Column(Integer,ForeignKey("tbl_Speech_global_word_category.ID"),nullable=False)
    global_categorys = relationship("Global_Category",back_populates='word_categorys')
    key_words = relationship("Key_Word",back_populates='word_categorys')

class Key_Word(Base):
    __tablename__="tbl_Speech_key_words"
    ID = Column(Integer(),primary_key=True,index=True,autoincrement=True)
    WORD = Column(String(),nullable= False)
    SPEAKER = Column(String(30),nullable=False)
    WORD_CATEGORY_ID = Column(Integer,ForeignKey('tbl_Speech_word_category.ID'),nullable=False)
    word_categorys = relationship('Word_Category',back_populates='key_words')
    key_word_resumens = relationship('Key_word_Resumen',back_populates='key_words')

class Resumen_Call(Base):
    __tablename__="tbl_Speech_resumen_call"
    ID = Column(String(100),primary_key=True,index=True)
    DATE = Column(DateTime())
    ID_BOSS_EMPLOYE = Column(String())
    BOSS_NAME = Column(String())
    SERVICE_LINE = Column(String())
    TRANSCRIPT = Column(String())
    TRANSCRIPT_AGENT = Column(String())
    TRANSCRIPT_CUSTOMER = Column(String())
    WORD_PER_MINUTE = Column(Float())
    DURATION = Column(Float())
    SPEAKING_TIME = Column(Float())
    SILENCE_TIME =Column(Float())
    NUMBER_OF_SILENCES_5 =Column(Integer())
    NUMBER_OF_SILENCES_10 = Column(Integer())
    NUMBER_OF_SILENCES_15 = Column(Integer())
    NUMBER_OF_SILENCES_20 = Column(Integer())
    TOTAL_NUMBER_OF_SILENCES = Column(Integer())
    AVERAGE_SILENCE_DURATION = Column(Float())
    IS_SILENT = Column(Boolean())
    SENTIMENT =Column(String())
    key_word_resumens = relationship('Key_word_Resumen',back_populates='call')

class Key_word_Resumen(Base):
    __tablename__="tbl_Speech_words_resumen"
    ID = Column(Integer(),primary_key=True,index=True,autoincrement=True)
    KEY_WORD_ID = Column(Integer(),ForeignKey('tbl_Speech_key_words.ID'))
    COUNT_WORD =Column(Integer())
    CALL_ID =Column(Integer(),ForeignKey('tbl_Speech_resumen_call.ID'),nullable=False)
    call = relationship('Resumen_Call',back_populates='key_word_resumens')
    key_words = relationship('Key_Word',back_populates='key_word_resumens')
