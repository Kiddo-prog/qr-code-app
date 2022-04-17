from django.urls import path
from web import views as user_view
from django.conf import settings
from qr_code import views

app_name = "qr_code"
urlpatterns = [
    path("", user_view.home, name="home"),
    path(
        getattr(settings, "SERVE_QR_CODE_IMAGE_PATH", "images/serve-qr-code-image/"),
        views.serve_qr_code_image,
        name="serve_qr_code_image",
    ),
]
