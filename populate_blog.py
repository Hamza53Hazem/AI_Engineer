import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Category, Post

def create_sample_data():
    # Create a user
    user, created = User.objects.get_or_create(username='demo_user', email='demo@example.com')
    if created:
        user.set_password('password123')
        user.save()
        print(f"Created user: {user.username}")
    else:
        print(f"User {user.username} already exists")

    # Create a category
    category, created = Category.objects.get_or_create(name='AI & Tech', description='All about Artificial Intelligence')
    if created:
        print(f"Created category: {category.name}")
    else:
        print(f"Category {category.name} already exists")

    # Create a post
    post, created = Post.objects.get_or_create(
        title='Getting Started with Django',
        defaults={
            'content': 'Django is a high-level Python web framework...',
            'author': user,
            'category': category,
            'status': 'published'
        }
    )
    if created:
        print(f"Created post: {post.title}")
    else:
        print(f"Post {post.title} already exists")

if __name__ == '__main__':
    create_sample_data()
