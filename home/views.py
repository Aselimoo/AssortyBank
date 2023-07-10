import qrcode
from io import BytesIO
import base64
from django.shortcuts import render, redirect
from .models import UserProfile, Transaction


def IndexView(request):
    user = UserProfile.objects.all()
    context = {
        'user': user
    }
    return render(request, 'index.html', context)


def TransactionView(request):
    return render(request, 'transactions.html')


def generate_qr(request):
    if request.user.is_authenticated:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=2,
        )
        qr.add_data("https://github.com/aselimoo")
        
        qr.make(fit=True) # работает как make migrations после add_data
        img = qr.make_image(fill_color='black', back_color='white')

        buffered = BytesIO()
        img.save(buffered, format="PNG")
        qr_image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return render(request, "QR.html", {"qr_image": qr_image_base64})
    
    else:
        return redirect("admin/")


