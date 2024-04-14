from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"aboutus.html")

def removepunc(s):
    s1=""
    punc="""!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
    for i in s:
        if i  not in punc:
            s1+=i
    return s1

def rm_newline(s):
    s1=s.replace("\r\n","")
    return s1

def rm_ext_space(s):
    s1=""
    for i in s.split(" "):
        if i !="":
            s1+=i+" "
    s1=s1.replace(" \r\n","\r\n")
    return s1.strip()

def analyze(request):
    text={"given":(request.POST.get("Text","")),"analyzed":(request.POST.get("Text","")),"operations":[]}
    if text=="":
        return render(request,"analyze.html",text, status=400)
    
    remove_punc=(request.POST.get("removepunc",False))
    upper_case=(request.POST.get("upper",False))
    lower_case=(request.POST.get("lower",False))
    remove_newline=(request.POST.get("rm_newline",False))
    ext_space_rm=(request.POST.get("rm_ext_space",False))

    if remove_punc:
        text["operations"].append("Remove punctuations")
        text["analyzed"]=removepunc(text["analyzed"])
        
    if upper_case:
        text["operations"].append("Change text to uppercase")
        text["analyzed"]=text["analyzed"].upper()
    if lower_case:
        text["operations"].append("Change text to lowercase")
        text["analyzed"]=text["analyzed"].lower()
    
    if remove_newline:
        text["operations"].append("Remove newlines")
        text["analyzed"]=rm_newline(text["analyzed"])
    
    if ext_space_rm:
        text["operations"].append("Remove extra spaces")
        text["analyzed"]=rm_ext_space(text["analyzed"])
   
    return render(request,"analyze.html",text)