Name: 		freshmemory
Version:	1.0
Release:	%mkrel 1
License:	GNU GPL v3 
Summary:	fresh memory 
Group:		Education
URL:		https://sourceforge.net/projects/freshmemory/files/freshmemory/
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel >= 4.7.0
BuildRequires:	gcc
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
freshmemory

%prep
%setup -q

%build
qmake
make release

%install
make install

%files

%clean
