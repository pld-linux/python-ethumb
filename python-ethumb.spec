Summary:	Python bindings for Ethumb library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ethumb
Name:		python-ethumb
Version:	0.7.3
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	d5739237396d5cec434d5b4a9f39ce80
Patch0:		%{name}-update.patch
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	ethumb-devel >= 0.1.1
BuildRequires:	epydoc
BuildRequires:	python-Cython >= 0.13
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	ethumb-libs >= 0.1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Ethumb library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki Ethumb.

%package devel
Summary:	Python bindings for Ethumb library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Ethumb - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ethumb-devel >= 0.1.0

%description devel
Python bindings for Ethumb library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Ethumb - pliki programistyczne.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/ethumb/*.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitedir}/ethumb
%attr(755,root,root) %{py_sitedir}/ethumb/c_ethumb.so
%attr(755,root,root) %{py_sitedir}/ethumb/client.so
%{py_sitescriptdir}/ethumb
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/python-ethumb.pc
%{_pkgconfigdir}/python-ethumb_client.pc
