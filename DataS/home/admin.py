from django.contrib import admin

# Register your models here.
from .models import HotTables
from .models import Tables,TableDetails

class TablesFilter(admin.ModelAdmin):
    class TableDetailsInline(admin.TabularInline):
        model = TableDetails
        extra = 5 #默认显示条目的数量
    inlines = [TableDetailsInline,]    #Inline把BillSubInline关联进来    
    list_display = ['table_name','db_name','table_type']
     
    #筛选器
    list_filter =['db_name', 'db_type'] #过滤器
    search_fields =['table_name','db_name'] #搜索字段
    #date_hierarchy = ['create_time',]    # 详细时间分层筛选
    list_per_page = 20
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ['db_name',]

admin.site.register(HotTables)
admin.site.register(Tables,TablesFilter)
admin.site.register(TableDetails)
admin.site.site_header = 'DataShow'
admin.site.site_title = '矩阵'
