from django import forms
from .models import Order, WarehouseMovement, BarcodeData


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =['item_id','item_name','item_category','quantity','cost_per_unit','total_cost','supplier_name','supplier_email','supplier_phone','order_status','notes']


class WarehouseMovementForm(forms.ModelForm):
    class Meta:
        model = WarehouseMovement
        fields = ['product_name','quantity','from_location','to_location','date','time']        


class BarcodeDataForm(forms.ModelForm):
    class Meta:
        model = BarcodeData
        fields = ['supplier_name','supplier_email','item_id','item_name','barcode_number','quantity']