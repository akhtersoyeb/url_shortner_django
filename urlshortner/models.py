from django.db import models
import random
import string

def generate_random_code():
    length = 4
    while True:
        code = ''.join(random.choices(string.ascii_lowercase, k=length))
        if Url.objects.filter(short_url=code).count() == 0:
            break
    return code

class Url(models.Model):
    main_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=8,default=generate_random_code, unique=True)

    def __str__(self):
        return (f"{self.short_url}")
