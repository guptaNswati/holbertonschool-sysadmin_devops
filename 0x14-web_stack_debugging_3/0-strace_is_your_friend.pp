# Using strace fix apache 500 error and automate fix with puppet.
exec { 'fix_php':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/bin/sed'
}

service { 'apache2':
  restart => true
}
