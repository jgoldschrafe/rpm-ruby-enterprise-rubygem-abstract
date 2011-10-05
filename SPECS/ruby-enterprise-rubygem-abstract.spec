%define _prefix /opt/ruby-enterprise
%define _gem %{_prefix}/bin/gem
%define _ruby %{_prefix}/bin/ruby
%define ruby_dist ruby-enterprise
%define ruby_dist_dash %{ruby_dist}-

# Generated from abstract-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(%{_ruby} -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(%{_ruby} -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname abstract
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: a library which enable you to define abstract method in Ruby
Name: %{?ruby_dist_dash}rubygem-%{gemname}
Version: 1.0.0
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rubyforge.org/projects/abstract
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: %{?ruby_dist_dash}rubygems
BuildRequires: %{?ruby_dist_dash}rubygems
BuildArch: noarch
Provides: %{?ruby_dist_dash}rubygem(%{gemname}) = %{version}

%description
'abstract.rb' is a library which enable you to define abstract method in Ruby.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
%{_gem} install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct  3 2011 Jeff Goldschrafe <jeff@holyhandgrenade.org> - 1.0.0-1.hhg
- Rebuild for Ruby Enterprise Edition

* Sun Dec 19 2010 Sergio Rubio <rubiojr@frameos.org> - 1.0.0-1
- Initial package
