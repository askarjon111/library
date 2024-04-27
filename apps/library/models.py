from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify
from apps.library.managers import BookManager


class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name='books')
    description = models.TextField(null=True, blank=True)
    published_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    objects = models.Manager()
    with_images = BookManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    @property
    def book_cover(self):
        try:
            return mark_safe('<img src="%s"/ width="120" height="200">' % self.covers.first().image.url)
        except Exception:
            return 'No cover'


class BookCover(models.Model):
    book = models.ForeignKey(Book, related_name='covers', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_covers')

    def __str__(self):
        return self.book.title
