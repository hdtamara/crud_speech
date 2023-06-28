from database import SessionLocal,engine
import models
import schemas
from typing import List


models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)


session=SessionLocal()
def add_global_category(info:schemas.Global_Category) -> dict:
    data = models.Global_Category(**info)
    try:
        session.add(data)
        session.commit()
        return {'codigo':1, 'informacion':'Cargue Exitoso'}
    except Exception as e:
        session.rollback ()
        return {'codigo':0, 'informacion':f'Error en el cargue:{e.args}'}
    finally:
        session.close ()

def get_global_category(id:int):
    global_category = session.get(models.Global_Category,id)
    return global_category

def add_word_category(info:schemas.Word_Category) -> dict:
    global_category = get_global_category(info['GLOBAL_CATEGORY_ID'])
    data = models.Word_Category(**info)
    try:
        session.add(data)
        session.commit()
        return {'codigo':1, 'informacion':'Cargue Exitoso'}
    except Exception as e:
        session.rollback ()
        return {'codigo':0, 'informacion':f'Error en el cargue:{e.args}'}
    finally:
        session.close ()

def get_word_category(id:int):
    global_category = session.get(models.Global_Category,id)
    return global_category

def add_key_word(info:schemas.Key_Word) -> dict:
    data = models.Key_Word(**info)
    try:
        session.add(data)
        session.commit()
        return {'codigo':1, 'informacion':'Cargue Exitoso'}
    except Exception as e:
        session.rollback ()
        return {'codigo':0, 'informacion':f'Error en el cargue:{e.args}'}
    finally:
        session.close ()

def get_key_word(id:int):
    global_category = session.get(models.Global_Category,id)
    return global_category

def add_call_resumen(info:schemas.Resumen_Call) -> dict:
    data = models.Resumen_Call(**info)
    try:
        session.add(data)
        session.commit()
        return {'codigo':1, 'informacion':'Cargue Exitoso'}
    except Exception as e:
        session.rollback ()
        return {'codigo':0, 'informacion':f'Error en el cargue:{e.args}'}
    finally:
        session.close ()

def add_key_word_resumen(info:schemas.Key_word_Resumen) -> dict:
    data = models.Key_word_Resumen(**info)
    try:
        session.add(data)
        session.commit()
        return {'codigo':1, 'informacion':'Cargue Exitoso'}
    except Exception as e:
        session.rollback ()
        return {'codigo':0, 'informacion':f'Error en el cargue:{e.args}'}
    finally:
        session.close ()

# def get_by_fecha_movil(fecha:date) ->List[dict]:
#     resultado = session.query(models.Info_Escritas_Movil).filter_by(ENVIADO=fecha).all()
#     datos_as_dict = []
#     for dato in resultado:
#         dato_dict = dato.__dict__
#         dato_dict.pop('_sa_instance_state', None)
#         datos_as_dict.append(dato_dict)
#     return datos_as_dict

# def save_registro(registro:schemas.Registros_Datos):
#     registro = models.Registros_Datos(**registro)
#     session.add(registro)
#     session.commit()
#     return 'registro cargado'

global_cate = {'CATEGORY':'english_proficiency'}

add_global_category(global_cate)

word_category = {'CATEGORY':'ICW_words','GLOBAL_CATEGORY_ID':1}
add_word_category(word_category)

key_word = {'WORD':'More cheap','SPEAKER':'Agent','WORD_CATEGORY_ID':1}
add_key_word(key_word)
