from django.contrib.auth.models import User

def createUser(request):
    
    u = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    u.is_active = False
    u.save()
    
    return True
    
def getActiveUsers():
    return User.objects.filter(is_active=True)   