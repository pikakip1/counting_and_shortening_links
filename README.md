# Скрипт для обрезки ссылок с помощью Битли

При передаче длинной ссылки, программа создает и возвращает укороченную версию    
При передаче укороченной версии ссылки, программа возвращает количество переходов по ней      

# Требования для запуска программы

Для успешного запуска программы, установите две библиотеки   
С помощью команды  
```
pip install requests

pip install python-dotenv
```

Актуальная версия requests и python-dotenv есть в файле requirements.txt  

# Переменные окружения

Для установки собственного API ключа, требуется создать файл TOKEN_BITLINK.env в папке с программой   
Внутри файла должен быть токен в виде BITLY_TOKEN={ваш токен}  

# Запуск

Скопируйте и вставьте код из файла Count_clicks_on_links.py  

Запустите код через консоль и введите вашу ссылку:   

При передаче неукороченной версии ссылки:  
```
https://www.deepl.com/ru/translator
```

Программа выводит:  
```
Укороченная ссылка: https://bit.ly/3XrcPps
```

При передаче укороченной версии ссылки, программа выведет количество переходов по ней  
``` 
Количество переходов: https://bit.ly/3XrcPps
```

```
3
```
