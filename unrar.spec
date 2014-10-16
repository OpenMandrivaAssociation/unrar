%define oversion 5.1.5

Name:		unrar
Version:	5.10
Release:	2
Summary:	Decompressor for .rar format archives
Source0: 	http://www.rarlab.com/rar/%{name}src-%oversion.tar.gz
Url:		http://www.rarlab.com/rar_add.htm
License:	Freeware
Group:		Archiving/Compression
Conflicts:	bash-completion < 20031225

%description
The unrar program is used to uncompress .rar format archives, which were
somewhat popular on DOS based machines.

%prep
%setup -qn %{name}

%build
make -f makefile CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags} -pthread" STRIP=true

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 unrar %{buildroot}%{_bindir}

%files
%doc license.txt readme.txt
%{_bindir}/unrar
