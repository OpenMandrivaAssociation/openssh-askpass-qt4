Name: openssh-askpass-qt4
Version: 1.0.1
Release: 5
Summary: Qt4 passphrase dialog for OpenSSH
License: GPL
Group: Graphical desktop/KDE
BuildRequires: qt4-devel
URL: http://www.mandriva.com/
Source: %name-%version.tar.bz2
Buildroot: %_tmppath/%name-buildroot
Requires: openssh-askpass-common
Provides: openssh-askpass
Provides: ssh-askpass
Provides: ssh-extras

%description
Qt4 version of ssh passphrase dialog.

%files 
%defattr(0755,root,root,755)
%_libdir/ssh/qt4-ssh-askpass

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%qmake_qt4 qt4-ssh-askpass.pro

%make

%install
mkdir -p %buildroot/%_sysconfdir/profile.d/
mkdir -p %buildroot/%_libdir/ssh
install -m 755 qt4-ssh-askpass %buildroot/%_libdir/ssh/qt4-ssh-askpass

%post
update-alternatives --install %_libdir/ssh/ssh-askpass ssh-askpass %_libdir/ssh/qt4-ssh-askpass 50
update-alternatives --install %_bindir/ssh-askpass bssh-askpass %_libdir/ssh/qt4-ssh-askpass 50

%postun
[ $1 = 0 ] || exit 0
update-alternatives --remove ssh-askpass %_libdir/ssh/qt4-ssh-askpass
update-alternatives --remove bssh-askpass %_libdir/ssh/qt4-ssh-askpass

%clean
rm -rf %buildroot

