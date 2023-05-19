from rest_framework.serializers import Serializer, CharField, IntegerField, FloatField


class CountryAddSerializer(Serializer):
    nume = CharField(max_length=128)
    lat = FloatField()
    lon = FloatField()


class CountryUpdateSerializer(Serializer):
    id = IntegerField()
    nume = CharField(max_length=128)
    lat = FloatField()
    lon = FloatField()


class CityAddSerializer(Serializer):
    idTara = IntegerField()
    nume = CharField(max_length=128)
    lat = FloatField()
    lon = FloatField()


class CityUpdateSerializer(Serializer):
    id = IntegerField()
    idTara = IntegerField()
    nume = CharField(max_length=128)
    lat = FloatField()
    lon = FloatField()


class TemperatureAddSerializer(Serializer):
    idOras = IntegerField()
    valoare = FloatField()


class TemperatureUpdateSerializer(Serializer):
    id = IntegerField()
    idOras = IntegerField()
    valoare = FloatField()
