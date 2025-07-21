import os
import shutil


def organize_nes_games(source_dir, destination_folder="NES_Games", include_subdirs=False):
    # Ensure destination folder exists
    destination_path = os.path.join(source_dir, destination_folder)
    os.makedirs(destination_path, exist_ok=True)

    # Walk through files
    if include_subdirs:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(".nes"):
                    source_file = os.path.join(root, file)
                    dest_file = os.path.join(destination_path, file)
                    if os.path.abspath(source_file) != os.path.abspath(dest_file):
                        shutil.move(source_file, dest_file)
                        print(f"Moved: {source_file} -> {dest_file}")
    else:
        for file in os.listdir(source_dir):
            if file.lower().endswith(".nes"):
                source_file = os.path.join(source_dir, file)
                dest_file = os.path.join(destination_path, file)
                if os.path.abspath(source_file) != os.path.abspath(dest_file):
                    shutil.move(source_file, dest_file)
                    print(f"Moved: {source_file} -> {dest_file}")


def organize_snes_games(source_dir, destination_folder="SNES_Games", include_subdirs=False):
    # Ensure destination folder exists
    destination_path = os.path.join(source_dir, destination_folder)
    os.makedirs(destination_path, exist_ok=True)

    # Walk through files
    if include_subdirs:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(".sfc"):
                    source_file = os.path.join(root, file)
                    dest_file = os.path.join(destination_path, file)
                    if os.path.abspath(source_file) != os.path.abspath(dest_file):
                        shutil.move(source_file, dest_file)
                        print(f"Moved: {source_file} -> {dest_file}")
    else:
        for file in os.listdir(source_dir):
            if file.lower().endswith(".nes"):
                source_file = os.path.join(source_dir, file)
                dest_file = os.path.join(destination_path, file)
                if os.path.abspath(source_file) != os.path.abspath(dest_file):
                    shutil.move(source_file, dest_file)
                    print(f"Moved: {source_file} -> {dest_file}")


def organize_gb_games(source_dir, destination_folder="GB_Games", include_subdirs=False):
    # Ensure destination folder exists
    destination_path = os.path.join(source_dir, destination_folder)
    os.makedirs(destination_path, exist_ok=True)

    # Walk through files
    if include_subdirs:
        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(".gb"):
                    source_file = os.path.join(root, file)
                    dest_file = os.path.join(destination_path, file)
                    if os.path.abspath(source_file) != os.path.abspath(dest_file):
                        shutil.move(source_file, dest_file)
                        print(f"Moved: {source_file} -> {dest_file}")
    else:
        for file in os.listdir(source_dir):
            if file.lower().endswith(".gb"):
                source_file = os.path.join(source_dir, file)
                dest_file = os.path.join(destination_path, file)
                if os.path.abspath(source_file) != os.path.abspath(dest_file):
                    shutil.move(source_file, dest_file)
                    print(f"Moved: {source_file} -> {dest_file}")


if __name__ == "__main__":
    # Replace this with your actual directory path
    source_directory = input("Enter the full path to your NES games folder: ").strip()
    organize_nes_games(source_directory, include_subdirs=True)
    source_directory = input("Enter the full path to your SNES games folder: ").strip()
    organize_snes_games(source_directory, include_subdirs=True)
    source_directory = input("Enter the full path to your GB games folder: ").strip()
    organize_gb_games(source_directory, include_subdirs=True)
