from django.contrib import admin
from api.models import Products
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class ProductsResources(resources.ModelResource):
    class Meta:
        model = Products


class ProductsAdmin(ImportExportModelAdmin):
    resource_class = ProductsResources


admin.site.register(Products, ProductsAdmin)
