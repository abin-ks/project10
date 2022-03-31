from django.shortcuts import render, redirect
from .models import *
from datetime import date


# Create your views here.


def home(request):
    it = categories.objects.all()
    return render(request, 'home.html',{'it': it})

def test_page(request):
    it = categories.objects.all()
    its = items.objects.all()
    return render(request, 'test_page.html',{'it': it, 'its': its})


def modelshow(request, id):
    model = items.objects.get(id=id)
    return render(request, 'modelshow.html', {'model': model})


def new_page(request, id):
    man1 = items.objects.filter(cat_id_id=id)
    man = categories.objects.get(cat_id=id)
    return render(request, 'new_page.html', {'man': man, 'man1': man1})


def sub(request, id, key):
    man1 = items.objects.filter(types=key)
    man = categories.objects.get(cat_id=id)
    return render(request, 'sub.html', {'man': man, 'man1': man1})


def admin_log(request):
    return render(request, 'admin_log.html')


def registration(request):
    if request.method == "POST":
        fullname = request.POST["name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        data = Admin_register(fullname=fullname, email=email,
                              username=username, password=password)
        data.save()
        return redirect('admin_log')
    return render(request, 'registration.html')


def admin_login(request):

    if request.method == 'POST':
        if Admin_register.objects.filter(username=request.POST['username'], password=request.POST['password'], designation="admin").exists():
            member = Admin_register.objects.get(
                username=request.POST['username'], password=request.POST['password'])
            request.session['admid'] = member.reg_id
            return redirect('admin_dashboard')

        elif Admin_register.objects.filter(username=request.POST['username'], password=request.POST['password'], designation="user").exists():
            member = Admin_register.objects.get(
                username=request.POST['username'], password=request.POST['password'])
            request.session['admid'] = member.reg_id
            return redirect('home')

        else:
            return redirect('admin_log')
    else:
        return redirect('admin_log')


def admin_dashboard(request):

    admid = request.session['admid']
    adm = Admin_register.objects.filter(reg_id=admid)
    users = Admin_register.objects.all().count()
    models = items.objects.all().count()

    return render(request, 'admin_dashboard.html', {'adm': adm, 'users': users, 'models': models})


def show_category(request):

    caty = categories.objects.all()
    return render(request, 'categories.html', {'caty': caty})


def add_category(request):
    try:

        if request.method == 'POST':
            category_name = request.POST['category_name']
            category_logo = request.FILES['category_logo']
            sub_category1 = request.POST['sub_category1']
            sub_category2 = request.POST['sub_category2']
            sub_category3 = request.POST['sub_category3']
            sub_category4 = request.POST['sub_category4']
            sub_category5 = request.POST['sub_category5']

            cat = categories(category_name=category_name, category_logo=category_logo, sub_category1=sub_category1,
                             sub_category2=sub_category2, sub_category3=sub_category3, sub_category4=sub_category4, sub_category5=sub_category5)
            cat.save()

            return redirect('category')
        else:
            return redirect('categories')
    except:
        return redirect('categories')


def cat_delete(request, cat_id):

    emp = categories.objects.get(cat_id=cat_id)
    emp.delete()
    return redirect('category')


def admin_models(request):
    return render(request, 'admin_models.html')


def addmodel(request):
    var = categories.objects.all()
    return render(request, "addmodel.html", {'var': var})


def createmodel(request):
    if request.method == 'POST':

        modelname = request.POST['modelname']
        description = request.POST['description']
        gib = request.FILES['gib']
        price = request.POST['price']
        types = request.POST['types']
        format = request.POST['format']
        modeltype = request.POST['modeltype']
        category = request.POST['category']
        fbx = request.FILES['fbx']

        item = items(modelname=modelname, description=description, gib=gib, price=price, types=types, format=format, modeltype=modeltype, cat_id_id=category,
                     fbx=fbx)
        item.save()
        return redirect('addmodel')
    else:
        return redirect('createmodel')


def admin_payment_history(request):
    return render(request, 'admin_payment_history.html')


def payment_table(request):
    var = payment.objects.all()
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        var = payment.objects.filter(date__range=[fromdate, todate])
    return render(request, 'payment_table.html', {'var': var})


def registeredusers(request):
    use = Admin_register.objects.all()
    return render(request, 'registeredusers.html', {'use': use})


def delete(request, reg_id):
    admid = request.session['admid']
    use = Admin_register.objects.get(reg_id=reg_id)
    use.delete()
    return redirect('registeredusers')


def adminedit(request, id):
    item = items.objects.filter(id=id)
    viva = categories.objects.all()
    return render(request, "adminedit.html", {'item': item, 'viva': viva})


def admin_current_models(request):
    category = categories.objects.all()
    item = items.objects.all()
    return render(request, 'admin_current_models.html', {'category': category, 'item': item})


def model_delete(request, id):
    abc = items.objects.get(id=id)
    abc.delete()
    return redirect('admin_current_models')


def modeledit(request, id):
    if request.session['admid'] == "":
        return redirect('logout')
    else:

        item = items.objects.get(id=id)
        item.modelname = request.POST.get('modelname', item.modelname)
        item.description = request.POST.get('description', item.description)
        item.gib = request.FILES.get('gib', item.gib)
        item.price = request.POST.get('price', item.price)
        item.types = request.POST.get('types', item.types)
        item.format = request.POST.get('format', item.format)
        item.modeltype = request.POST.get('modeltype', item.modeltype)
        item.cat_id_id = request.POST.get('category_name', item.cat_id_id)
        item.fbx = request.FILES.get('fbx', item.fbx)

        item.save()
        return redirect('admin_current_models')
