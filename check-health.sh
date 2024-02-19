#!/bin/bash
while true
do
    kubectl get pod -n discord-bot-dev | grep Running
    if [ $? -eq 0 ]
    then
        break
    fi
done
echo "Pod is running!"
