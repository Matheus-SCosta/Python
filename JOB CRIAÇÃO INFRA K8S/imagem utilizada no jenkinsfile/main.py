from apps import app
from git import verify_new_branch, clone, push, merge
from k8s import apply_cluster, verify_existed
from efs import efs_create_directory
import sys

emissor = sys.argv[1]
ambiente = sys.argv[2]
new_branch = sys.argv[3]


def create_object(emissor, ambiente, new_branch):
    app_object = app(name_app = emissor, ambiente = ambiente, new_branch = new_branch)
    return app_object

if __name__ == "__main__":
    verify_new_branch(new_branch, ambiente)
    clone(new_branch, ambiente)
    app_object = create_object(emissor, ambiente, new_branch)
    NEW_COMMIT = verify_existed(app_object.name_deployment, app_object.name_ingress, app_object.name_app, app_object.ambiente)
    NEW_PUSH = push(NEW_COMMIT, app_object.ambiente, app_object.new_branch)
    merge(app_object.ambiente, NEW_PUSH, app_object.new_branch)
    efs_create_directory(app_object.name_app, app_object.ambiente)
    apply_cluster(app_object.name_app, app_object.name_deployment, app_object.name_ingress, app_object.ambiente)
