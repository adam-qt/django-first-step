from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.


def views_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_page.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'news/create.html'


class NewsDeleteView(DeleteView):
    model = Articles
    fields = ['title', 'annotation', 'text', 'date']
    template_name = 'news/news-delete.html'
    success_url = '/news/'



def create(request):
    err = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            err = 'Заполнение неверно'

    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'news/create.html', data)
