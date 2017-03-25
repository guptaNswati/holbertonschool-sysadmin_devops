# Using strace fix apache 500 error and automate fix with puppet.
exec { 'fix_php':
  command => "sed -ie 's/locale.phpp/locale.php/' /var/www/html/wp-settings.php",
  path    => ['/bin']
}
