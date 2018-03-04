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
		photo = request.POST.get('photo')
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
				f = open(email+'/conf.txt','w')
				f.write(name + '\n' + passv + '\n' + photo + '\n')
				f.close()
				f = open(email+'/liked.txt','w')
				f.close()
				f = open(email+'/friends.txt','w')
				f.close()
				f = open('glob_conf.txt','w')
				f.write(email)
				f.close()
			return resp
	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp

@csrf_exempt
def friends(request):
	if request.method == 'GET':
		resp = HttpResponse()
		resp.status_code = 405
		resp.write('Now method is not supported.')
		return resp
	elif request.method == 'POST':
		email = request.POST.get('email')
		if email == None:
			resp = HttpResponse()
			resp.status_code = 406
			resp.write('Required argument not found.')
			print("ok " )
			return resp
		else:
			resp = HttpResponse()
			resp.status_code = 400
			if os.path.isfile(email + '/friends.txt'):
				f = open(email + '/friends.txt','r')
				for line in f:
					resp.write(line.split('\n')[0]+'&')
					f1 = open(line.split('\n')[0]+'/conf.txt','r')
					halo = f1.read().split('\n')
					resp.write(halo[0]+'&')
					resp.write(halo[2]+'$')
					f1.close()

			else:
				resp.write('no friends')
				print("ne ok ")
			return resp
	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp

@csrf_exempt
def like(request):
	if request.method == 'GET':
		resp = HttpResponse()
		resp.status_code = 405
		resp.write('Now method is not supported.')
		return resp
	elif request.method == 'POST':
		likes = request.POST.get('likes')
		liked = request.POST.get('liked')
		if likes == None:
			resp = HttpResponse()
			resp.status_code = 406
			resp.write('Required argument not found.')
			print("ok " )
			return resp
		else:
			resp = HttpResponse()
			resp.status_code = 400
			f = open(likes + '/liked.txt','r')
			q = f.read().find(liked)
			f.close()
			if q==-1:
				f = open(liked + '/liked.txt','a')
				f.write(likes)
			else:
				f = open(liked + '/friends.txt','a')
				f.write(likes)
				f.close()
				f = open(likes + '/friends.txt','a')
				f.write(liked)
				f.close()
				resp.write('math')
				print("ne ok ")
			return resp
	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp

@csrf_exempt
def near(request):
	if request.method == 'GET':
		resp = HttpResponse()
		z = request.GET.get('user')
		print(z)
		resp.status_code = 200
		f = open('glob_conf.txt','r')
		f1 = open(z + '/friends.txt','r')
		for line in f:
			if f1.read().find(line)==-1:
				resp.write(line + '&')
				f2 = open(line + '/conf.txt')
				w = f2.read().split('\n')
				resp.write(w[0]+'&')
				resp.write(w[2]+'')
		return resp
	resp = HttpResponse()
	resp.status_code = 204
	resp.write('We need a request')
	return resp

