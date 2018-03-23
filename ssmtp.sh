#!/bin/bash
# ~/SPiBox/ssmtp.sh
# Creado el 23/03/2018

## EJEMPLO DE USO ##
# FUNCIONA SOLO CON CUENTAS DE GMAIL #
# sudo ./SpiBox/ssmtp.sh 12servicios.com clave_de_gmail

## CODIGO ##
sed -i 's/^mailhub=.*/mailhub=smtp.gmail.com:587/g' /etc/ssmtp/ssmtp.conf
sed -i 's/^#FromLineOverride=YES/FromLineOverride=YES/g' /etc/ssmtp/ssmtp.conf
sudo echo "# [GMAIL]
AuthUser=$1@gmail.com
AuthPass=$2
UseSTARTTLS=YES">> /etc/ssmtp/ssmtp.conf
