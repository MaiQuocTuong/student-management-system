class DatabaseConnection:
    def __init__(self):
        # Thông tin cấu hình DB (host, user, pass, v.v.)
        self.connection_string = "..."

    def connect(self):
        """
        Thiết lập kết nối đến cơ sở dữ liệu.
        """
        print("Đang kết nối đến Database...")
        # Code kết nối thực tế sẽ nằm ở đây
        return True

    def disconnect(self):
        """
        Đóng kết nối.
        """
        print("Đã đóng kết nối Database.")
