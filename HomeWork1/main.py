from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://lytvinenkoi:NRg880hID2oSmdoR@cluster0.hicuj9v.mongodb.net/",
    server_api=ServerApi('1')
)

db = client.cats

def read_from_db(conn, name_to_find:str=""):
    try:   
        if name_to_find=='':
            message = conn.find()
        else:
            message = conn.find({'name': {'$regex': name_to_find}})
    except Exception as e:
        message = f"Error in read_from_db: {e}"
    return message

def update_age(conn, name_to_find:str, new_age:int):
    try:   
        conn.update_one({'name': name_to_find}, {'$set': {'age': new_age}}, False)
        message = conn.find_one({'name': name_to_find})
    except Exception as e:
        message = f"Error in read_from_db: {e}"
    return message


def update_feature(conn, name_to_find:str, new_feature:str):
    try:   
        conn.update_one({'name': name_to_find}, {'$push': {'features': new_feature}}, False)
        message = conn.find_one({'name': name_to_find})
    except Exception as e:
        message = f"Error in read_from_db: {e}"
    return message

def delete_from_db(conn, name_to_find:str):
    try:   
        if name_to_find == '':
            db.cats.delete_many({})
        else:
            db.cats.delete_one({'name': name_to_find})
            message = 'deleted successfully!'
    except Exception as e:
        message = f"Error in read_from_db: {e}"
    return message

if __name__ ==  '__main__':
    # read. use "" for find all, or exact name for find by name
    result = read_from_db(db.cats,'')
    for el in result:
        print(el)

    # updates ages by name
    result = update_age(db.cats,'barsik',5)
    print(result)

    # adds feature by name
    result = update_feature(db.cats,'barsik','добрий')
    print(result)

    # use empty str to delete all, or use name to delete 1 document
    result = delete_from_db(db.cats,'barsik')
    print(result)