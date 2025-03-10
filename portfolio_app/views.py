from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request, 'home.html')

@require_http_methods(["POST"])
def contact(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        subject = f'Contact Form Message from {name}'
        email_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        
        send_mail(
            subject,
            email_message,
            email,  # From email
            [settings.DEFAULT_FROM_EMAIL],  # To email
            fail_silently=False,
        )
        
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
