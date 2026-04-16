


class FileManager:
    def write_file(self,file_path,content):
        file = open(file_path, "w")
        file.write(content)
        file.close()
        return f"{file_path}"

    def read_file(self,file_path):
        file = open(file_path, "r")
        content = file.read()
        return content


def main():
   
    print("Welcome to my file handling software")
   
    user_file_choice = int(input("Press 1 to Write a file\nPress 2 to Read a file: "))
   
    if user_file_choice == 1:
     
     file_manager = FileManager()

     file_name = input("Enter the name of the text file (with .txt extension): ")
     content = input("Enter the content to write to the file: ")

    
     write_result = file_manager.write_file(file_name, content)
     print(write_result)

    
     read_result = file_manager.read_file(file_name)
     print("Content of the file:")
     print(read_result)


    if user_file_choice == 2:
     file_manager = FileManager()

     file_name = input("Enter the name of the file you want to read (with .txt extension): ")

    
     read_result = file_manager.read_file(file_name)
     print("Content of the file:")
     print(read_result)
    


if __name__ == "__main__":
    main()