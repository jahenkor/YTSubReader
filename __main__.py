import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c","--channelid", help="Skip google-auth, uses channel-id only",
                    action= "store_true")
parser.add_argument("-g","--googleauth", help="Use google-auth",
                    action= "store_true")
args = parser.parse_args()
if args.channelid:
    print("You have selected channel-id as reader input")
elif args.googleauth:
    print("Selected google-auth")
else: 
    print("Use -h for help")
    sys.exit(0)


