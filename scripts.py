import random

from django.db.models.aggregates import Count

from datacenter.models import Schoolkid, Mark, Сhastisement, Lesson, Commendation


def fix_marks(schoolkid: Schoolkid):
    negative_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    for negative_mark in negative_marks:
        negative_mark.points = random.randint(4, 5)
        negative_mark.save()


def remove_chastisements(schoolkid: Schoolkid):
    Сhastisement.objects.filter(schoolkid=schoolkid).delete()


commend_texts = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!",
]


def commend_kid(schoolkid: Schoolkid, subject_title: str):
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__iexact=subject_title,
    )

    count = lessons.aggregate(count=Count('id'))['count']
    random_index = random.randint(0, count - 1)

    lesson_to_commend = lessons[random_index]
    commend = Commendation(
        schoolkid=schoolkid,
        teacher=lesson_to_commend.teacher,
        subject=lesson_to_commend.subject,
        created=lesson_to_commend.date,
        text=random.choice(commend_texts),
    )
    commend.save()
