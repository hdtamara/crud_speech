from pydantic import BaseModel
from datetime import datetime


class Global_Category(BaseModel):
    ID: int
    CATEGORY = str
    class Config:
        orm_mode =True

class Word_Category(BaseModel):
    ID:int
    CATEGORY:str
    GLOBAL_CATEGORY_ID:int
    class Config:
        orm_mode =True

class Key_Word(BaseModel):
    ID:int
    WORD: str
    SPEAKER: str
    WORD_CATEGORY_ID:int
    class Config:
        orm_mode =True

class Resumen_Call(BaseModel):
    ID : str
    DATE : datetime
    ID_BOSS_EMPLOYE : int
    BOSS_NAME : str
    SERVICE_LINE : str
    TRANSCRIPT : str
    TRANSCRIPT_AGENT : str
    TRANSCRIPT_CUSTOMER : str
    WORD_PER_MINUTE : float
    DURATION : float
    SPEAKING_TIME : float
    SILENCE_TIME : float
    NUMBER_OF_SILENCES_5 : int
    NUMBER_OF_SILENCES_10 : int
    NUMBER_OF_SILENCES_15 : int
    NUMBER_OF_SILENCES_20 : int
    TOTAL_NUMBER_OF_SILENCES : int
    AVERAGE_SILENCE_DURATION :float
    IS_SILENT : bool
    SENTIMENT : str
    class Config:
        orm_mode =True

class Key_word_Resumen(BaseModel):
    ID : int
    KEY_WORD_ID : int
    COUNT_WORD : int
    CALL_ID :int
    class Config:
        orm_mode =True
