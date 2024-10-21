from pymongo import MongoClient
from datetime import datetime
#ket noi den MongoDB

client = MongoClient('mongodb://Localhost:27017/')
db = client['fbData']
users_collection = db['users']

posts_collection = db['posts']

cmt_collection = db['cmt']

users_data = [
{ 'user_id': 1, 'name': "Nguyen Van A", 'email': "a@gmail.com", 'age': 25 },
{ 'user_id': 2, 'name': "Tran Thi B", 'email': "b@gmail.com", 'age': 30 },
{ 'user_id': 3, 'name': "Le Van C", 'email': "c@gmail.com", 'age': 22 }

]

post_data = [
    {'post_id': 1, 'user_id': 1, 'content': "Hôm nay thật đẹp trời!", 'created_at': 'new Date("2024-10-01")'},
    {'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': 'new Date("2024-10-02")'},
    {'post_id': 3, 'user_id': 1, 'content': "Chúc mọi người một ngày tốt lành!", 'created_at': 'new Date("2024-10-03")'}
]
cmt_data = [
{ 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': 'new Date("2024-10-01")' },
{ 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': 'new Date("2024-10-02")' },
{ 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': 'new Date("2024-10-03")' }
]

# users_collection.insert_many(users_data)
# posts_collection.insert_many(post_data)
# cmt_collection.insert_many(cmt_data)

#truy van du lieu

#tim tat ca nguoi dung
print("Tat ca nguoi dung")
for user in users_collection.find():
    print(user)


#Xem tất cả bài đăng của người dùng với user_id = 1

user_post = posts_collection.find({'user_id': 1})
for user in user_post:
    print("bai dang cua nguoi dung voi user_id = 1:\n")
    print(user)


#Xem tất cả bình luận cho bài đăng với post_id = 1

user_cmt = cmt_collection.find({'post_id' : 1})
for user in user_cmt:
    print("bình luận cho bài đăng với post_id = 1:\n",user)


#Truy vấn người dùng có độ tuổi trên 25

user_age = users_collection.find( { "age": { "$gt": 25 } })

for user in user_age:
    print("người dùng có độ tuổi trên 25:\n",user)


#Truy vấn tất cả bài đăng được tạo trong tháng 10

print (" tất cả bài đăng được tạo trong tháng 10\n")
post_in_oct = posts_collection.find({ "created_at": { "$gte": 'new Date("2024-10-01")', '$lt': 'new Date("2024-11-01")' } })
for post in post_in_oct:
    print (post)

#Cập Nhật và Xóa Dữ Liệu
posts_collection.update_one({ 'post_id': 1 }, { '$set': { 'content': "Hôm nay thời tiết thật đẹp!" } })
print("bai post sau khi cap nhat")
for post in posts_collection.find():
    print(post)


#Xóa bình luận với comment_id = 2
print("xoa du lieu")
cmt_collection.delete_one({ 'comment_id': 2 })
for cmt in cmt_collection.find():
    print(cmt)