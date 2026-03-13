---
layout: post
title:  "Guida per fare il backup SAN"
date:   2026-03-13
tags: server, storage, backup
category: [Server,Storage,Backup] #One, more categories or no at all.
author: jpo85 #Author's nick.
nextPart: #Next part.
prevPart: #Previous part.
og_image: #Open Graph preview image.
og_description: "descrizione." #Open Graph description.
fb_app_id: example
---
Per fare il backup della san, procediamo con l'esportare la configurazione dello zoning sui due switch SAN.  

Per fare questo abbiamo bisogno di un server scp da dare al comando nello switch per esportare la configurazione in txt.  

### Questi sono i comandi che utilizzeremo avendo ubuntu come server scp .

installa il server open-ssh
```bash
sudo apt install openssh-server
sudo systemctl enable --now ssh
```
```bash
sudo systemctl status ssh
```

avremo questo risultato
```bash
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/usr/lib/systemd/system/ssh.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-03-11 17:02:35 CET; 2s ago
TriggeredBy: ● ssh.socket
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 139092 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 139093 (sshd)
      Tasks: 1 (limit: 9203)
     Memory: 2.9M (peak: 3.4M)
        CPU: 18ms
     CGroup: /system.slice/ssh.service
             └─139093 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

Mar 11 17:02:35 buntupic systemd[1]: Starting ssh.service - OpenBSD Secure Shell server...
Mar 11 17:02:35 buntupic sshd[139093]: Server listening on 0.0.0.0 port 22.
Mar 11 17:02:35 buntupic sshd[139093]: Server listening on :: port 22.
Mar 11 17:02:35 buntupic systemd[1]: Started ssh.service - OpenBSD Secure Shell server.
```
0.0.0.0 port 22 indica che è in ascolto su tutti gli ip. verifichiamo l'ip del server
```bash
ip addr | grep eno1
```
considerando che il firewall di ubuntu sia disabilitato  

connettersi allo switch **san1**
```bash
ssh admin@10.10.10.1
```

```bash
san1:admin> 
san1:admin> configupload
Protocol (scp, ftp, sftp, local) [ftp]: scp
Server Name or IP Address [host]: 10.10.10.5 # IP server scp
User Name [user]: jacopo #user server scp
Path/Filename [<home dir>/config.txt]: san1-10-10-10-1.txt # nome file conf.txt
Section (all|chassis|switch [all]): all
jacopo@10.10.10.1's password:

configUpload complete: All selected config parameters are uploaded
```
ha salvato la configurazione nel file **san1-10-10-10-1.txt** dentro la home dell'utente

questo task va eseguito anche per il secondo switch **san2**

# Guida per fare il restore della SAN

tirare su lo stesso server scp da dove prenderà il file  

connettersi allo switch **san1**
```bash
ssh admin@10.10.10.1
```

```bash
configdownload
```
andare a prendere il file **san1-10-10-10-1.txt**  

questo task va eseguito anche per il secondo switch **san2**  
andando aprendere il file **san2-10-10-10-2.txt**
