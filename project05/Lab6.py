from pymongo import MongoClient
from datetime import datetime
#ket noi den MongoDB

client = MongoClient('mongodb://Localhost:27017/')
db = client['fileManagement']


files_collection = db['files']

files_data = [
    { 'file_id': 1, 'name': "Report.pdf", 'size': 2048, 'owner': "Nguyen Van A", 'created_at': 'new Date("2024-01-10")', 'shared': 'false' },
    { 'file_id': 2, 'name': "Presentation.pptx", 'size': 5120, 'owner': "Tran Thi B", 'created_at': 'new Date("2024-01-15")', 'shared': 'true' },
    { 'file_id': 3, 'name': "Image.png", 'size': 1024, 'owner': "Le Van C", 'created_at': 'new Date("2024-01-20")', 'shared': 'false' },
    { 'file_id': 4, 'name': "Spreadsheet.xlsx", 'size': 3072, 'owner': "Pham Van D", 'created_at': 'new Date("2024-01-25")', 'shared': 'true' },
    { 'file_id': 5, 'name': "Notes.txt", 'size': 512, 'owner': "Nguyen Thi E", 'created_at': 'new Date("2024-01-30")', 'shared': 'false' }
]

#files_collection.insert_many(files_data)

#tim tat ca files
print("Tat ca cac files:")
for file in files_collection.find():
    print(file)

#Tìm tệp có kích thước lớn hơn 2000KB

print('Tệp có kích thước lớn hơn 2000KB:')
tep_2000KB = files_collection.find({ 'size': { '$gt': 2000 } })

for tep in tep_2000KB:
    print(tep)


# Tìm tất cả tệp được chia sẻ
print('tất cả tệp được chia sẻ:')
shared_files = files_collection.find({'shared': 'true'})

for files in shared_files:
    print(files)
#Thống kê số lượng tệp theo chủ sở hữu
print("số lượng tệp theo chủ sở hữu")
files_gr = files_collection.aggregate([
    { '$group': {'_id': "$owner", 'count': { '$sum': 1}}}
])
for file in files_gr:
    print(file)

#cau 1 :Tìm tất cả tệp của người dùng có tên là "Nguyen Van A".
print('Tất cả tệp của người dùng có tên là "Nguyen Van A":')
user_nguyenvanA = files_collection.find({'owner':'Nguyen Van A'})
for user in user_nguyenvanA:
    print(user)

#Câu 2: Tìm tệp lớn nhất trong bộ sưu tập.
tep_lon_nhat = files_collection.find().sort({ 'size': -1 }).limit(1)
print("Tep lon nhat la:")
for tep in tep_lon_nhat:
    print(tep)


#Câu 3: Tìm số lượng tệp có kích thước nhỏ hơn 1000KB.
tep_nho_hon_1000KB = files_collection.find({'size':{'$lt': 1000}})
print("Tep co kich thuoc nho hon 1000KB:")
for tep in tep_nho_hon_1000KB:
    print(tep)

#Câu 4: Tìm tất cả tệp được tạo trong tháng 1 năm 2024.

file_in_jan_2024 = files_collection.find({
    'created_at': {
        '$gte' : 'new Date("2024-01-01")',
        '$lt' : 'new Date("2024-02-01")'
    }
})
print("tất cả tệp được tạo trong tháng 1 năm 2024.")
for tep in file_in_jan_2024:
    print(tep)

#Câu 5: Cập nhật tên tệp với `file_id` là 4 thành "New Spreadsheet.xlsx".

files_collection.update_one({ 'file_id': 4 }, { '$set': { 'name': "New Spreadsheet.xlsx" } })

files_collection.delete_many({'size':{'$lt': 1000}})

#tim tat ca files
print("Tat ca cac files:")
for file in files_collection.find():
    print(file)