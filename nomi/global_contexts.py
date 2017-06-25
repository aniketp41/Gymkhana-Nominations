from .models import Post, UserProfile
from django.core.exceptions import ObjectDoesNotExist


def context(request):
    if request.user.is_authenticated:
        try:
            my_profile = UserProfile.objects.get(user=request.user)
            my_posts = Post.objects.filter(post_holders=request.user)
            length = len(my_posts)
            senate = False

            for post in my_posts:
                if post.perms == 'can ratify the post':
                    senate = True

            return {'my_posts': my_posts, 'my_profile': my_profile, 'senate': senate, 'length': length}

        except ObjectDoesNotExist:
            return {'my_posts': 0, 'my_profile': 0}

    else:
        return {'my_posts': 0, 'my_profile': 0}
