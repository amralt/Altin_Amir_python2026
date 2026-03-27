import os
import re
import argparse



def is_there_gitignore(path) -> bool:
    return ".gitignore" in os.listdir(path)


def get_gitignore_content(path) -> list:
    git_ignore_content = []
    with open(os.path.join(path, ".gitignore")) as f:
        for line in f:
            line = line.strip()
            if not line or line[0] == "#":
                continue
            git_ignore_content.append(line)
    return git_ignore_content


def get_all_ignored_files(path):
    if not is_there_gitignore(path):
        return
    
    ingored_files_path = []
    ignored_files = get_gitignore_content(path)

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            for pattern in ignored_files:
                if pattern[0] == "*":
                    if re.search(f"{pattern[1::]}$", file_path,):
                        ingored_files_path.append(f"{file_path} ignored by expression {pattern}")
                        break
                elif re.match(pattern, os.path.relpath(file_path, start=path)):
                    ingored_files_path.append(f"{file_path} ignored by expression {pattern}")
                    break

    return ingored_files_path 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Введите путь до папки с git репозиторием.")
    parser.add_argument(
        "--project_dir", required=True
    )
    args = parser.parse_args()
    path = args.project_dir

    if not os.path.isdir(path):
        raise Exception(f"Error: {path} is not a valid directory.")

    m = get_all_ignored_files(path)
    for i in m:
        print(i)
