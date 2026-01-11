import os
from src.controllers.student_controller import StudentController

class StudentView:
    def __init__(self):
        # View sẽ nắm giữ Controller để nhờ Controller xử lý dữ liệu
        self.controller = StudentController()

    def show_menu(self):
        """
        Hiển thị menu quản lý sinh viên và điều hướng chức năng.
        """
        while True:
            print("\n" + "="*40)
            print("   QUẢN LÝ SINH VIÊN")
            print("="*40)
            print("1. Xem danh sách sinh viên")
            print("2. Thêm sinh viên mới")
            print("3. Cập nhật thông tin sinh viên")
            print("4. Xóa sinh viên")
            print("5. Tìm kiếm sinh viên")
            print("0. Quay lại menu chính")
            print("="*40)
            
            choice = input("Mời bạn chọn chức năng (0-5): ")

            if choice == '1':
                self.display_list()
            elif choice == '2':
                self.add_student_ui()
            elif choice == '3':
                self.update_student_ui()
            elif choice == '4':
                self.delete_student_ui()
            elif choice == '5':
                self.search_student_ui()
            elif choice == '0':
                print("Đã thoát menu sinh viên.")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng thử lại!")

    def display_list(self):
        """
        Lấy dữ liệu từ Controller và in ra màn hình dạng bảng.
        """
        students = self.controller.get_all_students()
        
        if not students:
            print("\n[Thông báo] Danh sách sinh viên đang trống!")
            return

        print("\nDANH SÁCH SINH VIÊN:")
        # Định dạng cột: ID (10 ký tự), Tên (25 ký tự), Email (25 ký tự), SĐT (15 ký tự)
        print(f"{'Mã SV':<10} {'Họ và Tên':<25} {'Email':<25} {'SĐT':<15}")
        print("-" * 75)
        
        for sv in students:
            # Giả sử object sv có các thuộc tính tương ứng
            print(f"{sv.student_id:<10} {sv.full_name:<25} {sv.email:<25} {sv.phone:<15}")

    def add_student_ui(self):
        """
        Giao diện nhập liệu để thêm mới.
        """
        print("\n--- THÊM SINH VIÊN MỚI ---")
        student_id = input("Nhập Mã SV: ")
        full_name = input("Nhập Họ Tên: ")
        email = input("Nhập Email: ")
        phone = input("Nhập Số điện thoại: ")

        # Đóng gói dữ liệu thành dict
        data = {
            "id": student_id,
            "name": full_name,
            "email": email,
            "phone": phone
        }

        # Gọi Controller để xử lý logic thêm
        try:
            new_student = self.controller.create_student(data)
            print(f"\n[Thành công] Đã thêm sinh viên: {new_student.full_name}")
        except Exception as e:
            print(f"\n[Lỗi] Không thể thêm sinh viên. Chi tiết: {e}")

    def update_student_ui(self):
        """
        Giao diện sửa thông tin.
        """
        print("\n--- CẬP NHẬT THÔNG TIN ---")
        student_id = input("Nhập Mã SV cần sửa: ")
        
        # Kiểm tra xem SV có tồn tại không trước khi nhập dữ liệu mới
        student = self.controller.get_student_by_id(student_id)
        if not student:
            print(f"[Lỗi] Không tìm thấy sinh viên có mã {student_id}")
            return

        print(f"Đang sửa thông tin cho: {student.full_name}")
        print("(Bỏ trống và nhấn Enter nếu không muốn thay đổi thông tin đó)")
        
        new_name = input(f"Họ tên mới ({student.full_name}): ")
        new_email = input(f"Email mới ({student.email}): ")
        new_phone = input(f"SĐT mới ({student.phone}): ")

        data_update = {}
        if new_name: data_update['name'] = new_name
        if new_email: data_update['email'] = new_email
        if new_phone: data_update['phone'] = new_phone

        if self.controller.update_student(student_id, data_update):
            print("\n[Thành công] Cập nhật hoàn tất!")
        else:
            print("\n[Thất bại] Có lỗi xảy ra khi cập nhật.")

    def delete_student_ui(self):
        """
        Giao diện xóa sinh viên.
        """
        print("\n--- XÓA SINH VIÊN ---")
        student_id = input("Nhập Mã SV cần xóa: ")
        
        confirm = input(f"Bạn có chắc chắn muốn xóa SV {student_id}? (y/n): ")
        if confirm.lower() == 'y':
            if self.controller.delete_student(student_id):
                print(f"\n[Thành công] Đã xóa sinh viên {student_id}")
            else:
                print(f"\n[Lỗi] Không tìm thấy hoặc không thể xóa.")

    def search_student_ui(self):
        """
        Giao diện tìm kiếm.
        """
        keyword = input("\nNhập tên hoặc mã SV để tìm: ")
        results = self.controller.search_student(keyword)
        
        if results:
            print(f"\nTìm thấy {len(results)} kết quả:")
            print(f"{'Mã SV':<10} {'Họ và Tên':<25}")
            for sv in results:
                print(f"{sv.student_id:<10} {sv.full_name:<25}")
        else:
            print("Không tìm thấy kết quả nào.")