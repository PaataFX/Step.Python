import csv

def copy_csv_to_txt(csv_file, txt_file):
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            names = [row[0] for row in reader]

        with open(txt_file, 'w', encoding='utf-8') as txt_file:
            for name in names:
                txt_file.write(name + '\n')

        print(f"Successfully copied information from '{csv_file}' to '{txt_file}'.")
    except FileNotFoundError:
        print(f"Error: '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_file_path = "names.csv"
    txt_file_path = "names.txt"

    copy_csv_to_txt(csv_file_path, txt_file_path)
