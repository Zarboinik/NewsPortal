from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostNewsCreate(CreateView):
    form_class = PostForm
    model = PostForm
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'News'
        return super().form_valid(form)


class PostArticlesCreate(CreateView):
    form_class = PostForm
    model = PostForm
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'Articles'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'product_delete.html'
    success_url = reverse_lazy('post_list')
