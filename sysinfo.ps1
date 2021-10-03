function getIP{ 

    (get-netipaddress).ipv4address | Select-String "192*" 

} 
Get-Date -DisplayHint Date


write-host(getIP) 
$IP = getIP
$USER = $env:USERNAME
$DATE = Get-Date -DisplayHint Date
$HOSTNAME = $env:COMPUTERNAME

$BODY = "This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. Today's Date is $DATE"
Send-MailMessage -To "rohanpatelxf@gmail.com" -From "rohanpatelxf@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 
##botheaj@ucmail.uc.edu
write-host($BODY)