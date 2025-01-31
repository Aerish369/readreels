from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator



class Profile(models.Model):
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='users/images', blank=True, default='users/images/author.jpg')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.first_name + ' ' + self.user.last_name
    
    @property
    def username(self):
        return self.user.username
    
    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name
    
    @property 
    def email(self):
        return self.user.email

    @property
    def profile_image_url(self):
        """Return the URL of the profile image, or default if not set."""
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
        return '/media/users/images/author.jpg'


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
    description = models.TextField(max_length=500)
    saved_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='saved_books')
    cover_image = models.ImageField(upload_to='bookreview/images', blank=True, default='bookreview/images/default.jpg')
    tag = models.ForeignKey('Tag', on_delete=models.SET_NULL, null=True, related_name='books')

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

    class Meta:
        ordering = ['review_date']
        unique_together = ('book', 'reviewer')

    def __str__(self) -> str:
        return f'{self.reviewer} - {self.book}'



class Tag(models.Model):
    tag = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self) -> str:
        return self.tag
    