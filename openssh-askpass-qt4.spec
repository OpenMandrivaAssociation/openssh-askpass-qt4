%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Name: openssh-askpass-qt4
Version: 1.0.1
Release: 6
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



%changelog
* Fri Jun 01 2012 Crispin Boylan <crisb@mandriva.org> 1.0.1-5
+ Revision: 801893
- Rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2010.0
+ Revision: 430215
- rebuild

* Tue Aug 05 2008 Funda Wang <fwang@mandriva.org> 1.0.1-2mdv2009.0
+ Revision: 263989
- rebuild for new compile flags

* Thu May 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1.0.1-1mdv2009.0
+ Revision: 213103
- Minor update to center window and provide modal behavior

* Tue May 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1.0-1mdv2009.0
+ Revision: 211485
- First qt4 based ssh askpass dialog
- New ssh ask dialog for qt4

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 03 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.2-3mdv2008.1
+ Revision: 114491
- added a patch to fix askpass exit status, which must be >0 when the user cancels
- little more clear summary and description
- fixed qmake call in build

* Fri Aug 24 2007 Helio Chissini de Castro <helio@mandriva.com> 0.2-2mdv2008.0
+ Revision: 70892
- Rebuild to 2008.0

