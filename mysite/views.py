from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
import os

# Create your views here.
@csrf_exempt
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

@csrf_exempt
def reg(request):
	if request.method == 'GET':
		resp = HttpResponse()
		resp.status_code = 405
		resp.write('Now method is not supported.')
		return resp
	elif request.method == 'POST':
		email = request.POST.get('email')
		passv = request.POST.get('pass')
		name = request.POST.get('name')
		veg = request.POST.get('veg')
		if email == None:
			resp = HttpResponse()
			resp.status_code = 406
			resp.write('Required argument not found.')
			print("ok " )
			return resp
		else:
			resp = HttpResponse()
			resp.status_code = 400
			if os.path.isfile(email + '/conf.txt'):
				resp.write('exists')
				print("ne ok ")
			else:
				resp.write('ok')
				os.makedirs(email)
				f = open(email + '/conf.txt','a')
				f.write(name + '\n' + passv + '\n' + veg)
			return resp
	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp

