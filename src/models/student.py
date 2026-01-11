from users import User
"""Ke thua tu User"""
class Student:
    def __init__(self, student_id, full_name, email, phone):
        """
        Khởi tạo đối tượng Sinh viên.
        """
        self.student_id = student_id
        self.full_name = full_name
        self.email = email
        self.phone = phone

    def to_dict(self):
        """
        Chuyển đổi đối tượng thành Dictionary (để trả về JSON/API).
        """
        return {
            "id": self.student_id,
            "name": self.full_name,
            "email": self.email,
            "phone": self.phone
        }