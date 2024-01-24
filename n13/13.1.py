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
