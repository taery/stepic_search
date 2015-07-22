from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from searchengine.models import Lesson
from searchengine.forms import SearchForm


class LessonListView(ListView):
    model = Lesson

    def get(self, request, *args, **kwargs):
        return render(request, 'lesson_list.html', {"lessons": Lesson.objects.all()})


def get_search_text(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if request.POST['search_text']:
                return HttpResponseRedirect('/thanks/')
            else:
                return HttpResponseRedirect('/lessons/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})


def get_last_page(request):
    return render(request, 'thanks.html')
