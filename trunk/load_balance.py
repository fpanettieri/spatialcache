import urllib

def update_server_list(available_servers):
	working_servers = []
	opener = urllib.FancyURLopener()
	for i in available_servers:
		response = opener.open(i).code
		if response == 200:
			working_servers.append(i)
	return working_servers
