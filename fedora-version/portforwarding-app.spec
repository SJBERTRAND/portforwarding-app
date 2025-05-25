Name:           portforwarding-app
Version:        1.1
Release:        %autorelease
Summary:        PortForwarding App
Source:         %{name}-%{version}.tar.gz
License:        Open
BuildArch:      noarch
Requires:       openssh sshpass

%description
PortFrowading App written in python. Using GTK 4, ssh & sshpass


%prep
%autosetup

%install
install -D -m 0644 portforwarding_app.desktop %{buildroot}/usr/share/applications/portforwarding_app.desktop
install -D -m 0755 portforwarding_app %{buildroot}/usr/bin/portforwarding_app
install -D -m 0644 portforwarding-app-256x256.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/portforwarding-app.png
install -D -m 0644 portforwarding-app-48x48.png %{buildroot}/usr/share/icons/hicolor/48x48/apps/portforwarding-app.png
install -D -m 0644 gschemas.compiled %{buildroot}/usr/share/portforwarding_app/data/gschemas.compiled
install -D -m 0644 org.portforwarding_app.local.gschema.xml %{buildroot}/usr/share/portforwarding_app/data/org.portforwarding_app.local.gschema.xml

%files
/usr/share/applications/portforwarding_app.desktop
/usr/share/icons/hicolor/256x256/apps/portforwarding-app.png
/usr/share/icons/hicolor/48x48/apps/portforwarding-app.png
/usr/bin/portforwarding_app
/usr/share/portforwarding_app/data/gschemas.compiled
/usr/share/portforwarding_app/data/org.portforwarding_app.local.gschema.xml

%changelog
%autochangelog
