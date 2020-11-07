from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('edoc:company_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_date']


class Doc(models.Model):
    title = models.CharField(max_length=100)
    doc_file = models.FileField(upload_to='doc_file', blank=True, null=True)
    source = models.ForeignKey(Company, related_name='sended_docs', on_delete=models.CASCADE)
    destinations = models.ManyToManyField(Company, related_name='received_docs')
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('edoc:doc_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_date']

