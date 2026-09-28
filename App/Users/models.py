from django.db import models
from django.contrib.auth.models import User

# Model to store predictions
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_input = models.CharField(max_length=255)
    predicted_label = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_input} -> {self.predicted_label}"


# Model to store hash links and feature vectors
class UserFeatureData(models.Model):
    hash_link = models.CharField(max_length=256, unique=True)
    feature_vector = models.TextField()  # comma-separated 40 numeric values
    created_at = models.DateTimeField(auto_now_add=True)

    def get_vector(self):
        return [float(x) for x in self.feature_vector.split(',') if x.strip() != '']
