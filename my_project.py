# користувач вводить адресу ресурсу
# користувач вводить назву папки куди зберігти
# в папці для кожного запису
# буде створений файл із обраним користувачем полем
# процес створення файлів і ресурсів відбувається у фоновому режимі
# вміст файлів також поле обране користувачем
# користувач вводить номер першого і олстаннього елементу для отримання

'''
from threading import Thread
from multiprocessing import Process
import requests
import os
import time

url = input("Введіть адресу ресурсу:")
folder = input("В яку папку записати дані:")
title_field = input("Яке поле буде назвою файлу:")
text_field = input("Яке поле буде вмістом файлу:")
start_number = int(input("Номер початкового елементу:"))
end_number = int(input("Номер кінцевого елементу:"))

if not os.path.exists(folder):
    os.mkdir(folder)

def action(url,
           folder,
           title_field,
           text_field):
    data = requests.get(url).json()
    with open(f"{folder}/{data[title_field]}","w") as file:
        file.write(data[text_field])

threads = []

for number in range(start_number,end_number):
    t = Thread(target=action,
               args=[url+str(number),
                     folder,
                     title_field,
                     text_field])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
 
print("Виконано успішно")
'''

'''
from threading import Thread
from multiprocessing import Process
import requests
import os
import time

def action(url,
           folder,
           title_field,
           text_field):
    data = requests.get(url).json()
    with open(f"{folder}/{data[title_field]}","w") as file:
        file.write(data[text_field])



def process_action(url,
                   folder,
                   title_field,
                   text_field,
                   start_number,
                   end_number):
    threads = []
    for number in range(start_number,end_number):
        t = Thread(target=action,
                   args=[url+str(number),
                         folder,
                         title_field,
                         text_field])
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()
     
    print("Виконано успішно")   

if __name__ == "__main__":
    while True:
        choice = input("1 обробити адресу q вихід із програми")
        if choice == "1":
            url = input("Введіть адресу ресурсу:")
            folder = input("В яку папку записати дані:")
            title_field = input("Яке поле буде назвою файлу:")
            text_field = input("Яке поле буде вмістом файлу:")
            start_number = int(input("Номер початкового елементу:"))
            end_number = int(input("Номер кінцевого елементу:"))

            if not os.path.exists(folder):
                os.mkdir(folder)
            p = Process(target=process_action,
                        args=[url,
                              folder,
                              title_field,
                              text_field,
                              start_number,
                              end_number])
            p.start()

        if choice == "q":
            break
'''







