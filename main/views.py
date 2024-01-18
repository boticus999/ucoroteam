from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from .models import Link
from .forms import LinkForm
from django.http import HttpResponseRedirect


def link_list(request):
    links = Link.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            s_link = form.save(commit=False)
            s_link.user = request.user
            s_link.save()
            return redirect('home')
    else:
        form = LinkForm()

    return render(request, 'main/link_short.html', {'links': links,
                                                    'form': form})


def redirect_to_external_site(request, link):
    li = get_object_or_404(Link, link=link)
    return redirect(li.url)


def delete_link(request, link):
    li = get_object_or_404(Link, link=link)
    li.delete()
    return redirect(reverse('home'))
