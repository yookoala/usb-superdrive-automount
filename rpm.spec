Name:           rpm
Version:        1.0
Release:        1%{?dist}
Summary:        Simple udev rule to automount an Apple USB SuperDrive.

License:        MIT
URL:            https://github.com/yookoala/usb-superdrive-automount
Source0:        https://github.com/yookoala/usb-superdrive-automount

%global rulename 81-usb-superdrive.rules

Requires: sg3_utils

%description
Provide udev rule to automatically bootstrap an Apple USB SuperDrive for use.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%doc https://github.com/yookoala/usb-superdrive-automount



%changelog
* Mon Jan 16 2023 Koala Yeung <koalay@gmail.com>
  - Created the package
