from django.contrib import admin, sites
from main.models import City, District, Category, Enterprise, Product, Price, Company
from .city import CityAdmin
from .district import DistrictAdmin
from .category import CategoryAdmin
from .enterprise import EnterpriseAdmin
from .company import CompanyAdmin
from .product import ProductAdmin
from .price import PriceAdmin


# Register your models here.
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)