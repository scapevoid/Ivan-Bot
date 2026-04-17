
import getpath
path = getpath.pathreturn()
import os
import re
from datetime import datetime

def log_error(message: str):
    """Логирует ошибку в файл"""
    with open("exdb_error.log", "a", encoding="UTF-8") as log:
        log.write(f"[{datetime.now()}] {message}\n")

def exdb(data: str, number: int, id: int) -> bool:
    # --- Проверка типов ---
    if not isinstance(data, str):
        log_error("Неверный тип: data должно быть строкой.")
        return False
    if not isinstance(number, int) or number < 0:
        log_error(f"Неверный индекс number: {number}")
        return False
    if not isinstance(id, int) or id < 0:
        log_error(f"Неверный ID: {id}")
        return False

    # --- Замена опасных символов ---
    data = data.replace(",", " ") \
               .replace("\n", " ") \
               .replace("\r", " ") \
               .replace("\t", " ") \
               .replace("\"", "'") \
               .replace("\\", "/")


    filepath = os.path.join(path, f"{id}_id")

    # --- Чтение данных ---
    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            raw = file.readline().strip()
            raw = raw.rstrip(", ")
            data_list = raw.split(", ") if raw else []
    except FileNotFoundError:
        data_list = []
    except Exception as e:
        log_error(f"Ошибка чтения файла '{filepath}': {e}")
        return False

    # --- Обеспечим нужную длину ---
    if number >= len(data_list):
        data_list.extend([""] * (number - len(data_list) + 1))

    # --- Обновляем значение ---
    data_list[number] = data

    # --- Запись обратно ---
    try:
        with open(filepath, "w", encoding="UTF-8") as file:
            file.write(", ".join(data_list) + ", ")
    except Exception as e:
        log_error(f"Ошибка записи в файл '{filepath}': {e}")
        return False

    return True




def createdb(user_id):
    try:
        file = open(f"{path}{user_id}_id", "x")
        file.write(f"{user_id}, ")
        file.close()
    except Exception as e:
        print(f"Error creating file: {e}\nWaiting to create new db")
        return
    return
