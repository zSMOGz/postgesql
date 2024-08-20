from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import CountElementsOnPageForm
from .models import *


def index(request):
    count_elements_on_page = None

    if request.method == 'POST':
        form = CountElementsOnPageForm(request.POST)
        if form.is_valid():
            count_elements_on_page = form.cleaned_data['count_elements_on_page']
    else:
        form = CountElementsOnPageForm()

    posts = Post.objects.all().order_by('-date_posted')

    if (count_elements_on_page is None
            or count_elements_on_page < 1):
        count_elements_on_page = 1
    elif count_elements_on_page >= len(posts):
        count_elements_on_page = len(posts)

    print(count_elements_on_page)

    paginator = Paginator(posts, count_elements_on_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'form': form
    }

    return render(request,
                  'index.html',
                  {'page_obj': page_obj})
