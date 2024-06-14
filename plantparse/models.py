from django.db import models

class PlantsAll(models.Model):
    plant_name_latin = models.CharField(max_length=255, primary_key=True)
    plant_family = models.CharField(max_length=255)
    plant_genus = models.CharField(max_length=255)
    plant_order = models.CharField(max_length=255)
    plant_image = models.ImageField()
    plant_video = models.BinaryField()
    plant_name_en = models.ForeignKey('PlantsEn', db_column='plant_name_en', to_field='plant_name_en', on_delete=models.CASCADE)
    plant_name_hy = models.ForeignKey('PlantsHy', db_column='plant_name_hy', to_field='plant_name_hy', on_delete=models.CASCADE)

    def __str__(self):
        return self.plant_name_latin

    class Meta:
        db_table = 'plants_all'
        verbose_name = 'Plant'
        verbose_name_plural = 'Plants'

class PlantsEn(models.Model):
    plant_name_en = models.CharField(max_length=255, primary_key=True)
    plant_audio_en = models.BinaryField()
    plant_text_en = models.TextField()
    plant_description_en = models.TextField()

    def __str__(self):
        return self.plant_name_en

    class Meta:
        db_table = 'plants_en'
        verbose_name = 'Plant English'
        verbose_name_plural = 'Plants English'

class PlantsHy(models.Model):
    plant_name_hy = models.CharField(max_length=255, primary_key=True)
    plant_audio_hy = models.BinaryField()
    plant_text_hy = models.TextField()
    plant_description_hy = models.TextField()

    def __str__(self):
        return self.plant_name_hy

    class Meta:
        db_table = 'plants_hy'
        verbose_name = 'Plant Armenian'
        verbose_name_plural = 'Plants Armenian'
