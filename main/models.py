from django.db import models

class Table(models.Model):
    date = models.DateTimeField(verbose_name='Дата')
    title = models.CharField(max_length=40, db_index=True, verbose_name="Название")
    quantity = models.IntegerField(db_index=True, verbose_name='Количество')
    distance = models.IntegerField(db_index=True, verbose_name='Расстояние')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        indexes = [
            models.Index(fields=['title', ]),
            models.Index(fields=['quantity', ]),
            models.Index(fields=['distance', ]),
        ]
