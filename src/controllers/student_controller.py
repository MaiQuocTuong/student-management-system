# src/controllers/student_controller.py
from src.models.student import Student
from src.database.connection import DatabaseConnection

class StudentController:
    def get_all_students(self):
        """
        Lấy danh sách tất cả sinh viên.
        """
        # Logic gọi DB để lấy dữ liệu
        print("Đang lấy danh sách sinh viên...")
        return []

    def get_student_by_id(self, student_id):
        """
        Tìm sinh viên theo ID.
        """
        print(f"Đang tìm sinh viên có ID: {student_id}")
        return None
    def get_student_by_name(self , student_name) :
        """
        Tìm sinh viên theo ID.
        """
        print(f"Đang tìm sinh viên có Ten: {student_name}")
        return None
    def create_student(self, data):
        """
        Tạo mới một sinh viên.
        """
        # Validate dữ liệu đầu vào
        new_student = Student(data['id'], data['name'], data['email'], data['phone'])
        print(f"Đã tạo sinh viên: {new_student.full_name}")
        return new_student

    def update_student(self, student_id, data):
        """
        Cập nhật thông tin sinh viên.
        """
        pass

    def delete_student(self, student_id):
        """
        Xóa sinh viên.
        """
        pass