from django.shortcuts import render, redirect
from django.views import generic
from .forms import *
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied


class HomeListView(generic.ListView):
    model = News
    paginate_by = 3
    context_object_name = 'news_list'
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        print(context)
        try:
            context['mention'] = Mention.objects.get(id=1)

        except:
            pass
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        das = []
        print(context['pages'])
        qwe = News.objects.filter(is_prior=True)
        for i in range(len(qwe)):
            if i == 2:
                break
            das.append(qwe[i])
        context['prior_news'] = das
        context['loginform'] = LoginForm
        context['events'] = Events.objects.all()[:2]
        return context


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        print(context)
        try:
            context['mention'] = Mention.objects.get(id=1)
        except:
            pass
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        context['loginform'] = LoginForm
        return context


class GaleryListView(generic.ListView):
    model = NewsImage
    paginate_by = 10
    context_object_name = 'images'
    template_name = 'gallery.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GaleryListView, self).get_context_data(**kwargs)
        try:
            context['mention'] = Mention.objects.get(id=1)
        except:
            pass
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        context['loginform'] = LoginForm
        return context


def register(request):  # функция регистрации
    print('da')

    if request.method == 'POST':  # Проверка запроса на пост
        form = UserRegisterForm(request.POST)  # присваиваем форму для данных
        print('POST')
        if form.is_valid():  # Проверка на валидность
            das = form.save(commit=False)  # Сохранение в базу
            file = request.FILES
            print(file)
            das.image = file['image']
            das.save()
            print('VAlid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)  # авторизация юзера
            print('hz')
            login(request, user)  # авторизация юзера
            return redirect('/')  # переадресация на главную страничку
        else:
            print(form.errors)
    else:  # если это запрос не пост
        form = UserRegisterForm()  # Присваивание форму
    context = {'form': form, 'loginform': LoginForm,
               'pages': OtherPage.objects.filter(navbar=True)}  # контекст для передачи данных для шаблона
    def get_context_data(self, **kwargs):
        context = super(NewsUpdateView, self).get_context_data(**kwargs)
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        return context
    return render(request, 'register.html', context)


def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    return redirect('/')


class NewsCreateView(generic.CreateView):
    model = News
    form_class = NewsCreateForm
    template_name = 'news_create.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(NewsCreateView, self).get_context_data(**kwargs)
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied()
        return super(NewsCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        print(form)
        das = form.save(commit=False)
        das.user = request.user
        print(form)
        print(das)
        das.save()
        return das


class NewsUpdateView(generic.UpdateView):
    model = News
    form_class = NewsCreateForm
    template_name = 'news_create.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super(NewsUpdateView, self).get_context_data(**kwargs)
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        return context

    def get_success_url(self):
        print(self.object.get_absolute_url())
        return reverse('home:news_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied()
        return super(NewsUpdateView, self).dispatch(request, *args, **kwargs)


class EventsListView(generic.ListView):
    model = Events
    template_name = 'events.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventsListView, self).get_context_data(**kwargs)
        try:
            context['mention'] = Mention.objects.get(id=1)
        except:
            pass
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        context['loginform'] = LoginForm
        return context


class EventDetailView(generic.DetailView):
    model = Events
    template_name = 'event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        print(context)
        try:
            context['mention'] = Mention.objects.get(id=1)
        except:
            pass
        context['loginform'] = LoginForm
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        return context


class EventCreateView(generic.CreateView):
    model = Events
    form_class = EventCreateForm
    template_name = 'event_create.html'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        return context

    def get_success_url(self):
        print(self.object.get_absolute_url())
        return reverse('home:event_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied()
        return super(EventCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = EventCreateForm(request.POST)
        das = form.save(commit=False)
        das.user = request.user
        print(form)
        print(das)
        if das.is_valid():
            das.save()
        return das


class EventUpdateView(generic.UpdateView):
    model = Events
    form_class = EventCreateForm
    template_name = 'event_create.html'
    context_object_name = 'form'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        return context

    def get_success_url(self):
        print(self.object.get_absolute_url())
        return reverse('home:event_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied()
        return super(EventUpdateView, self).dispatch(request, *args, **kwargs)


class PageDetailView(generic.DetailView):
    model = OtherPage
    context_object_name = 'page'
    template_name = 'page_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        try:
            context['mention'] = Mention.objects.get(id=1)
        except:
            pass
        context['loginform'] = LoginForm
        try:
            context['pages'] = OtherPage.objects.filter(navbar=True)
        except:
            pass
        return context
