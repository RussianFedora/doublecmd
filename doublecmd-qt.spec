%global debug_package %{nil}
%global realname doublecmd

Name:           doublecmd-qt
Version:        0.6.5
Release:        1%{?dist}
Summary:        Cross platform open source file manager with two panels

License:        GPLv2
URL:            http://doublecmd.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{realname}/%{realname}-%{version}-src.tar.gz

BuildRequires:  qt4pas-devel
BuildRequires:  lazarus >= 1.0.0
BuildRequires:  fpc >= 2.6.0
BuildRequires:  fpc-src
BuildRequires:  bzip2-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils

Provides:       %{realname} = %{version}
Conflicts:      %{realname}-gtk

%description
Double Commander is a cross platform open source file manager with two panels
side by side.
It is inspired by Total Commander and features some new ideas.
Qt version.


%prep
%setup -q -n %{realname}-%{version}

%build
./build.sh beta qt

%install
install/linux/install.sh --install-prefix=%{buildroot}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{realname}.desktop

%files
%doc doc/changelog.txt  doc/README.RUS.txt  doc/README.txt
%license doc/COPYING.LGPL.txt  doc/COPYING.modifiedLGPL.txt  doc/COPYING.txt
%{_libdir}/%{realname}
%{_bindir}/%{realname}
%{_datadir}/%{realname}
%{_datadir}/pixmaps/%{realname}.*
%exclude %{_datadir}/%{realname}/doc/
%{_datadir}/applications/%{realname}.desktop
%{_mandir}/man1/%{realname}.1.gz

%changelog
* Fri Oct 09 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.5-1
- Update to 0.6.5

* Tue Feb 10 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.0-1
- Update to 0.6.0

* Tue Aug 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3860.1.R
- Update to new revision

* Wed Aug 10 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3796.1.R
- Removed .svn files
- Update svn to 3796

* Sat Jul 30 2011 Alexei Panov <elemc AT atisserv DOT ru> - 0.5.5-1
- Initial build with active support of sergem from fedora@c.j.r
