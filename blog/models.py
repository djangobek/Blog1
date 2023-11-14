from django.db import models
from django.contrib.auth.models import User


class BlogCategories(models.Model):
    name = models.CharField(max_length=255, verbose_name='kategoriya nomi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog kategoriyasi"
        verbose_name_plural = "Bloglar kategoriyalari"
        ordering = "id",






class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='accepted')
    
class PassportInfo(models.Model):
    firstname = models.CharField(max_length=255, default="Nurbek")
    lastname = models.CharField(max_length = 255, blank=True, null=True)
    age = models.PositiveSmallIntegerField(verbose_name='Yoshi', default=3)
    seria = models.CharField(max_length = 2)
    num = models.CharField(max_length = 10)

class Author(models.Model):
    info = models.OneToOneField(PassportInfo, verbose_name="Pasport ma`lumotlari", on_delete=models.CASCADE, blank=True, null=True)
    STATUS = (
        ('Admin', 'Admin'),
        ('Menager', 'Menager'),
        ('super_admin', 'super_admin')
    )
    status = models.CharField(max_length=12, choices=STATUS, default='Menager')

class Blog(models.Model):
    STATUS = (
        ('create', 'yaratilgan'),
        ('accepted', 'tasdiqlangan'),
        ('cancelled', 'bekor qilingan')
    )
    category = models.ForeignKey(BlogCategories, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300, verbose_name='sarlavha')
    short_description = models.TextField(verbose_name="qisqa izoh")
    description = models.TextField(verbose_name="izoh")
    photo = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan sana', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True,null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='created')
    objects = models.Manager()
    blog_manager = BlogManager()

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
        ordering = ["id"]































