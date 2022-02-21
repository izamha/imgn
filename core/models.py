from django.db import models
from users.models import CustomUser

"""
    Iyi model ihagaririye ibigize umugani mugufi/w'umugenurano.
    ---------
    This model below is a data representation of umugani and all the sub-details.
    ---------
"""


class Umugani(models.Model):
    title = models.CharField(max_length=450, null=False)
    meaning = models.TextField()
    application = models.TextField()
    caricature = models.ImageField(null=True, upload_to='caricatures', default='caricatures/caricature-default.jpg')
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[%s]" % self.title
