from django.urls import path
from . import views
from django.conf import settings
from base.admin import admin_site
from django.conf.urls.static import static

urlpatterns = [
    path('mess_admin', admin_site.urls),
    path('', views.home, name='home'),  # Ensure this line exists
    path('login_view/', views.login_view, name='login_view'),
    path('change-password/', views.password_reset_request, name='password_reset_request'),
     path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.password_reset_form, name='password_reset_form'),
    path('sidebar_view/',views.sidebar_view,name='sidebar_view'),
    path('dash_view/', views.dash_view, name='dash_view'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    path('add_data/',views.add_data,name='add_data'),
    path('adddata/',views.adddata,name='adddata'),
    path('update_charts/',views.update_charts,name='update_charts'),    
    path('acknowledgement/', views.Acknowledgement_view, name='Acknowledgement'),
    path('Purchase_acknowledgement/', views.purchase_Acknowledgement_view, name='Purchase_Acknowledgement'),
    path('need_acknowledgement/', views.need_Acknowledgement_view, name='need_Acknowledgement'),
    path('mess-menu/', views.mess_menu, name='mess'),
    path('print_view/', views.print_view, name='print_view'),
    path('print_purchase_view/', views.print_purchase_view, name='print_purchase_view'),
    path('print_need_view/', views.print_need_view, name='print_need_view'),
    path('print_pdf/',views.print_pdf,name='print_pdf'),
    path('need_print_pdf/',views.need_print_pdf,name='need_print_pdf'),
    path('materials_purchase_view/', views.materials_purchase_view, name='materials_purchase_view'),
    path('fetch-purchase-data/', views.fetch_purchase_data, name='fetch_purchase_data'),
    path('materials_need_view/', views.materials_need_view, name='materials_need_view'),
    path('materials_receive_view/', views.materials_receive_view, name='materials_receive_view'),
    path('received_view/', views.received_view, name='received_view'),
    path('mess_entry_view/',views.mess_entry_view,name='mess_entry_view') ,
    path('add_item/', views.add_item, name='add_item'),
    path('backup_purchase_view/',views.backup_purchase_view,name='backup_purchase_view'),
    path('get-item-suggestions/', views.get_item_suggestions, name='get_item_suggestions'),
    path('backup_need_view/',views.backup_need_view,name='backup_need_view'),
    path('visualization/',views.visualization,name='visualization'),
    path('logout_view/', views.logout_view, name='logout_out'),
    path('fetch-received-data/', views.fetch_received_data, name='fetch_received_data'),
    path('fetch_materials_by_date/', views.fetch_materials_by_date, name='fetch_materials_by_date'),  # Save usage data
    path('get-mess-menu/', views.get_mess_menu, name='get_mess_menu'),
    path('needbackup_print_pdf/',views.needbackup_print_pdf,name='needbackup_print_pdf'),
    path('backup_purchase_print_pdf/',views.backup_purchase_print_pdf,name='backup_purchase_print_pdf'),
  
      
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
