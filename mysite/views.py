from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    html="""
    <h1>메인페이지 입니다.</h1>\n \
    <p><a href="/apage/">apage로 이동합니다.</a></p>
    <a href="/bpage/">bpage로 이동합니다.</a>
    <a href="/cpage/">cpage로 이동합니다.</a>
    """
    return HttpResponse(html)