Name:		unrar
Version:	5.9.2
Release:	1
Epoch:		1
Summary:	Decompressor for .rar format archives
Source0: 	http://www.rarlab.com/rar/%{name}src-%{version}.tar.gz
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
# build main binary
make -f makefile CXXFLAGS="%{optflags} -fPIC" CC=%{__cc} CXX=%{__cxx} LDFLAGS="%{ldflags} -pthread" STRIP=true unrar

# build dynamic library
make -f makefile CXXFLAGS="%{optflags} -fPIC" CC=%{__cc} CXX=%{__cxx} LDFLAGS="%{ldflags} -pthread" STRIP=true lib

%install
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 unrar %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_libdir}
install -m 755 libunrar.so %{buildroot}%{_libdir}

%files
%doc license.txt readme.txt
%{_bindir}/unrar
%{_libdir}/libunrar.so
