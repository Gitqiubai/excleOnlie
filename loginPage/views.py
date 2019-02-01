from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .models import userTable

# Create your views here.



def userLogin(request):

    if request.method == 'POST':
        l_username = request.POST.get('username')
        l_password = request.POST.get('password')
        log = authenticate(username=l_username,password=l_password)
        if log:
            login(request,log)
            request.session['username']=l_username
            rep = render(request,'loginSucess.html')
            rep.set_cookie('username',l_username)

            print('登陆成功')

            return rep
        else:
            return HttpResponseRedirect('/login')
    else:
        return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        r_username = request.POST.get('username')
        r_password = request.POST.get('password')
        r_email = request.POST.get('email')

        userTable.objects.create_user(username=r_username,email=r_email,password=r_password)

        return HttpResponse('注册成功<hr><p><a href="/login">返回登陆</a></p>')

    else:

        return render(request,'register.html')
