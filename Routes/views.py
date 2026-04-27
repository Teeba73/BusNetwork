from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Route, Station
from django.db.models import Q


def index(request):
    origin_q      = request.GET.get("origin", "").strip()
    destination_q = request.GET.get("destination", "").strip()

    routes = Route.objects.all()

    if origin_q:
        routes = routes.filter(
            Q(origin__city__icontains=origin_q) |
            Q(origin__name__icontains=origin_q)
        )

    if destination_q:
        routes = routes.filter(
            Q(destination__city__icontains=destination_q) |
            Q(destination__name__icontains=destination_q)
        )

    return render(request, "Routes/index.html", {"routes": routes})


def route_details(request, route_id):
    route = get_object_or_404(Route, pk=route_id)

    is_booked = False
    if request.user.is_authenticated:
        is_booked = route.passengers.filter(id=request.user.id).exists()

    return render(request, "Routes/Route.html", {
        "route": route,
        "passengers": route.passengers.all(),
        "is_booked": is_booked
    })


@login_required
def book(request, route_id):
    if request.method == "POST":
        route = get_object_or_404(Route, pk=route_id)
        if not route.passengers.filter(id=request.user.id).exists(): 
            route.passengers.add(request.user)
        return HttpResponseRedirect(reverse("Routes:Route_details", args=(route.id,)))
    return HttpResponseRedirect(reverse("Routes:index"))


@login_required
def unbook(request, route_id):
    if request.method == "POST":
        route = get_object_or_404(Route, pk=route_id)
        if route.passengers.filter(id=request.user.id).exists():  
            route.passengers.remove(request.user)
        return HttpResponseRedirect(reverse("Routes:Route_details", args=(route.id,)))
    return HttpResponseRedirect(reverse("Routes:index"))


def station_detail(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    departures = Route.objects.filter(origin=station)
    arrivals   = Route.objects.filter(destination=station)
    return render(request, "Routes/station.html", {
        "station":    station,
        "departures": departures,
        "arrivals":   arrivals,
    })
