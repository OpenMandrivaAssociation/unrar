%define mdkversion		%(perl -pe '/(\\d+)\\.(\\d)\\.?(\\d)?/; $_="$1$2".($3||0)' /etc/mandrake-release)
%define name		unrar
%define summary		Decompressor for .rar format archives
%define version		3.71
%define prerel beta1
%define fversion	3.7.8
%define rel		0.%prerel.1
%define release %mkrel %rel
%define distsuffix plf
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
Source:		http://www.rarlab.com/rar/%{name}src-%fversion.tar.gz
Source1:	unrar-bash-completion-20031225.bz2
Url:		http://www.rarlab.com/rar_add.htm
License:	freeware
Group:		Archiving/Compression
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
%if %mdkversion >= 1000
Conflicts:	bash-completion < 20031225
%endif

%description
The unrar program is used to uncompress .rar format archives, which were
somewhat popular on DOS based machines.

This package is in PLF for it's unclear license.
%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %name

%build
make -f makefile.unix CXXFLAGS="$RPM_OPT_FLAGS" STRIP=true

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 unrar $RPM_BUILD_ROOT%{_bindir}
%if %mdkversion >= 1000
install -d -m 755 %buildroot/%_sysconfdir/bash_completion.d
bzip2 -cd %SOURCE1 > %buildroot/%_sysconfdir/bash_completion.d/unrar
%endif

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc license.txt readme.txt
%if %mdkversion >= 1000
%config(noreplace) %_sysconfdir/bash_completion.d/unrar
%endif
%{_bindir}/unrar

