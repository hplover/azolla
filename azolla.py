import argparse

import subprocess

class mylist(list):

    def __contains__(self, other):

        return super(mylist,self).__contains__(other.lower())



def check_port(value):

    ivalue = int(value)

    if ivalue >= 1024 and ivalue <= 65535:

        return ivalue

    raise argparse.ArgumentTypeError("port number must range from 1024 to 65535")



choices=mylist(["AES-128-CFB", "AES-192-CFB", "AES-256-CFB", "BF-CFB", "Camellia-128-CFB", "Camellia-192-CFB", "Camellia-256-CFB", "CAST5-CFB", "ChaCha20", "DES-CFB", "IDEA-CFB", "RC2-CFB", "RC4-MD5", "Salsa20", "SEED-CFB", "Serpent-CFB"]);

ip="45.32.51.20"

programName="azolla"



parser = argparse.ArgumentParser()

parser.add_argument("-p","--port",help="specify the port number[1024-65535]", type=check_port)

parser.add_argument("-P","--password",help="specify the password")

parser.add_argument("-L","--label",help="specify label", default="{}_{}".format(programName,ip))

parser.add_argument("-m","--method", help="specify method",choices=choices, default="AES-256-CFB")

parser.add_argument("-v","--verbose", help="view configuration",action="store_true" )

args = parser.parse_args()



if args.port!=None and args.password!=None:

    vport=args.port

    vpasswd=args.password

    vlabel="{}:{}".format(ip,vport)

    vmethod=args.method



    print(vport,vpasswd,vlabel,vmethod)



if args.verbose:

        print(args.port,args.password,args.label,args.method)
