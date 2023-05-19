import datetime
import json

from rest_framework.views import APIView
from rest_framework.response import Response

from api_app.models import CountryModel, CityModel, TemperatureModel
from api_app.serializers import CountryAddSerializer, CountryUpdateSerializer, \
    CityAddSerializer, CityUpdateSerializer, TemperatureAddSerializer, TemperatureUpdateSerializer


class ViewCountry(APIView):

    def post(self, request):

        serializer: CountryAddSerializer = CountryAddSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400)

        try:
            data = serializer.data
            new_entry: CountryModel = CountryModel(name=data['nume'], longitude=data['lon'], latitude=data['lat'])
            new_entry.save()
        except:
            return Response(status=409)

        return Response(status=201, data={'id': new_entry.id})


    def get(self, request):

        response_data = list(map(
            lambda entry: {'id': entry.id, 'nume': entry.name, 'lat': entry.latitude, 'lon': entry.longitude},
            CountryModel.objects.all()
        ))
        return Response(status=200, data=response_data)


class ViewCountryId(APIView):

    def put(self, request, country_id):

        serializer: CountryUpdateSerializer = CountryUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400)

        if country_id != serializer.data['id']:
            return Response(status=400)

        try:
            data = serializer.data

            if not CountryModel.objects.filter(id=country_id).exists():
                raise Exception()

            CountryModel.objects.filter(id=country_id) \
                .update(name=data['nume'], longitude=data['lon'], latitude=data['lat'])
        except:
            return Response(status=404)

        return Response(status=200)


    def delete(self, request, country_id):

        try:
            if not CountryModel.objects.filter(id=country_id).exists():
                raise Exception()

            CountryModel.objects.filter(id=country_id).delete()
        except:
            return Response(status=404)

        return Response(status=200)


class ViewCity(APIView):
    def post(self, request):

        serializer: CityAddSerializer = CityAddSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400)

        try:
            data = serializer.data
            new_entry: CityModel = CityModel(name=data['nume'], longitude=data['lon'],
                                             latitude=data['lat'], country_id=data['idTara'])
            new_entry.save()
        except:
            return Response(status=409)

        return Response(status=201, data={'id': new_entry.id})


    def get(self, request):

        response_data = list(map(
            lambda entry: {'id': entry.id, 'nume': entry.name, 'lat': entry.latitude,
                           'lon': entry.longitude, 'idTara': entry.country_id},
            CityModel.objects.all()
        ))
        return Response(status=200, data=response_data)


class ViewCityCountryId(APIView):
    def get(self, request, country_id):

        response_data = list(map(
            lambda entry: {'id': entry.id, 'nume': entry.name, 'lat': entry.latitude,
                           'lon': entry.longitude, 'idTara': entry.country_id},
            CityModel.objects.filter(country_id=country_id).all()
        ))
        return Response(status=200, data=response_data)


class ViewCityId(APIView):
    def put(self, request, city_id):

        serializer: CityUpdateSerializer = CityUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400)

        if city_id != serializer.data['id']:
            return Response(status=400)

        try:
            data = serializer.data

            if not CityModel.objects.filter(id=city_id).exists():
                raise Exception()

            CityModel.objects.filter(id=city_id) \
                .update(name=data['nume'], longitude=data['lon'], latitude=data['lat'], country_id=data['idTara'])
        except:
            return Response(status=404)

        return Response(status=200)


    def delete(self, request, city_id):

        try:
            if not CityModel.objects.filter(id=city_id).exists():
                raise Exception()

            CityModel.objects.filter(id=city_id).delete()
        except:
            return Response(status=404)

        return Response(status=200)


class ViewTemperature(APIView):
    def post(self, request):

        serializer: TemperatureAddSerializer = TemperatureAddSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400)

        try:
            data = serializer.data
            new_entry: TemperatureModel = TemperatureModel(city_id=data['idOras'], value=data['valoare'])
            new_entry.save()
        except:
            return Response(status=409)

        return Response(status=201, data={'id': new_entry.id})


    def get(self, request):

        query_args = {}

        if 'lat' in request.query_params:
            query_args['city__latitude__exact'] = request.query_params['lat']

        if 'lon' in request.query_params:
            query_args['city__longitude__exact'] = request.query_params['lon']

        if 'from' in request.query_params:
            query_args['timestamp__gte'] = datetime.datetime.strptime(request.query_params['from'], '%Y-%m-%d')
        # else:
        #     query_args['timestamp__gte'] = datetime.datetime.min

        if 'until' in request.query_params:
            query_args['timestamp__lte'] = datetime.datetime.strptime(request.query_params['until'], '%Y-%m-%d')
        # else:
        #     query_args['timestamp__lte'] = datetime.datetime.max

        response_data = list(map(
            lambda entry: {'id': entry.id, 'valoare': entry.value, 'timestamp': entry.timestamp},
            TemperatureModel.objects.filter(**query_args).all()
        ))
        return Response(status=200, data=response_data)


class ViewTemperatureCityId(APIView):
    def get(self, request, city_id):

        query_args = {}

        if 'from' in request.query_params:
            query_args['timestamp__gte'] = datetime.datetime.strptime(request.query_params['from'], '%Y-%m-%d')
        # else:
            # query_args['timestamp__gte'] = datetime.datetime.min

        if 'until' in request.query_params:
            query_args['timestamp__lte'] = datetime.datetime.strptime(request.query_params['until'], '%Y-%m-%d')
        # else:
        #     query_args['timestamp__lte'] = datetime.datetime.max

        query_args['city_id'] = city_id

        response_data = list(map(
            lambda entry: {'id': entry.id, 'valoare': entry.value, 'timestamp': entry.timestamp},
            TemperatureModel.objects.filter(**query_args).all()
        ))
        return Response(status=200, data=response_data)


class ViewTemperatureCityIdCountryId(APIView):
    def get(self, request, city_country_id):

        query_args = {}

        if 'from' in request.query_params:
            query_args['timestamp__gte'] = datetime.datetime.strptime(request.query_params['from'], '%Y-%m-%d')
        # else:
        #     query_args['timestamp__gte'] = datetime.datetime.min

        if 'until' in request.query_params:
            query_args['timestamp__lte'] = datetime.datetime.strptime(request.query_params['until'], '%Y-%m-%d')
        # else:
        #     query_args['timestamp__lte'] = datetime.datetime.max

        query_args['city__country_id'] = city_country_id

        response_data = list(map(
            lambda entry: {'id': entry.id, 'valoare': entry.value, 'timestamp': entry.timestamp},
            TemperatureModel.objects.filter(**query_args).all()
        ))
        return Response(status=200, data=response_data)


class ViewTemperatureId(APIView):
    def put(self, request, temperature_id):

        serializer: TemperatureUpdateSerializer = TemperatureUpdateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=400)

        if temperature_id != serializer.data['id']:
            return Response(status=400)

        try:
            data = serializer.data

            if not TemperatureModel.objects.filter(id=temperature_id).exists():
                raise Exception()

            TemperatureModel.objects.filter(id=temperature_id) \
                .update(value=data['valoare'], city_id=data['idOras'], timestamp=datetime.datetime.now())
        except:
            return Response(status=404)

        return Response(status=200)


    def delete(self, request, temperature_id):

        try:
            if not TemperatureModel.objects.filter(id=temperature_id).exists():
                raise Exception()

            TemperatureModel.objects.filter(id=temperature_id).delete()
        except:
            return Response(status=404)

        return Response(status=200)
