from pymongo import MongoClient
client = MongoClient("mongodb+srv://blessing:x.bling99@covid19.afhxi.mongodb.net/<covid19>?retryWrites=true&w=majority")
db = client.get_database('covid19')
records = db.chat_records
print(records.count_documents({}))
new_chat = {
    'name': 'ram',
    'roll_no': 321,
    'branch': 'it'
}
records.remove()


