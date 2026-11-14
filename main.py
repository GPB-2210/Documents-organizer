import shutil
from datetime import datetime
from pathlib import Path
from tkinter import Tk, filedialog


EXTENSIONS_BY_FOLDER = {
    "Images": {".jpeg", ".png", ".jpg", ".heic", ".gif", ".webp", ".svg"},
    "Videos": {".mp4", ".mkv", ".mov", ".flv", ".avi"},
    "Documents": {".pdf", ".docx", ".doc", ".txt", ".ppt", ".pptx",
        ".xls", ".xlsx", ".csv", ".odt", ".ods",},
    "Music": {".mp3", ".wav", ".ogg", ".flac", ".m4a"},
    "Code": {".py", ".html", ".js", ".css", ".java", ".cpp", ".json"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}


def get_folder_for_extension(extension):
    #Retorna a categoria correspondente à extensão do arquivo.
    for folder, extensions in EXTENSIONS_BY_FOLDER.items():
        if extension.lower() in extensions:
            return folder

    return "Others"


def create_move_plan(directory, organize_by):
    #Prepara os destinos sem mover os arquivos.
    moves = []
    reserved_destinations = set()

    for source in sorted(directory.iterdir()):
        if not source.is_file():
            continue

        if organize_by == "type":
            folder_name = get_folder_for_extension(source.suffix)
        else:
            modified_at = datetime.fromtimestamp(source.stat().st_mtime)
            folder_name = modified_at.strftime("%Y-%m-%d")

        destination_folder = directory / folder_name
        destination = destination_folder / source.name
        original_destination = destination
        counter = 1

        while destination.exists() or destination in reserved_destinations:
            destination = original_destination.with_name(
                f"{original_destination.stem} ({counter}){original_destination.suffix}"
            )
            counter += 1

        moves.append((source, destination))
        reserved_destinations.add(destination)

    return moves


def organize_files(directory, organize_by):
    #Mostra uma prévia e move os arquivos após confirmação.
    moves = create_move_plan(directory, organize_by)

    if not moves:
        print("Não há arquivos para organizar nessa pasta.")
        return

    print("\nPrévia das alterações:")
    for source, destination in moves:
        destination_in_folder = destination.relative_to(directory)
        print(f"  {source.name} -> {destination_in_folder}")

    confirmation = input("\nDeseja continuar? (S/N): ").strip().lower()
    if confirmation != "s":
        print("Operação cancelada. Nenhum arquivo foi movido.")
        return

    for source, destination in moves:
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(destination))
            print(f"Movido: {source.name}")
        except OSError as error:
            print(f"Não foi possível mover {source.name}: {error}")


def choose_directory():
    #Abre a janela para selecionar a pasta que será organizada.
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Selecione a pasta")
    root.destroy()

    if not directory:
        return None

    return Path(directory)


def main():
    directory = choose_directory()
    if directory is None:
        print("Nenhuma pasta foi selecionada. Encerrando.")
        return

    while True:
        print("\nORGANIZADOR DE ARQUIVOS")
        print("1. Organizar por tipo de arquivo")
        print("2. Organizar por data de modificação")
        print("3. Sair")

        choice = input("Escolha uma opção (1-3): ").strip()

        if choice == "1":
            organize_files(directory, "type")
        elif choice == "2":
            organize_files(directory, "date")
        elif choice == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()
