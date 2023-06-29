from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="blg")
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author, related_name="writter")
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

    def get_authors(self):
        return "\n".join([p.name for p in self.authors.all()])


class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    birth_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ["id"]
    #     verbose_name_plural = "oxen"

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime

        if self.birth_date < datetime.date(2023, 4, 5):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(2023, 5, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"
