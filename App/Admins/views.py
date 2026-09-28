from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from Users.models import Prediction
import matplotlib.pyplot as plt
import io
import urllib, base64
from collections import Counter

def adminhome(request):
    users = User.objects.filter(is_staff=False, is_superuser=False) 
    return render(request, "Admin/adminhome.html", {"users": users})

def admin_update_userstatus(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        
        # Toggle the is_active status
        user.is_active = not user.is_active
        user.save()

        # Display message based on the action
        if user.is_active:
            messages.success(request, f"User {user.username} has been activated.")
        else:
            messages.success(request, f"User {user.username} has been deactivated.")
        
        return redirect('adminhome')  # Redirect back to the admin home page
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('adminhome')
    
def adminuserpredictions(request):
    predictions = Prediction.objects.all().order_by('-created_at')
    return render(request, 'admin/adminuserpredictions.html', {'predictions': predictions})

def admingraphs(request):
    # Fetch all predictions and count occurrences of each label
    predictions = Prediction.objects.all()
    label_counts = Counter(pred.predicted_label for pred in predictions)

    # Generate Pie Chart
    pie_chart = None
    bar_chart = None

    if label_counts:
        labels = list(label_counts.keys())
        sizes = list(label_counts.values())

        # Generate pie chart
        plt.figure(figsize=(6, 4))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title('Prediction Distribution (Pie Chart)')

        # Save pie chart to buffer
        buffer_pie = io.BytesIO()
        plt.savefig(buffer_pie, format='png')
        buffer_pie.seek(0)
        image_png = buffer_pie.getvalue()
        buffer_pie.close()
        pie_chart = base64.b64encode(image_png).decode('utf-8')
        plt.close()

        # Generate bar chart
        plt.figure(figsize=(6, 4))
        plt.bar(labels, sizes, color='skyblue')
        plt.title('Prediction Distribution (Bar Chart)')
        plt.xlabel('Predicted Labels')
        plt.ylabel('Count')
        plt.xticks(rotation=45)

        # Save bar chart to buffer
        buffer_bar = io.BytesIO()
        plt.savefig(buffer_bar, format='png')
        buffer_bar.seek(0)
        image_png = buffer_bar.getvalue()
        buffer_bar.close()
        bar_chart = base64.b64encode(image_png).decode('utf-8')
        plt.close()

    return render(request, 'admin/admingraphs.html', {
        'pie_chart': pie_chart,
        'bar_chart': bar_chart
    })
