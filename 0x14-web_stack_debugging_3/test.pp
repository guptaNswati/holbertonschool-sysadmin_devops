# Using strace fix apache 500 error and automate fix with puppet.
file { './test1.txt':
  ensure => file,
  path   => './test1.txt',
  changes   => '/var/www/html/wp-includes/class-wp-locale.php',
  match  => '^/var/www/html/wp-includes/class-wp-locale.phpp.*$'
}
