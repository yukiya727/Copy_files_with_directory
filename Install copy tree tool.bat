@echo off
reg add HKCR\*\shell\dirtreecopy /v MUIVerb /t REG_SZ /d "Directory tree..."
reg add HKCR\*\shell\dirtreecopy /v subcommands /t REG_SZ

reg add HKCR\*\shell\dirtreecopy\shell\copytree /t REG_SZ /d "Copy"
reg add HKCR\*\shell\dirtreecopy\shell\copytree\command /t REG_SZ /d "%CD%/copytree.exe"

reg add HKCR\*\shell\dirtreecopy\shell\pastetree /t REG_SZ /d "Paste"
reg add HKCR\*\shell\dirtreecopy\shell\pastetree\command /t REG_SZ /d "%CD%/copytree.exe"
pause