from .models import Post, Category
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .utils import get_published_posts


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    queryset = get_published_posts().order_by('-created_at').select_related(
        'author', 'location', 'category'
    )[:5]


class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(
            Category,
            slug=category_slug,
            is_published=True,
        )
        return self.category.posts.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class PostDetailView(DetailView):
    model = Post

    queryset = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
