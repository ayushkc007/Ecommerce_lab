from django.contrib import admin

# Register your models here.
from .models import Brand, Category, Product, CartItem



class BrandAdmin(admin.ModelAdmin):
    list_display=["name","is_active"]
    search_fields=["name",]
    class Meta:
        model=Brand

class CategoryAdmin(admin.ModelAdmin):
    list_display=["name","is_active"]
    search_fields=["name",]
    class Meta:
        model=Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag","name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]
    #readonly_fields = ["quantity",]
    #search_fields = ["name","price","quantity",]
    # list_display = ["name","price","quantity",]
    # list_filter = ["first_name","email",]
    # search_fields = ["first_name","last_name","email",]
    # readonly_fields = ["last_name",]
    # exclude = ["email"] # to exclude
    # fields = ["first_name","last_name",] # to include
    # fields vs exclude -- mutually exclusive

    class Meta:
        model = Product 
        
admin.site.register(Brand,BrandAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)  

admin.site.register(CartItem)      