# FIXME build failure with LTO, last verified with 6.2.12-1, clang 17.0.3
#define _disable_lto 1

Name:		unrar
Version:	7.0.5
Release:	1
Epoch:		1
Summary:	Decompressor for .rar format archives
Source0: 	http://www.rarlab.com/rar/%{name}src-%{version}.tar.gz
Patch0:		unrar-linkfix.patch
Url:		http://www.rarlab.com/rar_add.htm
License:	Freeware
Group:		Archiving/Compression
Conflicts:	bash-completion < 20031225

%description
The unrar program is used to uncompress .rar format archives, which were
somewhat popular on DOS based machines.

%prep
%autosetup -p1 -n %{name}

%build
# build main binary
make -f makefile CXXFLAGS="%{optflags} -fPIC" CC=%{__cc} CXX=%{__cxx} LDFLAGS="%{ldflags} -pthread" STRIP=true unrar
mv unrar unrar.bin

# build dynamic library
make -f makefile CXXFLAGS="%{optflags} -fPIC" CC=%{__cc} CXX=%{__cxx} LDFLAGS="%{ldflags} -pthread" STRIP=true lib


%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 unrar.bin %{buildroot}%{_bindir}/unrar

install -d -m 755 %{buildroot}%{_libdir}
install -m 755 libunrar.so %{buildroot}%{_libdir}

%files
%doc license.txt readme.txt
%{_bindir}/unrar
%{_libdir}/libunrar.so
