from pymongo import MongoClient
from datetime import datetime
#ket noi den MongoDB

client = MongoClient('mongodb://Localhost:27017/')
db = client['toptop'] #chon csdl tiktok

#tao cac collections

users_collection = db['users']

videos_collection = db['video']
#them du lieu nguoi dung

users_data = [
    {'user_id': 1, 'username': "user1", 'full_name': "Nguyen Van A", 'followers': 1500, 'following': 200},
    {'user_id': 2, 'username': "user2", 'full_name': "Tran Thi B", 'followers': 2000, 'following': 300},
    {'user_id': 3, 'username': "user3", 'full_name': "Le Van C", 'followers': 500, 'following': 100}

]
#users_collection.insert_many(users_data)
videos_data = [
    {'video_id': 1, 'user_id': 1, 'title': "Video 1", 'views': 10000, 'likes': 500, 'created_at': 'new Date("2024-01-01")'},
    {'video_id': 2, 'user_id': 2, 'title': "Video 2", 'views': 20000, 'likes': 1500, 'created_at': 'new Date("2024-01-05")'},
    {'video_id': 3, 'user_id': 3, 'title': "Video 3", 'views': 5000, 'likes': 200, 'created_at': 'new Date("2024-01-10")'}
]
#videos_collection.insert_many(videos_data)

#truy van du lieu
print("Tat ca nguoi dung")
for user in users_collection.find():
    print(user)


#tim video co nhieu nguoi xem nhat

most_views_video =  videos_collection.find().sort('view',-1).limit(1)

for user in most_views_video:
    print("video co nhieu luot xem nhat:\n",user)

#tim tat ca video cua nguoi dung co username la user1

user_video = videos_collection.find({'user_id': 1})
for video in user_video:
    print('video cua user1:\n', video)

