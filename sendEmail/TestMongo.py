from pymongo import MongoClient
client = MongoClient("mongodb+srv://blessing:x.bling99@covid-chatbot.afhxi.mongodb.net/chatbot?retryWrites=true&w=majority")
db = client.get_database('chatbot')
records = db.chat_records
print(records.count_documents({}))
new_chat = {
    'name': 'ram',
    'roll_no': 321,
    'branch': 'it'
}



