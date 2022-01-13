from apps import app
import os
import sys
import subprocess
import requests

def verify_new_branch(new_branch, ambiente):
    if ambiente == "hml":
        url_new_branch = "https://gitlab.ct.dk.th/infra-connect/deployment/lab/cards-private/env-hml/-/tree/" + new_branch
        url_api = "https://gitlab.ct.dk.th/api/v4/projects/1314/repository/branches"
    elif ambiente == "qa":
        url_new_branch = "https://gitlab.ct.dk.th/infra-connect/deployment/lab/cards-private/env-teste/-/tree/" + new_branch
        url_api = "https://gitlab.ct.dk.th/api/v4/projects/1313/repository/branches"    
    headers = { 'PRIVATE-TOKEN': 's9PwtsJ_b3t_D4bTzmqv' }
    api = requests.get(url_api, headers=headers).json()
    for i in api:
        for key, value in i.items():
            if value == url_new_branch:
                print(f"Branch {new_branch} existed")
                sys.exit()
                

def clone(new_branch, ambiente):
    if ambiente == "hml":
        subprocess.run(["git", "clone","git@gitlab.ct.dk.th:infra-connect/deployment/lab/cards-private/env-hml.git"], stdout=True)
        os.system("cd env-hml && git checkout eks-terraform && git checkout -b " + new_branch)
    elif ambiente == "qa":
        subprocess.run(["git", "clone","git@gitlab.ct.dk.th:infra-connect/deployment/lab/cards-private/env-teste.git"], stdout=True)
        os.system("cd env-teste && git checkout eks-terraform && git checkout -b " + new_branch)                
        


def push(NEW_COMMIT, ambiente, new_branch):
    NEW_PUSH = False
    if NEW_COMMIT:
        if ambiente == "hml":
            os.chdir("env-hml") 
        elif ambiente == "qa":
            os.chdir("env-teste")
        subprocess.run(["git", "status"], stdout=True)
        subprocess.run(["git", "add","."], stdout=True)
        subprocess.run(["git", "commit","-am", "add_new_app"], stdout=True)
        os.system("git push origin " + new_branch)
        NEW_PUSH = True
    else:
        print(f'unsolicited push as there are no repository changes')    
    return NEW_PUSH



def merge(ambiente, NEW_PUSH, new_branch):
    if NEW_PUSH:
        if ambiente == "hml":
            url_api = "https://gitlab.ct.dk.th/api/v4/projects/1314/merge_requests"
        elif ambiente == "qa":
            url_api = "https://gitlab.ct.dk.th/api/v4/projects/1313/merge_requests"
        title = "merge_request_branch_source_" +  new_branch + "_targe_eks_terraform"
        headers = { 'PRIVATE-TOKEN': 's9PwtsJ_b3t_D4bTzmqv' }
        form = { 'id': '1389', 'title': title, 'source_branch': new_branch, 'target_branch': 'eks-terraform', 'remove_source_branch': 'true' }
        requests.post(url_api, headers=headers, data=form)
    else:
        print(f'merge unsolicited why push unsolicited to branch {new_branch}')    
        
