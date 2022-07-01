import os
import time

while True:
    filename = "plantfem_22.04-ubuntu2004_amd64.deb"
    os.system("git clone https://github.com/kazulagi/plantFEM.git deb_build && cd deb_build && sh install/install_all")
    os.system("cp -fv deb_build/plantfem plantFEM/usr/local/bin/plantfem")
    os.system("cp -fv deb_build/bin/soja plantFEM/usr/local/bin/soja")
    os.system("cp -rfv deb_build plantFEM/opt/plantfem")
    os.system("rm -rf plantFEM/opt/plantfem/.git")
    os.system("sh build_deb.sh")
    os.system("rm -rf deb_build")
    time.sleep(60*60*24)