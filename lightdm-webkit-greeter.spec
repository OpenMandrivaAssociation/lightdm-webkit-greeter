Summary:	LightDM Webkit Greeter
Name:		lightdm-webkit-greeter
Version:	0.1.2
Release:	1
Group:		System/X11
License:	GPLv3
URL:		https://launchpad.net/lightdm-webkit-greeter
Source0:	https://launchpad.net/lightdm-webkit-greeter/+download/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(liblightdm-gobject-1)
BuildRequires:	pkgconfig(webkit-1.0)

Provides: lightdm-greeter

%description
A LightDM greeter that uses the Webkit 1.0.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS='-ljavascriptcoregtk-1.0'

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%config(noreplace) %{_sysconfdir}/lightdm/lightdm-webkit-greeter.conf
%{_bindir}/lightdm-webkit-greeter
%{_datadir}/lightdm-webkit
%{_datadir}/xgreeters/lightdm-webkit-greeter.desktop

