from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from base.models import Material
from base.models import Purchase
from base.models import Need
from base.models import received
from django.contrib import messages
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.utils.dateparse import parse_date
from django.core.mail import send_mail
import openpyxl
import os
import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import io
import urllib, base64
from io import BytesIO
from django.http import HttpResponse
from django.db import IntegrityError
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.utils import timezone
from django.db import connection
from django.core.mail import send_mail
from .models import Item



from django.db import models

class MenuImage(models.Model):
    image = models.ImageField(upload_to='menu_images/')  # Stores the uploaded image
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Time of upload

    def __str__(self):
        return f"Menu uploaded on {self.uploaded_at}"


def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item-name').strip()
        if Item.objects.filter(name=item_name).exists():
            messages.error(request, "Item already exists.")
        else:
            Item.objects.create(name=item_name)
            messages.success(request, "Item added successfully.")
        return redirect('add_item')  # Redirect to the same view to display the new item list

    # Fetch all items to display in the table
    items = Item.objects.all()
    return render(request, 'base/add_item.html', {'items': items})

from django.http import JsonResponse