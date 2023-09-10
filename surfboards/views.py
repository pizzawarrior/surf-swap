from django.shortcuts import render
from surfboards.models import Surfboard
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from surfboards.forms import SurfboardForm


# Create surfboard:
@login_required(login_url="/accounts/login/")
def create_surfboard(request):
    if request.method == "POST":
        form = SurfboardForm(request.POST)
        if form.is_valid():
            surfboard = form.save(False)
            surfboard.owner = request.user
            surfboard.save()
            return redirect("surfboard_list")
    else:
        form = SurfboardForm()
    context = {"form": form}
    return render(request, "surfboards/create.html", context)


# Show list of surfboards: (no login required) (AKA HOME_PAGE)
def surfboard_list(request):
    surfboards = Surfboard.objects.all()
    context = {'surfboards': surfboards}
    # Do we want to add reservtions to the context?
    return render(request, 'surfboards/home.html', context)


# Show MY SURFBOARDS
@login_required(login_url="/accounts/login/")
def my_surfboards(request):
    surfboards = Surfboard.objects.filter(owner= request.user)
    context = {
        'surfboards': surfboards
    }
    return render(request, 'surfboards/my_list.html', context)


# Show surfboard detail: (login required)
@login_required(login_url="/accounts/login/")
def surfboard_detail(request, id):
    surfboard = get_object_or_404(Surfboard, id=id)
    context = {
        'surfboard': surfboard
    }
    return render(request, 'surfboards/detail.html', context)


# Update surfboard details:
@login_required(login_url="/accounts/login/")
def edit_surfboard(request, id):
    surfboard = get_object_or_404(Surfboard, id=id)
    if request.method == 'POST':
        form = SurfboardForm(request.POST, instance = surfboard)
        if form.is_valid():
            form.save()
            return redirect('surfboard_detail', id=id)
    else:
        form = SurfboardForm(instance = surfboard)
    context = {
        'surfboard': surfboard,
        'form': form,
        }
    return render(request, 'surfboards/update.html', context)


# Delete surfboard
@login_required(login_url="/accounts/login/")
def delete_surfboard(request, id):
    surfboard = get_object_or_404(Surfboard, id=id)
    surfboard.delete()
    return redirect('my_surfboards')
