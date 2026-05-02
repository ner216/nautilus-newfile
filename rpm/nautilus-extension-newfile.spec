Name: nautilus-extension-newfile
Version: 1.0.0
Release: 1%{?dist}
Summary: Add new file option to Nautilus right-click menu
License: Proprietary
BuildArch: noarch

Source0: nautilus-newfile.py
Source1: new-file-dialog.ui

Requires: nautilus-python

%description
Add new file option to the right-click menu in the Nautilus file manager.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datarootdir}/nautilus-python/extensions/
install -m 644 %{_sourcedir}/new-file-dialog.ui $RPM_BUILD_ROOT/%{_datarootdir}/nautilus-python/extensions/
install -m 644 %{_sourcedir}/nautilus-newfile.py $RPM_BUILD_ROOT/%{_datarootdir}/nautilus-python/extensions/

%files
%{_datarootdir}/nautilus-python/extensions/new-file-dialog.ui
%{_datarootdir}/nautilus-python/extensions/nautilus-newfile.py

%changelog
* Sat May 2 2026 Nolan Pro <email@email.com>
- First RPM version

