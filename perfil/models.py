from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200,verbose_name='Titulo')
  desc =models.TextField(verbose_name='Descripcion')
  
  created = models.DateTimeField(
    auto_now_add=True, 
    verbose_name='Fecha de creacion'
    )
  update = models.DateTimeField(  
    auto_now=True, 
    verbose_name='Fecha de actualizacion'
    )
  
  class Meta:
    verbose_name = 'Proyecto'
    verbose_name_plural = 'Proyectos'
    ordering = ['-created']
  
  def __str__(self) -> str:
    return self.title