from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=32, unique=True)
    book_text = models.TextField(unique=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.book_name
