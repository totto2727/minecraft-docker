#!/bin/bash

cd /opt/minecraft-server

NOW=`date "+%Y%m%d"`
zip ${NOW}.zip -r world world_nether world_the_end/
aws s3 cp ${NOW}.zip s3://${S3_BUCKET_NAME}/${MINECRAFT_SERVER_NAME}/world_backup/ --storage-class ONEZONE_IA
rm -f ${NOW}.zip