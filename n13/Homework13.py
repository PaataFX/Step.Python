# კოდი აძლევს მომხარებელს საშუალებას, შეიყვანოს ინფორმაცია იქამდე სანამ არ დააბრეიქებს, ეს ინფრომაცია ინახება txt ფაილში
def write_to_file():
    file_name = "user_data.txt"

    with open(file_name, "w") as file:
        while True:
            user_input = input("Enter information (type 'enough' to stop): ")
            
            if user_input.lower() == "enough":
                print("Writing to file is complete.")
                break
            
            file.write(user_input + "\n")

if __name__ == "__main__":
    write_to_file()

# პოულობს შეყვანილ საქაღალდეს სისტემაში. ქმინის შესაბამის ფაილს. პრინტავს იმ საქაღალდეში არსებული სხვა ფაილების სახელებს
import os

def create_file_and_list_files():
    folder_location = input("Enter the folder location: ")
    file_name = input("Enter the file name: ")

    file_path = os.path.join(folder_location, file_name)

    try:
        with open(file_path, "w") as file:
            print(f"File '{file_name}' created successfully at {folder_location}.")
    except IOError as e:
        print(f"Error creating the file: {e}")
        return

    print(f"\nList of files in {folder_location}:")
    try:
        files_in_folder = os.listdir(folder_location)
        for file in files_in_folder:
            print(file)
    except FileNotFoundError:
        print(f"Folder '{folder_location}' not found.")
    except PermissionError:
        print(f"Permission error accessing '{folder_location}'. Check your permissions.")

if __name__ == "__main__":
    create_file_and_list_files()