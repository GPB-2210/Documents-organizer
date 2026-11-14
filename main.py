import os
import shutil

from datetime import datetime
from tkinter import Tk, filedialog

#Mapear as extensões dos arquivos
def create_default_extentions_map():
    return {
        "Images": [".jpeg", ".png", ".jpg", ".heic", ".gif"],
        "Videos": [".mp4", ".mkv", ".mov", ".flv"],
        "Documents": [".pdf", ".docx", ".doc",".txt", ".ppt", ".pptx", ".xls", "xlsx"],
        "Music": [".mp3", ".wav", ".ogg"],
        "Code": [".py", ".html", "js", "css"],
        "Archives": [".zip", ".rar", ".7z"],
        "Others": [],
    }

#Encontrar nome da pasta apropriada para arquivo
def get_folder_for_extentions(extension, extension_map):
    for folder, extensions in extension_map.items():
        if extension in extensions:
            return folder

    return "Others"

#mover arquivo para pasta apropriada
def move_file(file_path, folder_name, directory):
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    new_path = shutil.move(file_path, folder_path)
    print(f"moved {os.path.basename(file_path)} to {folder_path}")
    return new_path

#organizar arquivos
def organize_by_extension(directory):
    extensions_map = create_default_extentions_map()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(file_path)[1].lower()
            folder_name = get_folder_for_extentions(extension, extensions_map)
            move_file(file_path, folder_name, directory)

# Organizar arquivos por data
def organize_by_date(directory):
    extensions_map = create_default_extentions_map()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
           created_at = datetime.fromtimestamp(os.path.getctime(file_path))
           folder_name = created_at.strftime("%Y-%m-%d")
           move_file(file_path, folder_name, directory)

def main():
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Selecione o Diretório")
    if not directory:
        print("o diretório selecionado não existe")
        return

    while True:
        print("\nFILE ORGANIZER - escolha uma opção:")
        print("1. Organizar por tipo de arquivo")
        print("2. Organizar por Data")
        print("3. Sair")

        escolha = int(input("escolha sua opção (1-3): "))

        match escolha:
            case 1:
                organize_by_extension(directory)
            case 2:
                organize_by_date(directory)
            case 3:
                break
            case _:
                print("desculpe, opção invalida, tente novamente")

if __name__ == "__main__":
    main()