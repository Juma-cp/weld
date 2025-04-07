
## **2. Key File Contents**

### 1. Backend Models (`backend/authentication/models.py`)
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class WeldingUser(AbstractUser):
    CERT_LEVELS = [
        ('CW', 'Certified Welder'),
        ('CWI', 'Certified Welding Inspector'),
        ('SCWI', 'Senior Certified Welding Inspector')
    ]
    
    certification = models.CharField(max_length=4, choices=CERT_LEVELS)
    years_experience = models.PositiveIntegerField(default=0)
    employer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.get_full_name()} ({self.certification})"
