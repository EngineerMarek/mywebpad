from django.shortcuts import render
from django.utils import timezone
from .models import Webpad
from django.shortcuts import redirect

from .forms import WebpadForm


from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/NzMlVn/')
def pad_list(request):
    pads = Webpad.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'webpad/pad_list.html', {'pads': pads})



@login_required(login_url='/admin/')
def new_pad(request):
    if request.method == "POST":
        form = WebpadForm(request.POST)
        if form.is_valid():
            pad = form.save(commit=False)
            pad.published_date = timezone.now()
            pad.save()
            form = WebpadForm() #show default new form view

    else:
        form = WebpadForm()
    return render(request, 'webpad/pad_edit.html', {'form': form})
