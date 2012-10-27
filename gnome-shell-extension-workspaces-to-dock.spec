%define		extname		workspaces-to-dock
Summary:	Transform the workspaces of the overview mode into an intellihide dock
Name:		gnome-shell-extension-%{extname}
Version:	20121027
Release:	1
Group:		X11/Applications
# parts of code comes from gnome-shell-extensions which is GPLv2, assume GPL virality
# as there is no information about license
License:	GPLv2
URL:		https://extensions.gnome.org/extension/427/workspaces-to-dock/
# $ git clone git://github.com/passingthru67/workspaces-to-dock.git
# $ cd workspaces-to-dock/
# $ git archive --format=tar --prefix=%{name}-%{version}/ master | xz > ../%{name}-%{version}.tar.xz
Source0:	%{extname}-%{version}.tar.xz
# Source0-md5:	233e9924159d3fc29d375a4f8c16f6af
Requires:	gnome-shell >= 3.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Gnome Shell extension that transforms the workspaces of the overview
mode into an intellihide dock.  The dock is positioned and sized to
maintain tight integration with the Gnome Shell.

%prep
%setup -q -n %{extname}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas \
	$RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/workspaces-to-dock@passingthru67.gmail.com

install schemas/org.gnome.shell.extensions.workspaces-to-dock.gschema.xml $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/
install *.js* $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/workspaces-to-dock@passingthru67.gmail.com/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.workspaces-to-dock.gschema.xml
%{_datadir}/gnome-shell/extensions/workspaces-to-dock*
