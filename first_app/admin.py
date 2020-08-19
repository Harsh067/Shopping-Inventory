from django.contrib import admin
from first_app.models import Admin,Product,Buyer,Seller,Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name','Product_Description','Reviews','Unit_Price')
    list_filter = ('Unit_Price','Reviews')
    search_fields = ('Name','Product_ID')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('Order_ID','Delivery_Date')
    list_filter = ('Delivery_Date','Total')

admin.site.register(Admin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Order,OrderAdmin)
