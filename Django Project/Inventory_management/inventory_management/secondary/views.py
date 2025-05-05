from django.shortcuts import render, redirect

# Create your views here.

def reports_page(request):
    return render(request, 'reports.html')

def security(request):
    return render(request, 'security.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def cookie_policy(request):
    return render(request, 'cookie_policy.html')

def contact_us(request):
    return render(request, 'contact.html')

def manage1(request):
    return render(request, 'manage1.html')

def manage2(request):
    return render(request, 'manage2.html')

def manage3(request):
    return render(request, 'manage3.html')

def manage4(request):
    return render(request, 'manage4.html')

def manage5(request):
    return render(request, 'manage5.html')

def manage6(request):
    return render(request, 'manage6.html')

def manage7(request):
    return render(request, 'manage7.html')

def manage8(request):
    return render(request, 'manage8.html')

def manage9(request):
    return render(request, 'manage9.html')

def serial_tracking(request):
    return render(request, 'serial_tracking.html')

def sales_order(request):
    return render(request, 'sales_order.html')

def invoicing(request):
    return render(request, 'invoicing.html')

def item_grouping(request):
    return render(request, 'item-grouping.html')

def multi_warehouse(request):
    return render(request, "multi-warehouse.html")

def serial_tracking(request):
    return render(request, "serial-tracking.html")

def sales_order(request):
    return render(request, 'sales-order.html')

def packing_shipping(request):
    return render(request, 'packing_shipping.html')

def sales_return(request):
    return render(request, 'sales-return.html')

def reporting_analytics(request):
    return render(request, 'reporting-analytics.html')

def sku_generator(request):
    return render(request, 'sku-generator.html')

def recorder_points(request):
    return render(request, 'recorder-points.html')

def package_geometry(request):
    return render(request, 'package-geometry.html')

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def cookie_policy(request):
    return render(request, 'cookie_policy.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def cookies(request):
    return render(request, 'cookies.html')

def packing_shipping(request):
    return render(request, 'packing-shipping.html')

def contact_us(request):
    return render(request, 'contact-us.html')