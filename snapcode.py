import argparse
import sys
import urllib.request

__version__ = "v1.0"
url = "https://app.snapchat.com/web/deeplink/snapcode?username={}&type={}&bitmoji={}"


def get_code(username, bitmoji_option):

	if bitmoji_option == False:
		
		bitmoji_option = "disbale"
		filetype = "PNG"

	else:
		bitmoji_option = "enable"
		filetype = "SVG"

	request_url = url.format(username, filetype, bitmoji_option)
	
	path = str(username)+"."+filetype.lower()

	urllib.request.urlretrieve(request_url, path)
	print("Downloaded ---> "+path)


def main():

	parser = argparse.ArgumentParser(description = "A simple command-line tool to download SnapChat codes.")
	
	parser.add_argument("-v", "--version",
		action='store_true',
		help = "Get current version")

	parser.add_argument("-u", "--username",
		type=str,
		required=True,
		help = "SnapChat username")

	parser.add_argument("-b", "--bitmoji_option", type = bool,
						default = False,
						choices=[True, False],
						help = "If you want a Bitmoji in the center of the snapcode")

	args = parser.parse_args()

	if len(sys.argv) == 1: # if argument is given then show help
		parser.print_help()

	elif args.version:
		print(__version__)

	get_code(args.username, args.bitmoji_option)

if __name__=="__main__":
	main()