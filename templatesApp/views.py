from django.shortcuts import render


def renderTemplate(request):
    myDict={"name":"Chanatip soyjit"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)


def renderEmployee(request):
    myDict={"id":6604101318,"name":"Chanatip soyjit","sal":50000}
    return render(request, 'templatesApp/employeeTemplate.html',context=myDict)