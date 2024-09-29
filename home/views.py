from django.shortcuts import render

from .forms import SForm
from .models import marks, stud


def show(request):
    return render(request, "home.html")


import os
# for generating pdf marksheet
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa

from marksheet import settings


def existing(request):
    return render(request,'existing.html')

def fetch_resources(uri, rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1", 'ignore')), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def search(request):
    title = "search"
    form=SForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['roll']
        if stud.objects.filter(roll=name).exists():
            name = form.cleaned_data['roll']      
            queryset = stud.objects.filter(roll=name)
            marksquery = marks.objects.filter(roll=name)
            context={
            "title":title,
            "queryset":queryset,
            "marksquery":marksquery,
            "name":name,
            }
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
        else:
            render(request, "search.html",{'error': True})
         
        context={
            "title":title,
            "form":form,
            }
    context={
            "title":title,
            "form":form,
            'error':True,
            }
    return render(request,'search.html',context)


    