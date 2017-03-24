# Using Puppet, install puppet-lint.
package { 'puppet-lint':
  ensure          => installed,
  install_options => ['version-2.1.1'],
  provider        => gem
}
