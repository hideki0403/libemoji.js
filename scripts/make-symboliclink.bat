@echo off

cd %~dp0..

rmdir .\externals\libemoji
mkdir C:\repo\libemoji
mklink /D .\externals\libemoji C:\repo\libemoji
