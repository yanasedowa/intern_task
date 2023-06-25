# intern_task
Тестовое задание (создание видео бегущей строки)

### Описание

**intern_task** — это тестовое задание для вакансии стажер python в компанию АйТи-Солюшн. Задание заключается в написании кода для создания бегущей строки.


### Основной функционал проекта:
> -   создание видео бегущей строки с текстом, вводимым пользователем, с использованием библиотеки moviepy;
> -   размер создаваемого видео 100х100, длительность 3 секунды, цвет фона розовый, цвет текста белый;
> -   скорость бегущей строки подстраивается под длину строки;
> -   после создания видео предлагает сохранение на пк.

### Как запустить проект:
На macOS или Linux запустите программу Терминал. 
Если у вас Windows — запускайте [Git Bash](https://gitforwindows.org/)

Установите интерпретатор Python 3.9

Для Windows:
www.python.org/downloads/#

Для MacOS:

```
brew install python@3.79
```

Для Linux (Ubuntu):

```
sudo apt-get install python3.9
```


  

Клонировать репозиторий и перейти в него в командной строке:

  

```

git clone git@github.com:yanasedowa/intern_task.git

```

  

```

cd intern_task

```

  

Cоздать и активировать виртуальное окружение:

  

```

python3 -m venv env

```

  

Для *nix-систем:

```

source venv/bin/activate

```

Для windows-систем:

```

source venv/Scripts/activate

```
  

```

python3 -m pip install --upgrade pip

```

  

Установить зависимости из файла requirements.txt:

  

```

pip install -r requirements.txt

```



Установить на ПК ImageMagick:


```

https://imagemagick.org/script/download.php

```



Прописать в файле conf.py в переменной IMAGEMAGICK_BINARY путь к ImageMagick.



Выполнить миграции:

  

```

python3 manage.py migrate

```

  

Запустить проект:

  

```

python3 manage.py runserver

```

