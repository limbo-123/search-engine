#!/bin/bash 

check_deployment=$(kubectl describe deployment search-engine-alpha)
if [ $(echo $?) == 0 ]; then
kubectl delete deployment search-engine-alpha
kubectl delete svc search-engine-alpha
sleep 5
fi
