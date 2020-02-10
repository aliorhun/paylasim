#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import re
import os
from sys import stderr



# Get Hostname ----------------------------------------------------------------------------------

def getHostname():
    command = "hostname"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    return out

def getWhoAmI():
    command = "whoami"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    return out


# Get All Users and Groups with Permissions ------------------------------------------------------

def UserAndGroupPermissions(dosyaAdi):
    command = "getfacl -p " + dosyaAdi
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    output = str(out).replace("\\n", "\n")

    # acl perm
    regex = re.compile(r'(user:(.*)|group(.*))', re.MULTILINE)
    matches = [m.groups() for m in regex.finditer(str(output))]

    # posix perm
    regex2 = re.compile(r'(owner: (.*)|group: (.*))', re.MULTILINE)
    matches2 = [m.groups() for m in regex2.finditer(str(output))]

    user_permission = list()
    for i in matches:
        if "user::" in i[0]:
            newstr1=str(i[0].replace("user::", "user [P]:"+matches2[0][1]+":")+", "+i[1]+", "+str(i[2]))
            i = tuple(map(str, newstr1.split(',')))
        if "group::" in i[0]:
            newstr1=str(i[0].replace("group::", "group [P]:"+matches2[0][1]+":")+", "+str(i[1])+", "+str(i[2]))
            i = tuple(map(str, newstr1.split(',')))
        user_permission.append(list(i))
    return user_permission


# Users -----------------------------------------------------------------------------------------

def removeUser(username,filename):
    command = "setfacl -x u:" + username + " " + filename
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out, error) = proc.communicate()
    if error:
        return False
    else:
        return True


# Groups -----------------------------------------------------------------------------------------

def removeGroup(groupname,filename):
    command = "setfacl -x g:" + groupname + " " + filename
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out, error) = proc.communicate()
    if error:
        return False
    else:
        return True

# Give Permissions --------------------------------------------------------------------------------

def userAllow(username, izinturu, filename):
    command = "setfacl -m u:" + username + ":" + izinturu + " " + filename
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out, error) = proc.communicate()
    if error:
        return False
    else:
        return True


def groupAllow(groupname, izinturu,filename):
    command = "setfacl -m g:" + groupname + ":" + izinturu + " " + filename
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out, error) = proc.communicate()
    if error:
        return False
    else:
        return True

# Samba Share  --------------------------------------------------------------------------------

def create(sharefile):
    command = "mkdir -p /mnt/" + sharefile
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out, error) = proc.communicate()
    if error:
        return False
    else:
        return True


def Samba_Share(password,path):
    command = 'echo ' + password + '| sudo -S mount -t cifs //10.154.25.164/betul """%s"""/ -o username=administrator,password=SambaPardus01,domain=WORKGROUP,vers=3.0' %path
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = proc.communicate()
    if error:
        return False
    else:
        return True




def UserAndGroupPermissionsWindows(path):

    command = "getcifsacl " + path
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    output = str(out).replace("\\n", "\n")

    if ("getxattr error: 95" in output):
        command = "getfacl " + path
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        (out, error) = proc.communicate()
        output = str(out).replace("\\n", "\n")
        user_permission = list()
        print("aliveli"+output)
    else:
        regex = re.compile(r'ACL:(.*)', re.MULTILINE)
        matches = [m.groups() for m in regex.finditer(str(output))]
        user_permission = list()
        for i in matches:
             user_permission.append(list(i))
    return user_permission


# Samba Share  --------------------------------------------------------------------------------

def shareFile(password, sharingName, path):

    #written="""[ kartal $]\ncomment = kartal\npath = %s \nbrowseable = yes\nguest ok = yes\nread only = yes\npublic = yes\nwritable = yes """ % (path)
    written="""[{0}$]\ncomment = {1}\npath = {2} \nbrowseable = yes\nguest ok = yes\nread only = yes\npublic = yes\nwritable = yes\n""".format(sharingName, sharingName, path)
    command = 'echo ' + password + ' | sudo -S sh -c \'echo """%s""">> /etc/samba/smb.conf\'' %written
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out, error) = proc.communicate()
    if error:
        return False
    else:
        return True


def startSamba():
    command = "service smbd restart"
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    return out


def searchOnFile(keyword):
    command = "grep -rnw '/etc/samba/smb.conf' -e '\[{0}\$\]'".format(keyword)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    if out:
        return True
    else:
        return False

def isShared(path):
    command = "cat /etc/samba/smb.conf | grep {0}".format(path)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    if out:
        return True
    else:
        return False

def getShareName(path):
    command = "cat /etc/samba/smb.conf | grep -B2 {0} | head -1 | head -c -3 | tail -c +2".format(path)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    if out:
        return out
    else:
        return ""


def controlSharePath(path):

    file=open("/etc/samba/smb.conf","r")
    lines=file.readlines()
    currentIndex=0
    comparePath = "path = " + path + " \n"

    for i in lines:
        if comparePath == i:
            shareindex=lines[currentIndex-1]
            return shareindex
        currentIndex=currentIndex+1

    return " "


def mountControl(path):

    command = "mount | grep " + path
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    (out, error) = proc.communicate()
    if out:
        return True
    else:
        return False

def mountsearch(path):

    path2=list()
    path2.append(path.split("/"))

    count=len(path2[0])

    mounted=mountControl(path)
    if(mounted == True):
        return mounted
    else:
        for j in range(1,count-4):
                uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
                path3=uppath(path,j)


                ismount=mountControl(path3)
                if(ismount == True):
                    mounted=True

                else:
                    mounted=False

        return mounted

