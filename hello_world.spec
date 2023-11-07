Name: hello_world
Version: 1.0
Release: 1%{?dist}
Summary: Simple Hello World App

License: MIT
Group: Applications/System
Source0: hello_world.py

%description
This is a simple Hello World app in Python.

%prep
# Ніяких підготовчих дій для цього додатка

%build
# Ніяких підготовчих дій для цього додатка

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 hello_world.py %{buildroot}/usr/local/bin/hello_world

%files
/usr/local/bin/hello_world

%changelog
* Date Your Name <your.email@example.com>
- Initial build of hello_world RPM package
