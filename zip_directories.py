import os
import zipfile

def zip_directories_in_current_directory():
    current_directory = os.getcwd()
    
    # Lặp qua tất cả các mục trong thư mục hiện tại
    for item in os.listdir(current_directory):
        item_path = os.path.join(current_directory, item)
        
        # Kiểm tra xem mục đó có phải là một thư mục không
        if os.path.isdir(item_path):
            zip_filename = f"{item}.zip"
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Duyệt qua tất cả các tệp trong thư mục
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Thêm tệp vào tệp zip với tên tương đối
                        zipf.write(file_path, os.path.relpath(file_path, item_path))
            print(f"Đã tạo {zip_filename}")

if __name__ == "__main__":
    zip_directories_in_current_directory()
