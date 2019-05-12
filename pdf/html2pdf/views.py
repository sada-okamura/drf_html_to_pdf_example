import os

from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from jinja2 import Environment, FileSystemLoader
import pdfkit
from rest_framework import viewsets

from pdf.html2pdf.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    template_dir = ''

    @property
    def template_dir(self):
       return os.path.dirname(os.path.abspath(__file__)) + '/jinja2/'

    def retrieve(self, request, *args, **kwargs):
        pdf = self.request.query_params.get('pdf', None)
        if pdf:
            # fixme judge using accept header = 'application/pdf'
            return self.retrieve_as_pdf(request)

        return super().retrieve(request, *args, **kwargs)


    def retrieve_as_pdf(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        j2_env = Environment(loader=FileSystemLoader(self.template_dir), trim_blocks=True)
        j2_template = j2_env.get_template('user_report.html.jinja2')
        html = j2_template.render(dict(user=serializer.data))
        pdf = pdfkit.from_string(html, False)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=user_report.pdf'

        return response
