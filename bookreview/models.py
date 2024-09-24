from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator




class Collection(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ManyToManyField('Book', related_name='collections')
    is_public = models.BooleanField(default=True)   
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='users/images', blank=True, default='')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.first_name + ' ' + self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']



class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    publication_date = models.DateField()
    isbn = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^\d{13}$', message='ISBN must be 13 digits long')]
        )
    description = models.TextField()
    cover_image = models.ImageField(upload_to='bookreview/images', blank=True, default='')

    def __str__(self) -> str:
        return f'{self.title[:100]} - {self.author}'

    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(5)
            ])
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.reviewer} - {self.book} - {self.rating}'



class Tag(models.Model):
    tag = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, max_length=50)
    book = models.ManyToManyField(Book, related_name='tags')

    def __str__(self) -> str:
        return self.tag
    