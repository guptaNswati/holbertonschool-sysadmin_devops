# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'killmenow':
  command => 'pkill -f killmenow',
  path    => '/sbin:/usr/sbin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin',
}
