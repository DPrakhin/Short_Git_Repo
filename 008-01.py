"""
Міні проект з розробки файлової Бази Даних
Реалізація за допомогою простих класів
"""
import json
import os
import pickle

class JsonFileWorker:
    def __init__(self,file):
        self.file = file
        if not os.path.exists(file):
            self.write([])

    def read(self):
        with open(self.file,"r") as file:
            return json.loads(file.read())

    def write(self,data):
        with open(self.file,"w") as file:
            file.write(json.dumps(data))


class PickleFileWorker:
    def __init__(self,file):
        self.file = file
        if not os.path.exists(file):
            self.write([])

    def read(self):
        with open(self.file,"rb") as file:
            return pickle.loads(file.read())

    def write(self,data):
        with open(self.file,"wb") as file:
            file.write(pickle.dumps(data))


class Db:
    def __init__(self,file,data_format = "json"):
        file_workers = {"json":JsonFileWorker,
                        "byte":PickleFileWorker}
        self.file_worker = file_workers.get(data_format)(file)
        self.data = self.file_worker.read()

    def __str__(self):
        return str(self.data)

    def append(self,element):
        self.data.append(element)
        self.file_worker.write(self.data)

    def pop(self,index):
        result = self.data.pop(index)
        self.file_worker.write(self.data)
        return result

    def remove(self,element):
        result = self.data.remove(element)
        self.file_worker.write(self.data)
        return result

    def clear(self):
        self.data.clear()
        self.file_worker.write(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        return self.data[index]


# === ОСНОВНА ПРОГРАМА === #
db = Db("data.json", data_format="json")
db.clear()

db.append("1st element")
db.append("2nd element")
db.append("3rd element")
db.append("4th element")
print(db)

db.remove("2nd element")
print(db)

