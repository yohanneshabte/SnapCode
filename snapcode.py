import argparse
import sys
import urllib.request

url = "https://app.snapchat.com/web/deeplink/snapcode?username={}&type={}"


def get_code(username, bitmoji):

	if bitmoji == False:

		# If filetype is PNG, you will get the 
		# SnapCode without the bitmoji

		filetype = "PNG"

	else:

		# If filetype is SVG, you will get the 
		# SnapCode with the bitmoji

		filetype = "SVG"

	# Putting all the information into the url
	request_url = url.format(username, filetype)

	# Making the filename
	path = str(username) + "." + filetype.lower()

	# Downloading the image file
	urllib.request.urlretrieve(request_url, path)

	print("Downloaded ---> " + path)


def main():

	parser = argparse.ArgumentParser(description = "A simple command-line tool to download SnapChat codes.")

	parser.add_argument('username', action = "store")

	parser.add_argument("-b", "--bitmoji",
		                action= "store_true",
						help = "SnapCode with Bitmoji")

	args = parser.parse_args()

	if len(sys.argv) == 1: # if no argument is given then show help
		parser.print_help()

	get_code(args.username, args.bitmoji)

if __name__=="__main__":
	main()
