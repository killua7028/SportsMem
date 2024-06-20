from django.shortcuts import render
from AddUser.views import *
from MemberList.models import Member    

def mem_view(request):
    sport_name = request.GET.get('sport', 'Unknown Sport')
    queryset = Member.objects.all()
    context = {'members':queryset, 'sport_name': sport_name}
    return render(request, 'List.html', context) 