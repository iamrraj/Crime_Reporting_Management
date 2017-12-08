
from django.conf.urls import url, include
from django.contrib import admin
from comment.views import CreateComment
from comment.views import HomePage, CommentPage
from home.views import criminal_directory
from home.views import upload_evidence
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about$', TemplateView.as_view(template_name="about.html")),
    url(r'^contact', TemplateView.as_view(template_name="contact.html")),
    url(r'^police/', include('police.urls')),
    url(r'^anonymous/', include('home.url_anonymous')),
    url(r'^citizen/', include('citizen.urls')),
    url(r'comment/ajax/create', CreateComment, name = "create_comment"),
    url(r'comment/', CommentPage, name = "comment"),
    url(r'^criminal_directory/', criminal_directory, name = "criminal_directory"),
    url(r'evidence/upload', upload_evidence, name = "evidence_upload"),
    url(r'^$', HomePage, name = "HomePage")

]
