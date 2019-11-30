'''
Author: Prem Kumar 
Roll No:- SCETB461

A ZipFile Password Cracker

'''

import optparse
import zipfile

#if 'passwd' is the zipFile passwd , returns passwd else return null
def extractFile(zFile, passwd):
    try:
        zFile.extractall(pwd=passwd)
        return passwd

    except:
        

#parsing cmd line arguments and other options using optparse

usage = "Usage: python3 zip-crack.py -z|--zipFile <zip file> -d|--dictFile <dictionary file> \n\t\n  python3 zip-crack.py  -h|--help"

parser = optparse.OptionParser(usage)

parser.add_option("-z","--zipFile", dest="zipFile", help="Target ZipFile")
parser.add_option("-d","--dictFile", dest="dictFile", help="input dictionary file name containing passwords")

(options,args) = parser.parse_args()

if (options.dictFile == None) or (options.zipFile == None) :
    print(usage)
    exit(0)
else:
    dictFile = options.dictFile
    zipFile = options.zipFile


dict = open(dictFile)
zip = zipfile.ZipFile(zipFile)
for foo in dict.readlines():
    passwd = foo.strip('\n')
    guess = extractFile(zip,passwd)
    if guess:
        print("[+] ZipFile  Cracked\nPassword:= " + passwd + "\n")
        exit(0)
    else:
        print("[-] ZipFile not cracked")


