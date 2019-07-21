# e-diary scripts

Файл *scripts.py* содержит скрипты для задания из курса [dvmn](https://dvmn.org).
Репозиторий с django приложением находится по адресу https://github.com/devmanorg/e-diary

## Usage
* *fix_marks* изменяет объекты модели **Mark** с негативными показателями (2 и 3) на 4 и 5 для выбранного объекта schoolkid.
* *commend_kid* создает объект модели **Commendation** для переданного schoolkid и названия предмета subject_title.
* *remove_chastisements* удаляет объекты  **Chastisements** для переданного schoolkid.
### Example
```python
from datacenter.models import Schoolkid
from datacenter.scripts import remove_chastisements

schoolkid_name = '<put_your_name_here>'
schoolkid_obj = Schoolkid.objects.get(full_name__icontains=schoolkid_name)
remove_chastisements(schoolkid_obj)
```

## Project goals
The code is written for educational purposes. 
Training course for web-developers[dvmn](https://dvmn.org).