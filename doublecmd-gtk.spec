%global svn     3765

Name:		doublecmd-gtk
Summary:	Twin-panel (commander-style) file manager (GTK2)
Version:	0.5.5
Release:	svn%{svn}.1%{?dist}.R
URL:		http://doublecmd.sourceforge.net
Source0:	doublecmd-svn%{svn}.tar.xz
License:	GPL
Group:		Applications/File
BuildRequires:	fpc >= 2.4.0 fpc-src glib2-devel gtk2-devel lazarus >= 0.9.29
BuildRequires:  gdk-pixbuf-devel ncurses-devel dbus-devel bzip2-devel xorg-x11-proto-devel xorg-x11-xtrans-devel
 
Provides:  doublecmd
Obsoletes: doublecmd < 0.4.6 doublecmd-qt
BuildRoot:	%{_tmppath}/%{doublecmd}-%{version}-build

%description
Double Commander is a cross platform open source file manager with two panels side by side.
It is inspired by Total Commander and features some new ideas.

%prep
%setup -q -n doublecmd

%build
./build.sh all gtk2

%install
install/linux/install.sh --install-prefix=%{buildroot}

%clean
[ %{buildroot} != "/" ] && ( rm -rf %{buildroot} )

%files
%defattr(-,root,root)
%{_libdir}/doublecmd
%{_bindir}/doublecmd
%{_datadir}/doublecmd
%{_datadir}/pixmaps/doublecmd.png
%{_datadir}/applications/doublecmd.desktop

%changelog
* Thu Jul  28 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-avn3765.1.R
- Initial build for Fedora

* Fri Jun 11 2010 - Alexander Koblov <Alexx2000@mail.ru>
- Initial package, version 0.4.6
