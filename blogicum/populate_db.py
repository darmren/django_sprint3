from blog.models import Category, Location, Post
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
django.setup()


User = get_user_model()

# Получаем или создаем пользователя admin
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'is_staff': True,
        'is_superuser': True
    }
)
if created:
    admin_user.set_password('admin')
    admin_user.save()

# Создаем категории
travel_cat, _ = Category.objects.get_or_create(
    slug='travel',
    defaults={
        'title': 'Путешествия',
        'description': 'Посты о путешествиях и приключениях',
        'is_published': True
    }
)

notmyday_cat, _ = Category.objects.get_or_create(
    slug='not-my-day',
    defaults={
        'title': 'Не мой день',
        'description': 'Посты о трудных днях',
        'is_published': True
    }
)

python_cat, _ = Category.objects.get_or_create(
    slug='python',
    defaults={
        'title': 'Python-разработка',
        'description': 'Посты о программировании на Python',
        'is_published': True
    }
)

cooking_cat, _ = Category.objects.get_or_create(
    slug='cooking',
    defaults={
        'title': 'Кулинария',
        'description': 'Рецепты и советы по приготовлению',
        'is_published': True
    }
)

# Создаем локации
despair_loc, _ = Location.objects.get_or_create(
    name='Остров отчаянья',
    defaults={'is_published': True}
)

karaganda_loc, _ = Location.objects.get_or_create(
    name='Караганда',
    defaults={'is_published': True}
)

moscow_loc, _ = Location.objects.get_or_create(
    name='Москва',
    defaults={'is_published': True}
)

# Создаем посты
now = timezone.now()

Post.objects.get_or_create(
    title='Крушение',
    defaults={
        'text': '''Наш корабль, застигнутый в открытом море страшным штормом,
        потерпел крушение. Весь экипаж, кроме меня, утонул; я же, несчастный
        Робинзон Крузо, был выброшен полумёртвым на берег этого проклятого острова,
        который назвал островом Отчаяния.''',
        'pub_date': now - timedelta(days=30),
        'author': admin_user,
        'location': despair_loc,
        'category': travel_cat,
        'is_published': True
    }
)

Post.objects.get_or_create(
    title='Утро после крушения',
    defaults={
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло с мели
        приливом и пригнало гораздо ближе к берегу. Это подало мне надежду, что,
        когда ветер стихнет, мне удастся добраться до корабля и запастись едой и
        другими необходимыми вещами.''',
        'pub_date': now - timedelta(days=29),
        'author': admin_user,
        'location': despair_loc,
        'category': notmyday_cat,
        'is_published': True
    }
)

Post.objects.get_or_create(
    title='Шторм продолжается',
    defaults={
        'text': '''Всю ночь и весь день шёл дождь и дул сильный порывистый ветер.
        Корабль за ночь разбило в щепки; на том месте, где он стоял, торчат какие-то
        жалкие обломки, да и те видны только во время отлива.''',
        'pub_date': now - timedelta(days=25),
        'author': admin_user,
        'location': despair_loc,
        'category': notmyday_cat,
        'is_published': True
    }
)

Post.objects.get_or_create(
    title='Изучаем Django',
    defaults={
        'text': '''Сегодня начал изучать Django - отличный фреймворк для веб-разработки!
        Создал свой первый проект Блогикум. Разобрался с моделями, представлениями и
        шаблонами. Очень удобная админ-панель из коробки!''',
        'pub_date': now - timedelta(days=5),
        'author': admin_user,
        'location': moscow_loc,
        'category': python_cat,
        'is_published': True
    }
)

Post.objects.get_or_create(
    title='Рецепт борща',
    defaults={
        'text': '''Сегодня приготовил настоящий украинский борщ по бабушкиному рецепту.
        Секрет вкуса - в правильно приготовленной свекле и хорошем мясном бульоне.
        Добавил сметану и зелень - получилось объедение!''',
        'pub_date': now - timedelta(days=2),
        'author': admin_user,
        'location': karaganda_loc,
        'category': cooking_cat,
        'is_published': True
    }
)

# Создаем пост в будущем (не должен отображаться)
Post.objects.get_or_create(
    title='Планы на будущее',
    defaults={
        'text': '''Это пост запланирован на будущее и пока не должен отображаться
        на сайте.''',
        'pub_date': now + timedelta(days=7),
        'author': admin_user,
        'location': moscow_loc,
        'category': python_cat,
        'is_published': True
    }
)

print("Тестовые данные успешно добавлены!")
print(f"Создано категорий: {Category.objects.count()}")
print(f"Создано локаций: {Location.objects.count()}")
print(f"Создано постов: {Post.objects.count()}")
print("\nДля входа в админку используйте:")
print("Логин: admin")
print("Пароль: admin")
