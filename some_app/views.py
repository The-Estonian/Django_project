from django.shortcuts import render, redirect
from .models import ToDoList, DoneOrNot
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


def index(request):
    return render(request, "some_app/index.html")


def sign_up(request):
    if request.method == "POST":
        username = request.POST.dict()["username"]
        password = request.POST.dict()["password"]
        email = request.POST.dict()["email"]
        first_name = request.POST.dict()["first_name"]
        last_name =request.POST.dict()["last_name"]
        new_user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        new_user.save()
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "some_app/sign_up.html")
    

@login_required(login_url="login_page")
def show_data(request):
    if request.method == "POST":
        id_to_delete = request.POST.dict()["id_to_delete"]
        User.objects.filter(id=id_to_delete).delete()
    all_users = User.objects.values()
    context = {"all_users":all_users}
    return render(request, "some_app/show_data.html", context)

    
def login_page(request):
    if request.method == "POST":
        username = request.POST.dict()["username"]
        password = request.POST.dict()["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if "next" in request.GET.dict():
                return redirect(request.GET.dict()["next"])
            else:
                return redirect("/")
        else:
            context = {"password":"Username or Password incorrect! "}
            return render(request, "some_app/login_page.html", context)
    else:
        return render(request, "some_app/login_page.html")


def log_out(request):
    logout(request)
    return render(request, "some_app/index.html")


@login_required(login_url="login_page")
# @permission_required("")
def to_do_list(request):
    to_do_user = request.user.id
    to_do_list = ToDoList.objects.filter(user_id=to_do_user)
    done_or_not = DoneOrNot.objects.all()
    task_done = DoneOrNot.objects.get(id=2)
    task_not_done = DoneOrNot.objects.get(id=1)
    user_instance = User.objects.get(id=to_do_user)
    context = {"to_do_list" : to_do_list, "done_or_not": done_or_not}
    if request.method == "POST":
        # print(request.POST)
        if "id_to_delete" in request.POST.dict():
            id_to_delete = request.POST.dict()["id_to_delete"]
            ToDoList.objects.filter(id=id_to_delete).delete()
            return render(request, "some_app/to_do_list.html", context)
        elif "done_or_not" in request.POST.dict():
            datastream = request.POST.dict()["done_or_not"]
            current_value = ToDoList.objects.get(id=datastream)
            if current_value.done_or_not == task_done:
                ToDoList.objects.filter(id=datastream).update(done_or_not=task_not_done)
                print(f"Task {datastream}, ({current_value.to_do_message}) updated to Not Done!")
            elif current_value.done_or_not == task_not_done:
                ToDoList.objects.filter(id=datastream).update(done_or_not=task_done)
                print(f"Task {datastream}, ({current_value.to_do_message}) updated to Done!")
            return render(request, "some_app/to_do_list.html", context)
        elif "add-todo" in request.POST.dict():
            # print(request.POST.dict()["content"])
            content = request.POST.dict()["content"]
            try:
                db_connection = ToDoList(user_id=user_instance, to_do_message=content, done_or_not=task_not_done)
            except ValidationError as e:
                print("Raised error", e.message)
                error = {"ToDo-Error": e}
                context.update(error)
            print("Saving Instance")
            db_connection.save()
            return render(request, "some_app/to_do_list.html", context)
        else:
            return render(request, "some_app/to_do_list.html", context)
    else:
        return render(request, "some_app/to_do_list.html", context)

