Name:           poco
Version:        1.11.1
Release:        1
Summary:        C++ Framework for Network-based Applications
License:        BSL-1.0
Group:          System/Libraries
URL:            https://pocoproject.org
Source:         https://github.com/pocoproject/%{name}/archive/%{name}-%{name}-%{version}-release.tar.gz
BuildRequires:  cmake 
BuildRequires:  fdupes
BuildRequires:  mysql-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

%description
C++ class libraries and frameworks for building network- and Internet-based applications.
    
%prep
%autosetup -n poco-poco-%{version}-release -p1

%build
%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="" \
    -DENABLE_CPPPARSER=ON \
    -DENABLE_CRYPTO=ON \
    -DENABLE_DATA=ON \
    -DENABLE_DATA_MYSQL=ON \
    -DENABLE_DATA_ODBC=ON \
    -DENABLE_DATA_SQLITE=ON \
    -DENABLE_JSON=ON \
    -DENABLE_MONGODB=ON \
    -DENABLE_NET=ON \
    -DENABLE_NETSSL=ON \
    -DENABLE_NETSSL_WIN=OFF \
    -DENABLE_PAGECOMPILER=ON \
    -DENABLE_PAGECOMPILER_FILE2PAGE=ON \
    -DENABLE_PDF=ON \
    -DENABLE_UTIL=ON \
    -DENABLE_XML=ON \
    -DENABLE_ZIP=ON \
    -DFORCE_OPENSSL=ON \
    -DPOCO_UNBUNDLED=ON
%make_build

%install
%make_install -C build
rm -rf %{buildroot}%{_libdir}/cmake/Poco/V*
%fdupes -s %{buildroot}/%{_libdir}/cmake/Poco

%files -
