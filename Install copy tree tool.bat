@echo off
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------    
:: Add Registry Keys
set "ph=%~dp0"
set "cp=dist\copytree\copyTree.exe"
set "pt=dist\PASTET~1\pastetree.exe"
set cfpath=%ph%%cp%
set pfpath=%ph%%pt%
set cfparg=%cfpath% %%1
set cfpargi=%cfpath% %%v
set pfpargi=%pfpath% %%v
REM set pfpargi="C:\Users\x'j\AppData\Local\Programs\Python\Python38-32\python.exe" %pfpath% %%v
reg add HKCR\*\shell\dirtreecopy /v MUIVerb /t REG_SZ /d "Directory Tree..." /f
reg add HKCR\*\shell\dirtreecopy /v subcommands /t REG_SZ /f

reg add HKCR\*\shell\dirtreecopy\shell\copytree /t REG_SZ /d "Copy" /f
reg add HKCR\*\shell\dirtreecopy\shell\copytree\command /t REG_SZ /d "%cfparg%" /f

reg add HKCR\Directory\Background\shell\dirtreecopy /v MUIVerb /t REG_SZ /d "Directory Tree..." /f
reg add HKCR\Directory\Background\shell\dirtreecopy /v subcommands /t REG_SZ /f

REM reg add HKCR\Directory\Background\shell\dirtreecopy\shell\copytree /t REG_SZ /d "Copy" /f
REM reg add HKCR\Directory\Background\shell\dirtreecopy\shell\copytree\command /t REG_SZ /d "%cfpargi%" /f

reg add HKCR\Directory\Background\shell\dirtreecopy\shell\pastetree /t REG_SZ /d "Paste" /f
reg add HKCR\Directory\Background\shell\dirtreecopy\shell\pastetree\command /t REG_SZ /d "%pfpargi%" /f