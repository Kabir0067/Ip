import json
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie



@ensure_csrf_cookie
def home_view(request):
    return render(request, "index.html", {"recipient_email": settings.LOVER_EMAIL})

def love_view(request):
    return render(request, "love.html")

def sad_view(request):
    return render(request, "index.html")

@require_POST
def save_location(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Malformed JSON")

    recipient_email = (data.get("recipient_email") or settings.LOVER_EMAIL or "").strip()
    if not recipient_email:
        return HttpResponseBadRequest("Recipient email required")

    try:
        lat = float(data.get("lat"))
        lon = float(data.get("lon"))
        acc = data.get("accuracy")
    except (TypeError, ValueError):
        return HttpResponseBadRequest("Invalid coordinates")

    subject = "📍 Location (by consent) — Kabir"
    message = f"Lat: {lat}\nLon: {lon}\nAccuracy(m): {acc if acc is not None else 'n/a'}"
    send_mail(subject, message, None, [recipient_email])

    return JsonResponse({"ok": True, "redirect": "/love/"})
