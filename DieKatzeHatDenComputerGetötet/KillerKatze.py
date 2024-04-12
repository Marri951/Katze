import subprocess, http.server, socketserver, os, sys

#Noting current public IP Address--------------------------
ip_method_check = str(os.system(command = 'curl ifcfg.me'))

if ip_method_check != '6':
    ipv4 = str(subprocess.check_output('curl ifcfg.me'))
else:
    ipv4 = str(subprocess.check_output('curl icanhazip.com'))
#-------------------------------------------------------------


#take a seperate list of social media companies, and turn each name/line into an item
companies = open('firmen.txt', 'r').read().split('\n') 
create_temp_hostnames = open('hostnames.txt', 'a')


#go through each company name and create new versions of it that will fit into the hosts file
#these new names are added to a created, temperoary hostnames file
for company in companies:
    addlist_pre = ['www.', '']
    addlist_post = ['.com', '.net', '.org', '.gg', '.net']
    for PieceOfDomain in addlist_pre:
        hostname_part1 = PieceOfDomain + company
        for PieceOfDomain in addlist_post:
            hostname_final =  hostname_part1 + PieceOfDomain
            create_temp_hostnames.write('\n' + str(hostname_final))

create_temp_hostnames.close()


#execution of powershell instance, which uses powershell_command script to create another powershell instance w/ elevated privs.
#The elevated script goes through each line within the hostnames.txt file within the same directory as this index.py file.
#The refrenced script, KatzeHerstellerin.ps1 (Roughly translated to Cat Manufacturer) is the script that actually applies the changes to the hosts file.
powershell_command = r"""Start-Process -Verb runAs -Wait powershell.exe -Args "cd """ + str(os.getcwd()) + r""" ; ./KatzeHerstellerin.ps1 -Force" """
p = subprocess.Popen(["powershell.exe", powershell_command], stdout=sys.stdout)


#establish general variables like port number and the picture of the cat that needs to be displayed
PORT = 80
DEFAULT_FILE = "katze.png"


#create simple http server that displays image of a cat as its only static content
#the changes in the hosts file is inteded to direct as much trafic as possible to this local server
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = DEFAULT_FILE
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


#signify data collection and editing is finished
print('done')


#leave the webserver running
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    httpd.serve_forever()