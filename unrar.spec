%define name		unrar
%define summary		Decompressor for .rar format archives
%define version		3.80
%define prerel beta1
%define fversion	3.8.1
%define rel		1
%define release %mkrel  0.%prerel.%rel

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
Source:		http://www.rarlab.com/rar/%{name}src-%fversion.tar.gz
Source1:	unrar-bash-completion-20031225.bz2
Url:		http://www.rarlab.com/rar_add.htm
License:	Freeware
Group:		Archiving/Compression
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Conflicts:	bash-completion < 20031225

%description
The unrar program is used to uncompress .rar format archives, which were
somewhat popular on DOS based machines.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %name

%build
make -f makefile.unix CXXFLAGS="$RPM_OPT_FLAGS" STRIP=true

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 unrar $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 %buildroot/%_sysconfdir/bash_completion.d
bzip2 -cd %SOURCE1 > %buildroot/%_sysconfdir/bash_completion.d/unrar

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc license.txt readme.txt
%config(noreplace) %_sysconfdir/bash_completion.d/unrar
%{_bindir}/unrar

