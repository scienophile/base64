from django.db import models


class CryptData(models.Model):
    input_text = models.TextField(max_length=320)
    CRYPT_TYPES = [
        ('en', 'encode'),
        ('de', 'decode'),
    ]
    crypt = models.CharField(
        max_length=2,
        choices = CRYPT_TYPES,
        blank=False,
        default='de',
    )
    crypt_date = models.DateTimeField('crypt date')
    guess_ip = models.GenericIPAddressField()
    output_text = models.TextField(max_length=320, editable=False)

    class Meta:
        ordering = ['crypt_date']

    def __str__(self):
        return f'Input: {self.input_text} \n Output: {self.output_text}'
