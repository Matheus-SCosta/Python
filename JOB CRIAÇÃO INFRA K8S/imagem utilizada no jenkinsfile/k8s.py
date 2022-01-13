import os
import subprocess
import shutil



def verify_existed(name_deployment, name_ingress, name_app, ambiente):
    NEW_COMMIT = False
    NEW_DEPLOYMENT = True
    NEW_INGRESS = True
    if ambiente == "hml":
        deployments_existente = os.listdir("env-hml/deployments/")
        ingress_existentes = os.listdir("env-hml/ingress/")
        for i in range (len(deployments_existente)):
            if deployments_existente[i] == name_deployment:  NEW_DEPLOYMENT = False
            if ingress_existentes[i] == name_ingress:  NEW_INGRESS = False
    elif ambiente == "qa":
        deployments_existente = os.listdir("env-teste/deployments/")
        ingress_existentes = os.listdir("env-teste/ingress/")
        for i in range (len(deployments_existente)):
            if deployments_existente[i] == name_deployment: NEW_DEPLOYMENT = False
            if ingress_existentes[i] == name_ingress:  NEW_INGRESS = False         
    criando_deployment(name_deployment, name_app, ambiente, NEW_DEPLOYMENT)
    criando_ingress(name_ingress, name_app, ambiente, NEW_INGRESS)
    if NEW_DEPLOYMENT or NEW_INGRESS:
        NEW_COMMIT = True
    return NEW_COMMIT    
    


def criando_deployment(name_deployment, name_app, ambiente, NEW_DEPLOYMENT):
    if NEW_DEPLOYMENT:
        if ambiente == "hml":
            template = "env-hml/deployments/template-deployment.yaml"
            arquive = "env-hml/deployments/" + str(name_deployment)
        elif ambiente == "qa":
            template = "env-teste/deployments/template-deployment.yaml" 
            arquive = "env-teste/deployments/" + str(name_deployment)
        shutil.copyfile(template, arquive)
        with open(arquive, encoding='utf-8') as arq:
            newText = arq.read().replace('EMISSOR', name_app)
        with open(arquive, "w", encoding='utf-8') as arq:
            arq.write(newText)
        print(f'Deployment file created for {name_app} issuer')
    else:
        print(f'Deployment file for existing {name_app} issuer, not created')    


def criando_ingress(name_ingress, name_app, ambiente, NEW_INGRESS):
    if NEW_INGRESS:
        if ambiente == "hml":
            template = "env-hml/ingress/template-ingress.yaml" 
            arquive = "env-hml/ingress/" + str(name_ingress)
        elif ambiente == "qa":
            template = "env-teste/ingress/template-ingress.yaml" 
            arquive = "env-teste/ingress/" + str(name_ingress)
        shutil.copyfile(template, arquive)       
        with open(arquive) as arq:
            newText = arq.read().replace('EMISSOR', name_app)
        with open(arquive, "w") as arq:
            arq.write(newText)
        print(f'Deployment file created for {name_app} issuer')
    else:
        print(f'Deployment file for existing {name_app} issuer, not created')    
    
                    
def apply_cluster(name_app, name_deployment, name_ingress, ambiente):
    status_exit = subprocess.call(['kubectl','get','deployment', name_app ,'-n','core-privatehml'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if status_exit != 0:
        if ambiente == "hml":
            yaml = "/home/jenkins/agent/workspace/CREATE_APP_CARDS_PRIVATE/env-hml/deployments/" + name_deployment
            subprocess.run(['kubectl','apply', '-f', yaml], stdout=True)  
        elif ambiente == "qa":
            yaml = "/home/jenkins/agent/workspace/CREATE_APP_CARDS_PRIVATE/env-teste/deployments/" + name_deployment
            subprocess.run(['kubectl','apply', '-f', yaml], stdout=True) 
    
    ingress = name_ingress[:-5]
    status_exit = subprocess.call(['kubectl','get','ingress', ingress ,'-n','core-privatehml'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    if status_exit != 0:
        if ambiente == "hml":
            yaml = "/home/jenkins/agent/workspace/CREATE_APP_CARDS_PRIVATE/env-hml/ingress/" + name_ingress
            subprocess.run(['kubectl','apply', '-f', yaml], stdout=True)  
        elif ambiente == "qa":
            yaml = "/home/jenkins/agent/workspace/CREATE_APP_CARDS_PRIVATE/env-teste/ingress/" + name_ingress
            subprocess.run(['kubectl','apply', '-f', yaml], stdout=True)
