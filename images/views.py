from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import ImageCreateForm

# Create your views here.
@login_required
def image_create(request):
    if request.method == 'POST':
        # Form is sent 
        form = ImageCreateForm(data = request.POST)
        if form.is_valid():
            # Form validation success
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # Assign the new item to the current user
            new_item.user = request.user
            new_item.save()

            messages.success(request, "Image added successfully")

            #redirect to new create item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # Build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.POST)

    context = {
        'form': form,
    }

    return render(request, 'images/image/create.html', {'section': 'images'}, context)
