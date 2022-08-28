from django.contrib.auth import get_user_model
from django.db import models

class Quote(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    theme = models.CharField(max_length=64)
    the_quote = models.TextField(default = "")
    created_at = models.DateTimeField(auto_now_add = True)
    # When you add a post this will automatically add a timestamp. It is not modifiable.
    updated_at = models.DateTimeField(auto_now = True)
    # This updates, the first it takes the same time as the created_at field.

    def __str__(self):
        return self.the_quote