"""
URL configuration for inventory_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from accounts.views import *
from secondary.views import *
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('features/', features, name='features'),
    path('solutions/', solutions, name='solutions'),
    path('pricing/', pricing, name='pricing'),
    path('signup/<int:plan_id>/', signup_plan, name='signup2'),
    path('payment/', payment, name='payment'),
    path('customers/', customers, name='customers'),
    path('integrations/', integrations, name='integrations'),
    path('resources/', resources, name='resources'),
    path('search/', search_results, name='search_results'),
    path("order_management/", order_management, name="order_management"),
    path('team/', team, name='team'),
    path('warehouse_management/',add_warehouse_movement, name='warehouse_management'),
    path('update-warehouse-movement/<int:movement_id>/', update_warehouse_movement, name='update_warehouse_movement'), 
    path('delete-warehouse-movement/<int:movement_id>/', delete_warehouse_movement, name='delete_warehouse_movement'),
    path('barcodes/', barcode_scanning, name='barcodes'),
    path('integrations2/', integrations2, name='integrations2'),
    path('inventory_tracking/', inventory_tracking, name='inventory_tracking'),
    path('update-item/<item_id>/',update_item, name='update_item'),
    path('delete-item/<item_id>/', delete_item, name='delete_item'),
    path('reports_page', reports_page, name='reports'),
    path('security', security, name='security'),
    path('terms_of_service',terms_of_service, name='terms_of_service'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('cookie_policy/', cookie_policy, name='cookie_policy'),
    path('error/', error_page, name='error_page'),
    path('payment/process/', process_payment, name='process_payment'),    path('contact/', contact_us, name='contact_us'),
    path('webinar-registration/', webinar_registration, name='webinar_registration'),
    path('inventory/', inventory_view, name='inventory'),
    path('item_grouping/', item_grouping, name='item_grouping'),
    path('multi_warehouse/', multi_warehouse, name='multi_warehouse'),  # Fixed missing path
    path('serial_tracking/', serial_tracking, name='serial_tracking'),
    path('sales_order/', sales_order, name='sales_order'),
    path('invoicing/', invoicing, name='invoicing'),
    path('manage1/', manage1, name='manage1'),
    path('manage2/', manage2, name='manage2'),
    path('manage3/', manage3, name='manage3'),
    path('manage4/', manage4, name='manage4'),
    path('manage5/', manage5, name='manage5'),
    path('manage6/', manage6, name='manage6'),
    path('manage7/', manage7, name='manage7'),
    path('manage8/', manage8, name='manage8'),
    path('manage9/', manage9, name='manage9'),
    path('packing-shipping/', packing_shipping, name='packing_shipping'),
    path('sales-return/', sales_return, name='sales_return'),
    path('reporting-analytics/', reporting_analytics, name='reporting_analytics'),
    path('sku-generator/', sku_generator, name='sku_generator'),
    path('recorder-points/', recorder_points, name='recorder_points'),
    path('package-geometry/', package_geometry, name='package_geometry'),
    path('terms/', terms_of_service, name='terms_of_service'),
    path('privacy/', privacy_policy, name='privacy_policy'),
    path('cookies/', cookie_policy, name='cookie_policy'),
    path('terms/', terms, name='terms'),
    path('privacy/', privacy, name='privacy'),
    path('cookies/', cookies, name='cookies'),
    path('contact-us/', contact, name='contact'),
    path('register/', register, name='register'),
    path('help-documentation/', help_documentation, name='help_documentation'),
    path('faq/', faq, name='faq'),  # Make sure this is defined
    path('forums/', forums, name='forums'),
    path('blogs/', blogs, name='blogs'),
    path('essential-business-guides/', essential_business_guides, name='essential_business_guides'),
    path('webinar/', webinar, name='webinar'),
    path('reach-out-to-us/', reach_out_to_us, name='reach_out_to_us'),
    path('webinar/', webinar, name='webinar'),
    path('save-webhook/', save_webhook, name='save_webhook'),
    path('trigger-custom-function/', trigger_custom_function, name='trigger_custom_function'),
    path('accounts/login/', login_view, name='login'),
    path('signup2/', signup_plan, name='signup2'),
    path('inventory/', inventory_tracking, name='inventory'),
    path('warehouse/update/<int:id>/', update_warehouse, name='update_warehouse'),
    path('warehouse/delete/<int:id>/', multi_warehouse, name='delete_warehouse'),
    path('payment/', payment, name='payment'),
    path('pricing-details/', pricing_page, name='pricing_page'),
    # path('protected/', protected_view, name='protected'),

]
