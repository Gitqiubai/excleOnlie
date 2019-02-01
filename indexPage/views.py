from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.http import FileResponse
from indexPage.FunctionDir import readExcle
from .models import workData,work
import demjson
# Create your views here.




def indexPage(request):

    if request.COOKIES.get('username'):

        all_work = work.objects.filter(is_timeout=False)



        return render(request,'index.html',{'all_work':all_work})

    else:

        return HttpResponseRedirect('/login')


def test(request):

    if request.COOKIES.get('username'):
        #username = request.session['username']
        username = request.COOKIES.get('username')
        work_id = request.GET.get('id')

        data, data2 = readExcle.read()

        is_exist = workData.objects.filter(work_id=work_id,student_number=username)

        if is_exist:

            work_data = workData.objects.get(work_id=work_id,student_number=username).work_content
            data3 = demjson.decode(work_data)

        else:

            print(len(data2))
            data3 = []
            for i in range(len(data)):
                data3.append(['form_{}'.format(i), data2[i]])
            # print('测试数据',data3)


        return render(request,'excle.html',{'data':data,'data3':data3,'id':work_id})

    else:

        return HttpResponseRedirect('/login')


def commit(request):


    if request.COOKIES.get('username'):
        #username = request.session['username']
        username = request.COOKIES.get('username')
        work_id = request.GET.get('id')
        print('session检查:',username)
        if request.method == "POST":

            print(len(request.POST))

            data = []
            for each in request.POST:
                if each != 'csrfmiddlewaretoken':
                    #data.setdefault(each,request.POST.get(each))
                    data.append([each,request.POST.get(each)])
                    #print(each,request.POST.get(each))
                else:
                    pass

            is_exist = workData.objects.filter(work_id=work_id,student_number=username)

            if is_exist:
                print('当前作业数据已经提交================')
                updata_data = workData.objects.get(work_id=work_id,student_number=username)
                #updata_data_content = updata_data.work_content

                #print('已提交已修改',demjson.decode(updata_data)[0])
                head, data_content = readExcle.read()
                data3 = []
                for i in range(len(head)):
                    data3.append(['form_{}'.format(i), data_content[i]])

                updata_data.work_content = data
                updata_data.save()
                print('这里：',updata_data.work_content[0])
                data3 = updata_data.work_content
                #updata_data_content = demjson.decode(updata_data.work_content)
                #return render(request,'excle2.html',{'data':head,'data3':data3})
                return HttpResponseRedirect('/test?id={}'.format(work_id))

            else:
                print('当前作业数据未提交================')
                res = readExcle.save(data,username,work_id)

                if res =="sucess":

                    #return HttpResponse('已经保存：\n{}'.format(data))
                    #return render(request,'show.html',{'data':data})
                    return HttpResponseRedirect('/test?id={}'.format(work_id))

                else:
                    return HttpResponse('保存失败')

        return HttpResponse('提交页面请勿非法进入')

    else:

        return HttpResponseRedirect('/login')


def show(request):

    if request.COOKIES.get('username'):
        work_id = request.GET.get('id')
        #username = request.session['username']
        head, data_content = readExcle.read()
        data3 = []
        for i in range(len(head)):
            data3.append(['form_{}'.format(i), data_content[i]])

        all_data=[]
        data = workData.objects.filter(work_id=work_id)

        for each in data:
            print(each.work_content)
            all_data.append(demjson.decode(each.work_content))



        return render(request,'show.html',{'head':head,'all_data':all_data,'id':work_id})

    else:

        return HttpResponseRedirect('/login')



def output(request):

    if request.COOKIES.get('username'):
        work_id = request.GET.get('id')
        data = workData.objects.filter(work_id=work_id)

        all_data=[]
        for each in data:
            all_data.append(demjson.decode(each.work_content))

        readExcle.ouput(all_data)

        file = open('output.xls','rb')
        res = FileResponse(file)
        res['Content-Type'] = 'application/octet-stream'
        res['Content-Disposition'] = 'attachment;filename="output_work_{}.xls"'.format(work_id)


        return res

    else:

        return HttpResponse('/login')