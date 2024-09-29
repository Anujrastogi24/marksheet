from django.shortcuts import render

from .forms import SForm
from .models import marks, stud

import os
# for generating pdf marksheet
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa

from marksheet import settings

            pdf = render_to_pdf('existing.html', context)
            # return HttpResponse(pdf, content_type='application/pdf')

            # force download
            if pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    filename = "%s_%s.pdf" %(context['title'],context['name'])
                    content = "inline; filename='%s'" %(filename)
                    #download = request.GET.get("download")
                    #if download:
                    content = "attachment; filename=%s" %(filename)
                    response['Content-Disposition'] = content
                    return response
            return HttpResponse("Not found")