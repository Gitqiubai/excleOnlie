import xlrd,xlwt
from indexPage.models import workData





def read():

    data = xlrd.open_workbook('test.xlsx')
    table = data.sheets()[0]
    print(table.row_values(2))

    return table.row_values(2),table.row_values(3)



def save(content,username,id):

    try:
        work_data = workData()

        #workData.student_number = username
        work_data.student_number =username
        print('保存方法：',username)
        work_data.work_id = id
        print('工作id：',id)
        work_data.work_content = content

        print('保存成功----')
        work_data.save()
        return 'sucess'
    except:
        return 'fail'


def ouput(all_data):

    #创建一个对象
    filename = xlwt.Workbook()
    #给工作本命名
    sheet=filename.add_sheet('sheet1')

    for each in all_data:
        for item in each:
            #print('内容：',item[1])
            pass

    for i  in range(len(all_data)):

        for a in range(len(all_data[i])):
            print('内容：',all_data[i][a][1])
            sheet.write(i,a,all_data[i][a][1])

    filename.save('output.xls')


    #print(all_data[0])

