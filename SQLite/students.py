from symbol import parameters
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

from Tools.scripts.make_ctype import values
from numpy.core.records import record

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("600x800")




def them():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    # Lấy dữ liệu đã nhập
    masv_value = masv.get()
    first_name_value =f_name.get()
    lastName_value = l_name.get()
    malop_value = malop.get()
    namhoc_value = namhoc.get()
    dtb_value = dtb.get()
    # Thực hiện câu lệnh để thêm
    c.execute('''
        INSERT INTO 
        students (masv, first_name, last_name, malop, namhoc, dtb)
        VALUES 
        (:masv, :first_name, :last_name, :malop,:namhoc, :dtb)
    ''',{
        'masv': masv_value,
        'first_name' : first_name_value,
        'last_name' : lastName_value,
        'malop': malop_value,
        'namhoc': namhoc_value,
        'dtb': dtb_value
      }
    )
    conn.commit()
    conn.close()

    # Reset form
    masv.delete(0,END)
    f_name.delete(0, END)
    l_name.delete(0, END)
    malop.delete(0, END)
    namhoc.delete(0, END)
    dtb.delete(0, END)

    # Hien thi lai du lieu
    truy_van()


def xoa():
    #ketnoi va lay dl
    conn = sqlite3.connect('students.db')

    c = conn.cursor()
    c.execute('''
        DELETE FROM
            students
        WHERE id =:id''',
        {'id':delete_box.get()})
    delete_box.delete(0, END)
    conn.commit()
    records = c.fetchall()

    # Nếu không có bản ghi nào với ID đã nhập, thông báo lỗi
    messagebox.showinfo("Thông báo", "Đã xóa!")
    conn.close()

    if not records:
        messagebox.showerror("Lỗi", "ID khong ton tai!!!")
        conn.close()
    truy_van()

def cap_nhat():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    record_id = f_id_editor.get()
    # Kiểm tra nếu ID đã bị thay đổi
    if record_id != delete_box.get():
        messagebox.showerror("Lỗi", "ID không thể chỉnh sửa!")
        conn.close()
        return  # Dừng việc cập nhật nếu ID bị thay đổi

    c.execute("""UPDATE students SET
           masv = :masv,
           first_name = :first,
           last_name = :last,
           malop = :malop,
           namhoc = :namhoc,
           dtb = :dtb
           WHERE id = :id""",
              {
                  'masv': masv_editor.get(),
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'malop': malop_editor.get(),
                  'namhoc': namhoc_editor.get(),
                  'dtb': dtb_editor.get(),
                  'id': record_id
              })

    conn.commit()
    conn.close()
    editor.destroy()

    # Cập nhật lại danh sách bản ghi sau khi chỉnh sửa
    truy_van()

def truy_van():
    #xoa di cac du lieu trong treeview
    for row in tree.get_children():
        tree.delete(row)
    # Kết nối tới db
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    # c.execute('''
    #        CREATE TABLE students(
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             masv text,
    #             first_name text,
    #             last_name text,
    #             malop text,
    #             namhoc text,
    #             dtb text
    #         )
    #     '''
    #           )
    c.execute("SELECT oid, * FROM students")
    record = c.fetchall()

    #hien thi du lieu
    for r in record:
        tree.insert("" , END,values=(r[0],r[2],r[3],r[4],r[5],r[6],r[7]))
def chinh_sua():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x300")

    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM students WHERE id=:id", {'id': record_id})
    records = c.fetchall()
    # Nếu không có bản ghi nào với ID đã nhập, thông báo lỗi
    if not records:
        messagebox.showerror("Lỗi", "Mòi bạn điền lại ID!!!")
        conn.close()
        return



    global f_id_editor,masv_editor, f_name_editor, l_name_editor, malop_editor, namhoc_editor, dtb_editor

    f_id_editor = Entry(editor, width=30)
    f_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    masv_editor = Entry(editor, width=30)
    masv_editor.grid(row=1, column=1, padx=20)
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=2, column=1)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=3, column=1)
    malop_editor = Entry(editor, width=30)
    malop_editor.grid(row=4, column=1)
    namhoc_editor = Entry(editor, width=30)
    namhoc_editor.grid(row=5, column=1)
    dtb_editor = Entry(editor, width=30)
    dtb_editor.grid(row=6, column=1)


    f_id_label = Label(editor, text="ID")
    f_id_label.grid(row=0, column=0, pady=(10, 0))
    f_masv_label = Label(editor, text="Mã sinh viên")
    f_masv_label.grid(row=1, column=0)
    l_name_label = Label(editor, text="Họ")
    l_name_label.grid(row=3, column=0)
    f_name_label = Label(editor, text="Tên")
    f_name_label.grid(row=2, column=0)
    malop_label = Label(editor, text="Mã lớp")
    malop_label.grid(row=4, column=0)
    namhoc_label = Label(editor, text="Năm nhập học")
    namhoc_label.grid(row=5, column=0)
    dtb_label = Label(editor, text="Điểm trung bình")
    dtb_label.grid(row=6, column=0)

    for record in records:
        f_id_editor.insert(0, record[0])
        masv_editor.insert(0, record[1])
        f_name_editor.insert(0, record[2])
        l_name_editor.insert(0, record[3])
        malop_editor.insert(0, record[4])
        namhoc_editor.insert(0, record[5])
        dtb_editor.insert(0, record[6])

    #f_id_editor.config(state='disabled')


    edit_btn = Button(editor, text="Lưu bản ghi", command=cap_nhat)
    edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
masv = Entry(input_frame, width=30)
masv.grid(row=0, column=1, padx=20, pady=(10, 0))
f_name = Entry(input_frame, width=30)
f_name.grid(row=1, column=1)
l_name = Entry(input_frame, width=30)
l_name.grid(row=2, column=1)
malop = Entry(input_frame, width=30)
malop.grid(row=3, column=1)
namhoc = Entry(input_frame, width=30)
namhoc.grid(row=4, column=1)
dtb = Entry(input_frame, width=30)
dtb.grid(row=5, column=1)

# Các nhãn
masv_label = Label(input_frame, text="Mã sinh viên")
masv_label.grid(row=0, column=0, pady=(10, 0))
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=1, column=0)
l_name_label = Label(input_frame, text="Tên")
l_name_label.grid(row=2, column=0)
malop_label = Label(input_frame, text="Mã lớp")
malop_label.grid(row=3, column=0)
namhoc_label = Label(input_frame, text="Năm nhập học")
namhoc_label.grid(row=4, column=0)
dtb_label = Label(input_frame, text="Điểm trung bình")
dtb_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
delete_box_label = Label(button_frame, text="Chọn ID")
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị bản ghi", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

columns = ("id", "masv", "first_name", "last_name", "malop", "namhoc", "dtb")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=7)
tree.pack()

# Định nghĩa tiêu đề cho các cột
tree.heading("id", text="ID")
tree.heading("masv", text="Mã số sinh viên")
tree.heading("first_name", text="Họ")
tree.heading("last_name", text="Tên")
tree.heading("malop", text="Mã lớp")
tree.heading("namhoc", text="Năm nhập học")
tree.heading("dtb", text="Điểm trung bình")


# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()

root.mainloop()