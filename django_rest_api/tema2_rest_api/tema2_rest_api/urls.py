"""tema2_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api_app.views import ViewCountry, ViewCountryId, ViewCity, ViewCityCountryId, ViewCityId, \
    ViewTemperatureCityIdCountryId, ViewTemperature, ViewTemperatureCityId, ViewTemperatureId

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/countries', ViewCountry.as_view()),
    path('api/countries/<int:country_id>', ViewCountryId.as_view()),

    path('api/cities', ViewCity.as_view()),
    path('api/cities/country/<int:country_id>', ViewCityCountryId.as_view()),
    path('api/cities/<int:city_id>', ViewCityId.as_view()),

    path('api/temperatures', ViewTemperature.as_view()),
    path('api/temperatures/cities/<int:city_id>', ViewTemperatureCityId.as_view()),
    path('api/temperatures/countries/<int:city_country_id>', ViewTemperatureCityIdCountryId.as_view()),
    path('api/temperatures/<int:temperature_id>', ViewTemperatureId.as_view()),

]
