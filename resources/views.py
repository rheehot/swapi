from __future__ import unicode_literals

from rest_framework import viewsets

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship
)

from .serializers import (
    PeopleSerializer,
    PlanetSerializer,
    FilmSerializer,
    SpeciesSerializer,
    VehicleSerializer,
    StarshipSerializer
)


class PeopleViewSet(viewsets.ModelViewSet):

    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return super(PeopleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PeopleViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PeopleViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PeopleViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PeopleViewSet, self).destroy(request, *args, **kwargs)


class PlanetViewSet(viewsets.ModelViewSet):

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return super(PlanetViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PlanetViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PlanetViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PlanetViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PlanetViewSet, self).destroy(request, *args, **kwargs)


class FilmViewSet(viewsets.ModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    search_fields = ('title',)

    def retrieve(self, request, *args, **kwargs):
        return super(FilmViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(FilmViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(FilmViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(FilmViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(FilmViewSet, self).destroy(request, *args, **kwargs)


class SpeciesViewSet(viewsets.ModelViewSet):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return super(SpeciesViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(SpeciesViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(SpeciesViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(SpeciesViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(SpeciesViewSet, self).destroy(request, *args, **kwargs)


class VehicleViewSet(viewsets.ModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    search_fields = ('name','model',)

    def retrieve(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VehicleViewSet, self).destroy(request, *args, **kwargs)


class StarshipViewSet(viewsets.ModelViewSet):

    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer
    search_fields = ('name','model',)

    def retrieve(self, request, *args, **kwargs):
        return super(StarshipViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(StarshipViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(StarshipViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(StarshipViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(StarshipViewSet, self).destroy(request, *args, **kwargs)
