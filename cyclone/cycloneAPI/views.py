from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .models import user
from django.template import loader
#from .forms import ApplicantsForm
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt

from .serializers import userSerializer
#@api_view(['POST'])
@csrf_exempt
def index(request):
	if request.method == "POST":
		print request
		name = request.POST.get('full_name','')
		email = request.POST.get('email','')
		passwor = request.POST.get('password','')
		Results_obj = user(full_name=name,email=email,Password=passwor)
		Results_obj.save()
		return HttpResponse({"test": "abc"})
	#return True
	return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
'''def loginform(request):
	if request.method == "POST":
		email = request.POST.get('email','')
		Password=request.POST.get('password','')
		try:
			context = Applicants.objects.get(email=email,Password=Password)
			#return render(request, 'Examination_system/signupdetail.html', {'context': context})
			return redirect("/myapp/list")
			
		except:
			
			return HttpResponse("Email or Password is incorrect")
#def submitquestion(request):
	#if request.method == "POST":
		#print("start")
		#question_id=request.POST.get('questionid','')
		#print(question_id)
		#user_id = request.POST.ge('userid','')
		#choice_id = request.POST.get('choice','')
		#Results_obj = Results(question_id=question_id,user_id=user_id,choice_id=choice_id)
		#Results_obj.save()
		#return render(request, 'Examination_system/index.html', {'context': context})
		
def signupform(request):
	print (request.method)
	params =[]
	if request.method == "POST":
		#context ={
		#"name":request.POST.get("name"),
		#"email":request.POST.get("email"),
		#"password":request.POST.get("password"),
		#"cpassword":request.POST.get("cpassword"),
		#"university":request.POST.get("university"),
		#}
		Full_Name=request.POST.get('name','')
		email = request.POST.get('email','')
		Password=request.POST.get('password','')
		#get usertype
		applicants_obj = Applicants(Full_Name=Full_Name,email=email,Password=Password)
		applicants_obj.save()
		return render(request, 'Examination_system/login.html')
		#return redirect('/myapp')
	else:
		redirect ('/')
def detail(request, question_id):
	context = {
	"question":Question.objects.get(id=question_id),
	"choice":Choice.objects.get(question_id=question_id),
	}
	template = loader.get_template('Examination_system/question.html')
	#return HttpResponse(question.question_text +" <br>"+""+choice.first_choice +"<br>"+ choice.second_choice+"<br>"+choice.third_choice)
	return HttpResponse(template.render(context, request))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def custom(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('Examination_system/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
def qdetail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'Examination_system/detail.html', {'question': question})
def signup(request):
	return render(request, 'Examination_system/signup.html')
def login(request):
	return render(request,'Examination_system/login.html')'''
