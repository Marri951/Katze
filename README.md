==============================

-What Will It Do?-

Eventually, the program will fork into 2 sub-versions. 
- "Die Katze" will be the version to further the mutation of the hosts file, ntp, dns, and other aspects of networking.
  The end goal of "Die Katze" side of the program will be to, essentially, push Windows Operating System penetration testing to an extreme and take the system offline.
- "Der Computer" will be the version to further the data collection side of the program, with the end goal of furthering my pen-testing skill and opening a backdoor to the system.
  Basic information will be collected similarly to other data collection tools I've made and this will be coupled with opening the firewall for a port, listening, and allowing remote access.
  An ease add-on that may be done is, in essence, pcap: whether it be through literal local sniffing, or rerouting w/ poisoned VPN or router info. Additionally, if more network access can be gained there is plenty of space for even further goals.

=========================

-What Does It Currently Do?-

As of version 1.0, the program collects the public IPv4 address of the system and reroutes as much traffic as possible to just a picture of a cat.

To do so, the Python program notes the directory the program is operating and then does 2 preparation tasks. The first is to ensure that "firmen" (companies) is formatted properly. 
The second task is to break down the list of company names and begin creating various possible hostnames for said company. These names are placed in a temporary hostnames.txt file.
Perhaps most interestingly, the program then executes 3 PowerShell scripts. 

The first is not truly a script as it is simply just .popen(), which establishes a prompt and executes the second script.
This second script creates a new instance of PowerShell, in the current directory (to ensure access to files no matter the location), and with elevated (admin) privileges. 
In this new instance, the second script rights a single line, which executes KatzeHerstellerin.ps1 (Cat Factory), which applies all possible hostnames from the hostnames.txt file to the Windows hosts file.
The script associates every hostname with the local IPv4 address 127.0.0.1.

Lastly, a simple HTTP server is created that is set to host static content for the 127.0.0.1 local address. The only file that is to be displayed by this server is a picture of a cat.

An interesting side effect that I've found is that given the local server is not yet developed for HTTPS, any HTTPS requests that are made to a company's site simply won't work.
In essence, any requests made to a site that's listed in the temporary hostnames file will either fail to do anything or only show a picture of a cat.

========================

-When is it okay to use?-

This is only to be used on your, personally owned, personally managed, free to do what you want with system. I WILL NEVER CONDONE the use of this program on any system.
I will still not condone it, but if you do choose to run this on your own system, ensure that you read and understand ALL OF the program's source code AND are FULLY CONSENTING to the operation of the program and ANY possible effects that may result.
I will never be responsible for anything you do with this program. YOU ARE THE ONE RESPONSIBLE. With this program, to use it on ANY SYSTEM would be against my wishes and objectively not in the name of learning.
This program is intended largely as a platform for learning about pen-testing and how Windows operates in regard to networking.
The program has been posted to allow others to learn from my mistakes and advancements to improve their own knowledge and skill set, to give me cloud-stored copies of the source code in case my copies corrupt, and to improve my knowledge and skill.
