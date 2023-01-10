import pyqrcode
import png
from pyqrcode import QRCode
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--url', '-url', required=True,
                    help='The url for where the QR code should go to')
parser.add_argument('--name', '-n', required=True,
                    help='Name QR code file, do not add file suffix')
parser.add_argument('--scale', '-s', required=True, help='Size of the QR code')

args = parser.parse_args()

website = args.url

url = pyqrcode.create(website)

url.svg(args.name+".svg", scale=args.scale)
url.png(args.name+".png", scale=args.scale)

print(
    f'Build QR Code for "{args.url}" to file "{args.name}".png/.svg. At size "{args.scale}"')
