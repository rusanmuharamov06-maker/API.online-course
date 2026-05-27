# API.online-course

## Описание проекта

API для платформы онлайн-обучения. Позволяет управлять курсами, преподавателями, студентами и отзывами.

## Функционал

- GET /teachers/ - список преподавателей
- GET /teachers/{id}/ - один преподаватель
- POST /teachers/ - создать преподавателя
- POST /teachers/ (со списком) - массовое создание
- PATCH /teachers/{id}/ - обновить преподавателя
- DELETE /teachers/{id}/ - удалить преподавателя
- DELETE /teachers/?ids=1,2,3 - массовое удаление

- GET /courses/ - список курсов
- GET /courses/?min_price=500&max_price=2000 - фильтр по цене
- GET /courses/?teacher_id=1 - фильтр по преподавателю
- GET /courses/{id}/ - один курс
- POST /courses/ - создать курс
- POST /courses/ (со списком) - массовое создание
- PATCH /courses/{id}/ - обновить курс
- DELETE /courses/{id}/ - удалить курс
- DELETE /courses/?ids=1,2,3 - массовое удаление

- GET /students/ - список студентов
- GET /students/{id}/ - один студент
- POST /students/ - создать студента
- POST /students/ (со списком) - массовое создание
- POST /students/{id}/enroll/ - записать на курс
- DELETE /students/{id}/unenroll/?course_id=1 - отписать от курса
- PATCH /students/{id}/ - обновить студента
- DELETE /students/{id}/ - удалить студента
- DELETE /students/?ids=1,2,3 - массовое удаление

- GET /reviews/ - список отзывов
- GET /reviews/?course_id=1 - фильтр по курсу
- GET /reviews/?rating=5 - фильтр по оценке
- GET /reviews/{id}/ - один отзыв
- POST /reviews/ - создать отзыв
- POST /reviews/ (со списком) - массовое создание
- PATCH /reviews/{id}/ - обновить отзыв
- DELETE /reviews/{id}/ - удалить отзыв
- DELETE /reviews/?ids=1,2,3 - массовое удаление

## Запуск

```bash
venv\Scripts\activate
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 15000
