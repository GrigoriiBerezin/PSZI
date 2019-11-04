@echo off
@icacls "template.tbl" /deny TestUser:F

:loop
for /F %%i in (template.tbl) do (
 	cls
	@touch %%i
 	@icacls %%i /deny TestUser:F
)
goto loop
