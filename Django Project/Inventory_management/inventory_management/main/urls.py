from django.urls import path
from .views import views
from .views import InventoryAPIView


urlpatterns = [
    path('order-management/', views.order_management, name='order_management'),
    path('inventory-tracking/', views.inventory_tracking, name='inventory_tracking'),
    path('update-inventory/<int:item_id>/', views.update_item, name='update_item'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('warehouse-management/', views.add_warehouse_movement, name='warehouse_management'),  # URL for warehouse management
    path('update-warehouse/<int:movement_id>/', views.update_warehouse_movement, name='update_warehouse_movement'),  # URL for updating a warehouse movement
    path('delete-warehouse/<int:movement_id>/', views.delete_warehouse_movement, name='delete_warehouse_movement'),
    path('show_barcode_page/', views.barcode_scanning, name='show_barcode_page'),
]