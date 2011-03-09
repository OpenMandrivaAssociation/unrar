%define name		unrar
%define summary		Decompressor for .rar format archives
%define version		4.00
%define fversion	4.0.7
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
Source:		http://www.rarlab.com/rar/%{name}src-%fversion.tar.gz
Url:		http://www.rarlab.com/rar_add.htm
License:	Freeware
Group:		Archiving/Compression
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Conflicts:	bash-completion < 20031225

%description
The unrar program is used to uncompress .rar format archives, which were
somewhat popular on DOS based machines.

%prep
%setup -q -n %name

%build
make -f makefile.unix CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}" STRIP=true

%install
rm -rf ${RPM_BUILD_ROOT}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 unrar $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc license.txt readme.txt
%{_bindir}/unrar

