from django.db import models

# Ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
  image = models.ImageField(verbose_name='Imagen', upload_to='blog')
  title = models.CharField(max_length=200, verbose_name='Titulo')
  desc = models.TextField(verbose_name='Descripcion')
  content = RichTextField(verbose_name='Contenido')
  
  created = models.DateTimeField(
    auto_now_add=True, 
    verbose_name='Fecha de creacion'
    )
  update = models.DateTimeField(  
    auto_now=True, 
    verbose_name='Fecha de actualizacion'
    )
  
  class Meta:
    verbose_name = 'Publicacion'
    verbose_name_plural = 'Publicaciones'
    ordering = ['-created']
  
  def __str__(self) -> str:
    return self.title