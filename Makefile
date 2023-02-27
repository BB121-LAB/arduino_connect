all:
	make premake
	python3 -m PyInstaller --clean --name="Arduino Connect" --windowed --onedir --icon=icon/icon.png ard_connect.py 
onefile:
	make premake
	python3 -m PyInstaller --onefile ard_connect.py
premake:
	make install-reqs
	pip3 install pyinstaller --user
install-reqs:
	pip3 install -r requirements.txt --user
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf __pycache__/
	rm -f *.spec
ve-build:
	pip3 install virtualenv --user
	virtualenv ard_connect_build
	. ./ard_connect_build/bin/activate
	make
	deactivate
ve-delete:
	rm -rf ard_connect_build
build-ui:
	pyuic5 connect.ui > connect.py
	pyuic5 about.ui > about.py
	pyuic5 license.ui > license.py
