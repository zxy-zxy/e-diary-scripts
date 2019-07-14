# e-diary scripts

Файл *scripts.py* содержит скрипты для задания из курса [dvmn](https://dvmn.org).
Репозиторий с django приложением находится по адресу https://github.com/devmanorg/e-diary/tree/master.

## Usage
* *fix_marks* изменяет объекты модели **Mark** с негативными показателями (2 и 3) на 4 и 5 для выбранного объекта schoolkid.
* *remove_chastisements* удаляет объекты  **Chastisements** для переданного schoolkid.
*  *commend_kid* создает объект модели **Commendation** для переданного schoolkid и названия предмета subject_title.

## Project goals
The code is written for educational purposes. 
Training course for web-developers[dvmn](https://dvmn.org).