from django.http import HttpResponse
from  django.shortcuts import render

def analize(request):
    # getting text
    djtext = request.POST.get('text', 'default')
    # checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    Fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('removenewline', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspacecount = request.POST.get('extraspacecount', 'off')
    charcount = request.POST.get('charcount', 'off')
    li=[]
    whole_analize = djtext
    check=False
    sumprivious = 0
    newsum=0

    if removepunc == 'on':
        punctuations = '''.,?!:;'"'''
        list_of_punctuations=list(punctuations)
        for i in list_of_punctuations:
            whole_analize=whole_analize.replace(i,'')
        li.append('Remove punctuation ')
        check=True

    if Fullcaps == 'on':
        analize = ''
        for char in whole_analize:
            analize = analize + char.upper()
        whole_analize=analize
        li.append('changing to uppercase ')
        check = True


    if newlineremove == 'on':
        analize = ''
        for char in whole_analize:
            if char != '\n' and char!='\r':
                analize = analize + char
        whole_analize=analize
        li.append('Remove new line ')
        check = True



    if extraspacecount == 'on':
        analize = ''
        for index, char in enumerate(whole_analize):
            if djtext[index] == ' ' and djtext[index + 1] == ' ':
                pass
            else:
                analize = analize + char
        whole_analize=analize
        li.append('Remove extraspace ')
        check = True

    if charcount == 'on':
        for char in djtext:
            sumprivious = sumprivious + 1

        for char in whole_analize:
            newsum=newsum+1

        li.append('char count ')
        check = True

    if check==False:
        return HttpResponse('Error')

    total_pupose='+'.join(li)
    print(total_pupose)
    param = {'purpose': total_pupose, 'analized_text': whole_analize}

    if charcount=='on':
        param.update({'newsum':newsum})
        param.update({'sumprivious':sumprivious})
    else:
        param.update({'sum': 'null'})

    return render(request, 'analize.html', param)

def contact(request):
    return render(request,'contactus.html')

def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index3.html')