from django.db import models

class Glavnaya(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Текст записи')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Главная'
        # ordering = ['-created_at']

class Novosti(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Текст записи')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Новости'
        # ordering = ['-created_at']

class Oshkole(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Текст записи')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'О школе'
        # ordering = ['-created_at']

class Roditelyam(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Текст записи')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Родителям'
        # ordering = ['-created_at']

class Uchebnayadeyatelnost(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Текст записи')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Учебная деятельность'
        # ordering = ['-created_at']

class Kontakty(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Текст записи')
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Контакты'
        # ordering = ['-created_at']