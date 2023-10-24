from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from home.models import *
from home.forms import LoginForm
from django.shortcuts import get_object_or_404
from .forms import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required


class CourseListView(generic.ListView):
    model = Course
    template_name = 'courses.html'
    paginate_by = 5
    context_object_name = 'courses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        try:
            context['mention'] = Mention.objects.get(id=1)

        except:
            pass
        try:
            context['pages'] = PageCatery.objects.all()
        except:
            pass
        context['loginform'] = LoginForm
        context['news'] = News.objects.all()
        return context


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'course_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['comments'] = CourseComment.objects.filter(course=self.object.id, parent__isnull=True)
        context['comment_form'] = CommentForm()
        context['news'] = News.objects.all()
        context['loginform'] = LoginForm
        try:
            context['mention'] = Mention.objects.get(id=1)

        except:
            pass
        try:
            context['pages'] = PageCatery.objects.all()
        except:
            pass
        print(context)
        return context


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        try:
            context['mention'] = get_object_or_404(Mention, id=1)
        except:
            pass
        context['comments'] = TaskComment.objects.filter(task=self.object.id, parent__isnull=True)
        context['comment_form'] = CommentTaskForm()
        context['news'] = News.objects.all()
        context['loginform'] = LoginForm
        tasks = Task.objects.filter(chapter=context['task'].chapter.id)
        chapters = Chapter.objects.filter(course=context['task'].chapter.course.id)
        try:
            context['mention'] = Mention.objects.get(id=1)

        except:
            pass
        try:
            context['pages'] = PageCatery.objects.all()
        except:
            pass
        for i in range(len(tasks)):
            print(tasks[i].title)
            if tasks[i].id == context['task'].id:
                print('==')
                print(i+1, len(tasks))
                if i+1 == len(tasks) or i+1 == 0:
                    print('nice')
                    for j in range(len(chapters)):
                        if context['task'].chapter.id == chapters[j].id:
                            print('chapter poshlo')
                            if j != 0:
                                context['prev_chapter'] = chapters[j-1]
                                print(context['prev_chapter'], 'prev_chapter')
                            if j+1 != len(chapters):
                                print('ravno', j, len(chapters))
                                if j == len(chapters):
                                    break
                                else:
                                    context['next_chapter'] = chapters[j+1]
                                    print(context['next_chapter'], 'next_chapter')
                                    break
                    print('no')
                if i != len(tasks):
                    try:
                        context['next_task'] = tasks[i + 1]
                        print(context['next_task'], 'next_task')
                    except:
                        pass
                if i != 0:
                    context['prev_task'] = tasks[i - 1]
                    print(context['prev_task'], 'prev_task')
                break
        return context


@require_http_methods(['POST'])
def comment_create(request, pk):
    form = CommentForm(request.POST)
    das = form.save(commit=False)
    das.user_id = request.user.id
    # print(get_object_or_404(CourseComment, pk), 'sad' * 100)
    das.parent = CourseComment.objects.get(id=pk)
    das.course = das.parent.course
    das.save()
    return redirect(f'/course/detail/{das.course.id}')


def main_comment_create(request, pk):
    form = CommentForm(request.POST)
    das = form.save(commit=False)
    das.user_id = request.user.id
    das.course = Course.objects.get(id=pk)
    das.parent = None
    print(das.parent)
    print(123)
    das.save()
    return redirect(f'/course/detail/{das.course.id}')


@permission_required(perm='is_superuser', login_url='/')
def course_comment_delete(request, pk):
    comment = CourseComment.objects.get(id=pk)
    comment.delete()
    return redirect(f'/course/detail/{comment.course.id}')


def main_comment_create_task(request, pk):
    form = CommentTaskForm(request.POST)
    if form.is_valid():
        das = form.save(commit=False)
        das.user_id = request.user.id
        das.task = Task.objects.get(id=pk)
        das.parent = None
        print(das.parent)
        print(123)
        das.save()
        return redirect(f'/course/task_detail/{das.task.id}')
    else:
        print(form.errors)
        return redirect('/')


def course_comment_task_delete(request, pk):
    comment = TaskComment.objects.get(id=pk)
    comment.delete()
    return redirect(f'/course/task_detail/{comment.task.id}')


def course_comment_create_task(request, pk):
    form = CommentTaskForm(request.POST)
    if form.is_valid():
        das = form.save(commit=False)
        das.user_id = request.user.id
        das.parent = TaskComment.objects.get(id=pk)
        das.task = das.parent.task
        print(das.parent)
        print(123)
        das.save()
        return redirect(f'/course/task_detail/{das.task.id}')
    else:
        print(form.errors)
        return redirect('/')


