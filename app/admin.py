from django.contrib import admin
from .models import Students, Teacher

# Register all models in a list
models_to_register = [Students, Teacher]

# Use a loop to register each model
for model in models_to_register:
    admin.site.register(model)