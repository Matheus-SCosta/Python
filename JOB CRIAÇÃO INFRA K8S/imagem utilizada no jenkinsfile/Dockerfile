FROM registry.ct.dk.th/imagem/k8s_config:corePrivateNew
RUN yum -y update && \
    yum install -y git && \
    yum install -y python3 && \
    pip3 install requests && \
    git config --global user.email "jenkins@emp.com.br" && \
    git config --global user.name "jenkins" && \
    aws eks --region us-east-1 update-kubeconfig --name CLUSTER-LAB

ADD apps.py main.py git.py k8s.py efs.py /
