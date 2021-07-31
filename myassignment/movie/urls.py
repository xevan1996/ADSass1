from django.conf.urls import url 
from movie import views
from django.urls import path 
from django.conf.urls.static import static

app_name = 'movie'

urlpatterns=[
    path('',views.HomePageView.as_view(), name='home'),
    path('movie-prod-country/',views.Api.movie_prod_country, name='movie-prod-country'),
    path('average-production-budget/',views.Api.average_production_budget, name='average-production-budget'),
    path('total-box-office/',views.Api.total_box_office, name='total-box-office'),
    path('total-box-year/',views.Api.total_box_year, name='total-box-year'),
    path('tikcet-sold-price/',views.Api.tikcet_sold_price, name='tikcet-sold-price'),
    path('release-per-year/',views.Api.release_per_year, name='release-per-year'),
    path('top-per-year/',views.Api.top_per_year, name='top-per-year'),
    path('ticket-sold/',views.Api.ticket_sold, name='ticket-sold'),
    path('top-dist-ms/',views.Api.top_dist_ms, name='top-dist-ms'),
    path('top-genre-ms/',views.Api.top_genre_ms, name='top-genre-ms'),
    path('top-mpaa-ms/',views.Api.top_mpaa_ms, name='top-mpaa-ms'),
    path('top-source-ms/',views.Api.top_source_ms, name='top-source-ms'),
    path('top-method-ms/',views.Api.top_method_ms, name='top-method-ms'),
    path('top-creative-ms/',views.Api.top_creative_ms, name='top-creative-ms'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]