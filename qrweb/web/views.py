from django.shortcuts import render
from qr_code.qrcode.utils import QRCodeOptions, WifiConfig

# Create your views here.
def home(request):
    wifi_config = WifiConfig(
        ssid="System.out.println()",
        authentication=WifiConfig.AUTHENTICATION.WPA,
        password="consoleLog(wifi)",
    )
    context = dict(
        wifi_config=wifi_config,
        options=QRCodeOptions(size="m", border=6, error_correction="L"),
    )
    return render(request, "base.html", context)
