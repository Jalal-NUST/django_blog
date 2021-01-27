from django.db import models
from django.contrib.auth.models  import User
from django.utils import timezone


# Create your models here.
class Post(models.Model):


    #a tuple for choices, to be used  later
    STATUS_CHOICES = (
        ('draft', 'Draft'),('published', 'Published'),
    )
    #This is the field for the post title. This field is CharField, which translates into a VARCHAR column in the SQL database
    title = models.CharField(max_length=250) 


    #This is a field intended to be used in URLs. A slug is a short label that contains only letters, numbers, underscores, or hyphens. 
    #You will use the slug field to build beautiful, SEO-friendly URLs for your blog posts
    #You have added the unique_for_date parameter to this field so that you
    #can build URLs for posts using their publish date and slug. Django will
    #prevent multiple posts from having the same slug for a given date.
    slug = models.SlugField(max_length=250,unique_for_date='publish') 


    #This field defines a many-to-one relationship, meaning that each
    #post is written by a user, and a user can write any number of posts. For this
    #field, Django will create a foreign key in the database using the primary
    #key of the related model. In this case, you are relying on the User model of
    #the Django authentication system. The on_delete parameter specifies the
    #behavior to adopt when the referenced object is deleted. This is not specific
    #to Django; it is an SQL standard. Using CASCADE, you specify that when
    #the referenced user is deleted, the database will also delete all related blog
    #posts. You can take a look at all the possible options at https://docsdjangoproject.com/en/3.0/ref/models/fields/#django.db.models.
    #ForeignKey.on_delete. You specify the name of the reverse relationship,
    #from User to Post, with the related_name attribute. This will allow you to
    #access related objects easily. 
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')

    #body: This is the body of the post. This field is a text field that translates
    #into a TEXT column in the SQL database.
    body = models.TextField()

    #publish: This datetime indicates when the post was published. You
    #use Django's timezone now method as the default value. This returns the
    #current datetime in a timezone-aware format. You can think of it as a
    #timezone-aware version of the standard Python datetime.now method
    publish = models.DateTimeField(default=timezone.now)

    #created: This datetime indicates when the post was created. Since you
    #are using auto_now_add here, the date will be saved automatically when
    #creating an object.
    created = models.DateTimeField(auto_now_add=True)

    #updated: This datetime indicates the last time the post was updated. Since
    #you are using auto_now here, the date will be updated automatically when
    #saving an object.
    updated = models.DateTimeField(auto_now=True)

    #status: This field shows the status of a post. You use a choices parameter,
    #so the value of this field can only be set to one of the given choices
    status = models.CharField(max_length=10,
    choices=STATUS_CHOICES,default='draft')

#You tell Django to sort results by the publish field in descending order by default when you query the database
#You specify the descending order using the negative prefix. By doing this, posts
#published recently will appear first.
class Meta:
    ordering = ('-publish',)

#the default human-readable representation of the object
def __str__(self):
    return self.title