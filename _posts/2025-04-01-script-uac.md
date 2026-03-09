---
layout: post
title:  "Script per la disabilitazione dell'UAC da remoto"
date:   2025-04-01
tags: script, powershell, windows, security
category: [Programming,Server] #One, more categories or no at all.
author: jpo85 #Author's nick.
nextPart: #Next part.
prevPart: #Previous part.
og_image: #Open Graph preview image.
og_description: "descrizione." #Open Graph description.
fb_app_id: example
---

# Script per la disabilitazione dell'UAC da remoto

> scrivere nel file lista_host.txt gli ip o l'hostname delle macchine su cui disabilitare l'uac

```powershell
$credential = Import-CliXml -Path "e:\script\cred_symantec_ad.xml"
$files = Get-Content -Path .\lista_host.txt


foreach ($host_item in $files) {
    Invoke-Command -Credential $Credential -ComputerName $host_item -ScriptBlock {
    $path = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    $filter="ConsentPromptBehaviorAdmin|PromptOnSecureDesktop"
    Write-Host "PRIMA DELLA MODIFICA UAC:" -BackgroundColor green
        (Get-ItemProperty $path).psobject.properties | where {$_.name -match $filter} | select name,value

    Set-ItemProperty -Path $path -Name "ConsentPromptBehaviorAdmin" -Value "0"
    Set-ItemProperty -Path $path -Name "PromptOnSecureDesktop" -Value "0"
    Write-Host "DOPO LA MODIFICA UAC:" -BackgroundColor green
        (Get-ItemProperty $path).psobject.properties | where {$_.name -match $filter} | select name,value
    }
}
```