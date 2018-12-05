from django.conf.urls import *
from django.conf.urls import include
from django.contrib import admin
from money_views import views as money_views
from django.views import static
from django.conf import settings
from django.contrib.auth.views import login, logout_then_login

admin.autodiscover()

urlpatterns = [
    url(r'^$', money_views.index),
    url(r'^any_account$', money_views.any_account),
    url(r'^accounts/(?P<key>[0-9a-f+]+)$', money_views.account),
    url(r'^accounts/(?P<key>[0-9a-f+]+)/csv$', money_views.account_csv),
    url(r'^accounts/(?P<key>[0-9a-f+]+)/modify$', money_views.modify),
    url(r'^accounts/(?P<key>[0-9a-f+]+)/categorize$', money_views.batch_categorize),
    url(r'^accounts/(?P<key>[0-9a-f+]+)/categorize/apply$', money_views.apply_categorize),

    url(r'^accounts/(?P<key>[0-9a-f]+)/transactions/new$', money_views.new_transaction),

    url(r'^transaction/(?P<guid>[0-9a-f]+)/files$', money_views.transaction_files),
    url(r'^transaction/(?P<guid>[0-9a-f]+)/files/upload$', money_views.transaction_upload_file),
    url(r'^transaction/(?P<guid>[0-9a-f]+)/files/delete/(?P<hash>[0-9a-f]+)$',
        money_views.transaction_delete_file),

    url(r'^api/change_memo$', money_views.api.change_memo),
    url(r'^api/change_account$', money_views.api.change_account),
    url(r'^api/transactions$', money_views.api.get_transactions),

    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Login
    url(r'^accounts/login/$', money_views.welcome),
]
