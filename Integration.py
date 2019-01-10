#!/usr/bin/python
import argparse
import json,os
import requests
from requests.auth import HTTPDigestAuth, HTTPBasicAuth
# agrument
parser = argparse.ArgumentParser()
parser.add_argument('--action', action='store',choices=['Create','Update','Approval'], help='Action To Be Performed')
parser.add_argument("-b","--build_tag", help="BUILD_TAG of the project",required=False)
parser.add_argument("-e","--email", help="Email Address of the Committer",required=False)
parser.add_argument("-t","--ticker_number", help="Ticket Number",required=False)
parser.add_argument("-c","--comment", help="Comment",required=False)
parser.add_argument("-s","--status", help="status",required=False)
parser.add_argument("-f","--filename", help="name of file",required=False)
args = parser.parse_args()

SNC_URL = 'https://dev60806.service-now.com'
SNC_USER = 'vdenge'
SNC_PASS = 'Welcome1'

def get_changeNumber(url):
    response=requests.get(url=SNC_URL+url,auth=HTTPBasicAuth(SNC_USER, SNC_PASS))
    if response.status_code==200:
        print  response.json()['records'][0]['number']

def get_approival_status(url):
    Approval= ['rejected','approved']
    Approval_Status=''
    flag=True
    while flag:
        response=requests.get(url=SNC_URL+url,auth=HTTPBasicAuth(SNC_USER, SNC_PASS))
        if response.status_code==200:
            Approval_Status=response.json()['records'][0]['approval']
            if Approval_Status in Approval:
                flag=False
    return Approval_Status
    
def createChange():
    snowURL= SNC_URL + "/api/now/table/u_jenkin_chg_staging_table"
    build = args.build_tag
    email=args.email
    #create payload
    data = {"u_watch_list":email,"u_requested_by":"c8ac7329db1ca30002a9793ebf9619a0","u_short_description":"This ticket is related to build: {}".format(build),"u_description":"Sample ticket","u_raised_by_jenkins":"true","u_build_version_number":build}

    try:
        r = requests.post(url=snowURL, data=json.dumps(data), auth=HTTPBasicAuth(SNC_USER, SNC_PASS))
        if r.status_code==201:
            TicketNumber=get_changeNumber("/change_request.do?JSONv2&sysparm_query=u_build_version_number={}&sysparm_limit=1".format(build))
    except requests.exceptions.RequestException as e:
        print ("Error: "+ e)

def updateChange():
    snowURL = SNC_URL + "/api/now/table/u_jenkin_chg_staging_table"
    ticket_number=args.ticker_number
    comment=args.comment
    build = args.build_tag
    status = args.status
    if comment==None and status!=None:
        data = {"u_change_request": ticket_number, "u_build_version_number": build,"u_build_status":status}
    else:
        data = {"u_change_request": ticket_number, "u_build_version_number": build, "u_comments": comment}
    try:
        r = requests.post(url=snowURL, data=json.dumps(data), auth=HTTPBasicAuth(SNC_USER, SNC_PASS))
    except requests.exceptions.RequestException as e:
        print ("Error: "+ e)

def Approval():
    ticket_number=args.ticker_number
    Approval_status=get_approival_status("/change_request.do?JSONv2&sysparm_query=number={}&sysparm_limit=1".format(ticket_number))
    print Approval_status

if __name__== "__main__":
    if args.action == "Create":
        createChange()
    elif args.action== "Update":
        updateChange()
    elif args.action== "Approval":
        Approval()
    
    else:
        pass
