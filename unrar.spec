%define oversion 4.1.2
%define prerel beta2
Name:		unrar
Version:	4.10
Release:	%mkrel -c %prerel 1
Summary:	Decompressor for .rar format archives
Source: 	http://www.rarlab.com/rar/%{name}src-%oversion.tar.gz
Url:		http://www.rarlab.com/rar_add.htm
License:	Freeware
Group:		Archiving/Compression
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Conflicts:	bash-completion < 20031225

%description
The unrar program is used to uncompress .rar format archives, which were
somewhat popular on DOS based machines.

%prep
%setup -qn %{name}

%build
make -f makefile.unix CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}" STRIP=true

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 unrar %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc license.txt readme.txt
%{_bindir}/unrar

