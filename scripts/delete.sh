#
# Destroys the pythons microservice on Kubernetes.
#
# Environment variables:
#
#   CONTAINER_REGISTRY - The hostname of your container registry.
#   VERSION - The version number of the image to deploy.
#
# Usage:
#
#   ./scripts/deploy.sh
#

set -u # or set -o nounset
: "$CONTAINER_REGISTRY"
: "$VERSION"
: "$DATABASE_URL"

envsubst < ./scripts/kubernetes/deployment.yaml | kubectl delete -f -
envsubst < ./scripts/kubernetes/service.yaml | kubectl delete -f -