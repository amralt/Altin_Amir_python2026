import os
import argparse
import time
import logging

logger = logging.getLogger("deleted trash")


def log(f) :
    def wrapper(*args, **qwargs):
        logging.basicConfig(filename="trash_deleter.log", level=logging.INFO)
        logger.info('Started')
        result = f(*args, **qwargs)
        logger.info('Finished')
        return result
    
    return wrapper


def delete_trash(path :str, age_thr: int):

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_age = time.time() - os.path.getmtime(file_path)
            if file_age > age_thr:
                os.remove(file_path)
                logger.info(f"Deleted: {file_path}")
        for dir in dirs:
            dir_age = time.time() - os.path.getmtime(os.path.join(root, dir))
            if not os.listdir(os.path.join(root, dir)) and dir_age > age_thr:
                os.rmdir(os.path.join(root, dir))


@log
def main():
    parser = argparse.ArgumentParser(description="Введите путь до папки и время жизни мусора.")
    parser.add_argument(
        "--trash_folder_path", required=True
    )
    parser.add_argument(
        "--age_thr", required=True
    )
    args = parser.parse_args()
    trash_folder_path = args.trash_folder_path
    age_thr = int(args.age_thr)

    if not os.path.isdir(trash_folder_path):
        raise Exception(f"Error: {trash_folder_path} is not a valid directory.")
    
    delete_trash(trash_folder_path, age_thr)
    time.sleep(1)
    delete_trash(trash_folder_path, age_thr)


if __name__ == "__main__":
    main()
