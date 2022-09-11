from django.db import models
from django.contrib.auth import get_user_model

# Документация рекомендует обращаться к модели User через эту функцию
User = get_user_model()

# класс Group - наследник класса Model из пакета models
class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    # поле для хранения произвольного текста
    text = models.TextField(max_length=200)
    # Тип поля: для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)
    # Тип: ссылка на модель User
    # обеспечивает связь (relation) между таблицами баз данных
    # Параметр on_delete=models.CASCADE обеспечивает связность данных:
    # если из таблицы User будет удалён пользователь, то будут удалены
    # все связанные с ним посты.
    author = models.ForeignKey(
        # если из таблицы User будет удалён пользователь, то будут
        # удалены все связанные с ним посты
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        blank=True,
        null=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="groups",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-pub_date"]
        # чтобы упорядочить по возрастанию поля pub_date

    def __str__(self):
        # выводим текст поста
        return self.text
