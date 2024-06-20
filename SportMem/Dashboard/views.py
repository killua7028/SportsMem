from django.shortcuts import render, redirect
from MemberList.models import Member
from .models import Dash

def Dashboard(request):
    sport_name = request.GET.get('sport', 'unknown_sport')
    if request.method == "POST":
        data = request.POST
        SportName = data.get('SportName')

        if SportName:
            # Create a new Dash entry
            new_dash = Dash.objects.create(
                SportName=SportName,
                NoOfMembers=0  # Initial count; update below
            )

            # Update NoOfMembers dynamically
            new_dash.NoOfMembers = get_count_of_members(SportName)
            new_dash.save()

        return redirect('/')

    # Retrieve all Dash entries
    queryset = Dash.objects.all()
    for dash in queryset:
        dash.NoOfMembers = get_count_of_members(dash.SportName)
        dash.save()
    context = {'sports': queryset}
    return render(request, 'Dashboard.html', context)

def get_count_of_members(sport):
    return Member.objects.filter(sport=sport).count()
