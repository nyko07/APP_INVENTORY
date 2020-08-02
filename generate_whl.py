import os
import setuptools

components = setuptools.find_packages()

os.system('python3 -m pip install --upgrade setuptools wheel')
os.chdir('./Orchestrator/API')
os.system('python3 ../../API/setup.py sdist bdist_wheel')
os.system('echo "......................generated binary API........................"')
os.chdir('../../Orchestrator/Back')
os.system('python3 ../../Core/setup.py sdist bdist_wheel')
os.system('echo "......................generated binary Core........................"')
os.chdir('../../Orchestrator/Back')
os.system('python3 ../../Notification/setup.py sdist bdist_wheel')
os.system('echo "......................generated binary Notifications........................"')
os.chdir('../../Orchestrator/Front')
os.system('python3 ../../GUI/setup.py sdist bdist_wheel')
os.system('echo "......................generated binary GUI........................"')
#os.chdir('../../Orchestrator/Front')
#os.system('python3 ../../GUI2/setup.py sdist bdist_wheel')
#os.system('echo "......................generated binary GUI2........................"')
os.chdir('../../Orchestrator/Orchestrator')
os.system('python3 ../../Orchestrator/setup.py sdist bdist_wheel')
os.system('echo "......................generated binary Orchestrator........................"')

print(components)
