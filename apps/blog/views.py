from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.db.models import Q
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.utils import timezone
from django.views.generic import (
    CreateView,
    ListView,
)

from .forms import PostForm
from .models import Post


class PostList(ListView):
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    paginate_by = 2

    def get_queryset(self):
        posts = Post.objects.filter(published_date__lte=timezone.now())
        keyword = self.request.GET.get('keyword')
        if keyword:
            posts = posts.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return posts


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


class PostNew(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'

    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
@permission_required('blog.change_post', raise_exception=True)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
@permission_required('blog.view_draft_posts', raise_exception=True)
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True)
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
@permission_required('blog.publish_post', raise_exception=True)
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:post_detail', pk=pk)


@login_required
@permission_required('blog.delete_post', raise_exception=True)
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')
