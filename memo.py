from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission, GroupManager, PermissionManager, ContentType
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

#　原本
class UserManager(BaseUserManager):
    def create_user(self,username, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username ,email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField('email address', blank=True, unique=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ,
    )

    is_trainer=models.BooleanField(
        'trainer',
        default=False,
    )

    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        # abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self, username):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return username.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    objects = GroupManager()


    def __str__(self):
        return self.username

    def natural_key(self):
        return (self.username,)


# class TrainerGroup(models.Model):
#     name = models.CharField(_('name'), max_length=150, unique=True)
#     permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('permissions'),
#         blank=True,
#     )

#     objects = GroupManager()

#     class Meta:
#         verbose_name = _('group')
#         verbose_name_plural = _('groups')
#         db_table = "test_db"

#     def __str__(self):
#         return self.name

#     def natural_key(self):
#         return (self.name,)


# class TrainerPermission(models.Model):
#     name = models.CharField(_('name'), max_length=255)
#     content_type = models.ForeignKey(
#         ContentType,
#         models.CASCADE,
#         verbose_name=_('content type'),
#     )
#     codename = models.CharField(_('codename'), max_length=100)

#     objects = PermissionManager()

#     class Meta:
#         verbose_name = _('permission')
#         verbose_name_plural = _('permissions')
#         unique_together = [['content_type', 'codename']]
#         ordering = ['content_type__app_label', 'content_type__model', 'codename']

#     def __str__(self):
#         return '%s | %s' % (self.content_type, self.name)

#     def natural_key(self):
#         return (self.codename,) + self.content_type.natural_key()
#     natural_key.dependencies = ['contenttypes.contenttype']
    

# class Trainer(AbstractUser):
#     is_trainer = True

#     trainer_groups = models.ManyToManyField(
#         TrainerGroup,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_(
#             'The groups this user belongs to. A user will get all permissions '
#             'granted to each of their groups.'
#         ),
#         related_name="trainer",
#         related_query_name="trainser_permissons",
#     )

#     trainer_permissions = models.ManyToManyField(
#         TrainerPermission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name="has_trainer",
#         related_query_name="user_permissions",
#     )


# class Article(models.Model):
#     title = models.CharField(max_length=70)
#     detail = models.TextField()
#     trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

# class User(AbstractUser):
#     follows = models.ManyToManyField(
#         Trainer,
#         related_name="followers",
#         blank=True,
#     )

#     likes = models.ManyToManyField(
#         Article,
#         related_name="like_user",
#         blank=True,
#     )

#     favorites = models.ManyToManyField(
#         Article,
#         related_name="favorite_user",
#         blank=True,
#     )


# class Comment(models.Model):
#     comment = models.CharField(max_length=256)
#     article = models.ForeignKey(
#         Article, 
#         related_name="comments",
#         on_delete=models.CASCADE,
#         )
#     user = models.ForeignKey(
#         User, 
#         related_name="commets",
#         on_delete=models.SET_NULL, 
#         null = True
#         )

# class Tag(models.Model):
#     tag = models.CharField(max_length=20)
#     article = models.ManyToManyField(
#         Article,
#         related_name="tags",
#         blank=True,
#     )

# class QuestionBox(models.Model):
#     detail = models.TextField()
#     user = models.ForeignKey(
#         User,
#         related_name="question_box",
#         on_delete=models.CASCADE
#     )

# class Answer(models.Model):
#     question_box = models.ForeignKey(
#         QuestionBox,
#         related_name = "answer",
#         on_delete=models.CASCADE
#     )
#     trainer = models.ForeignKey(
#         Trainer,
#         related_name="answer",
#         on_delete=models.SET_NULL,
#         null=True
#     )
