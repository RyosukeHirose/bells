from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission, GroupManager, PermissionManager, ContentType
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

#　原本
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    email = models.EmailField('email', unique=True)

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        'username',
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'is_active',
        default=True,
        help_text=
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ,
    )

    is_trainer=models.BooleanField(
        'is_trainer',
        default=False,
        help_text=
            'can write article',
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name="followers",
        blank=True,
    )



    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


    def __str__(self):
        return self.username

    def natural_key(self):
        return (self.username,)

class Article(models.Model):
    title = models.CharField(max_length=70)
    detail = models.TextField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)

    user_likes = models.ManyToManyField(
        User,
        related_name="likes",
        blank=True,
    )

    user_favorites = models.ManyToManyField(
        User,
        related_name="favorites",
        blank=True,
    )

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    article = models.ForeignKey(
        Article, 
        related_name="comments",
        on_delete=models.CASCADE,
        )
    user = models.ForeignKey(
        User, 
        related_name="commets",
        on_delete=models.SET_NULL, 
        null = True
        )

class Tag(models.Model):
    tag = models.CharField(max_length=20)
    article = models.ManyToManyField(
        Article,
        related_name="tags",
        blank=True,
    )

class QuestionBox(models.Model):
    detail = models.TextField()
    user = models.ForeignKey(
        User,
        related_name="question_box",
        on_delete=models.CASCADE
    )

class Answer(models.Model):
    question_box = models.ForeignKey(
        QuestionBox,
        related_name = "answers",
        on_delete=models.CASCADE
    )
    User = models.ForeignKey(
        User,
        related_name="answers",
        on_delete=models.SET_NULL,
        null=True
    )
