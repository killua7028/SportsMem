from django.shortcuts import render, redirect
from MemberList.models import *

def Add(request):
    sport_name = request.GET.get('sport', 'unkown_sport')
    if request.method == "POST":

        data = request.POST

        name = data.get('name')
        age = data.get('age')
        date_of_joining = data.get('date_of_joining')
        sport = data.get('sport')

        print(name)
        print(age)
        print(sport)

        Member.objects.create(
            name = name,
            age = age,
            date_of_joining = date_of_joining,
            sport = sport,
        )
        return redirect(f'/addusr/?sport={sport}')

    queryset = Member.objects.all()
    context = {'members':queryset, 'sport_name':sport_name}
    return render(request, 'AddUser.html', context)
