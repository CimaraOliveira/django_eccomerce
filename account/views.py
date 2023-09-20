from django.shortcuts import render

def users(request):
    return render(request, 'accounts/users.html')  
   