from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import PostForm

User = get_user_model()


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших зн. к меньшим)
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)  # будем выгружать по 10 постов
    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get("page")
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/index.html", context)

    # View-функция для страницы сообщества:


def group_posts(request, slug):
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.all()
    # будем выгружать по 10 постов
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    context = {
        "group": group,
        "page_obj": page_obj,
    }
    return render(request, "posts/group_list.html", context)


# Создать профил
def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    count = author.posts.count()
    # будем выгружать по 10 постов
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "count": count,
        "author": author,
    }
    return render(request, "posts/profile.html", context)


# Создать страницу поста
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    pub_date = post.pub_date
    post_title = post.text[:30]
    author = post.author
    author_posts = author.posts.all().count()
    context = {
        "post": post,
        "post_title": post_title,
        "author": author,
        "author_posts": author_posts,
        "pub_date": pub_date,
    }
    return render(request, "posts/post_detail.html", context)


# Создать новый пост
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(f"/profile/{post.author}/", {"form": form})
    form = PostForm()
    groups = Group.objects.all()
    context = {"form": form, "groups": groups}
    return render(request, "posts/create_post.html", context)


# Редактировать пост
def post_edit(request, post_id):
    is_edit = True
    post = get_object_or_404(Post, pk=post_id)
    author = post.author
    groups = Group.objects.all()
    form = PostForm(request.POST or None, instance=post)
    if request.user == author:
        if request.method == "POST" and form.is_valid:
            post = form.save()
            return redirect("posts:post_detail", post_id)
        context = {
            "form": form,
            "is_edit": is_edit,
            "post": post,
            "groups": groups,
        }
        return render(request, "posts/create_post.html", context)
    return redirect("posts:post_detail", post_id)
