# Using strace fix apache 500 error and automate fix with puppet.
file { 'fix_php':
  path    => './tmp.txt',
  line    => '/var/www/html/wp-includes/class-wp-locale.php',
  match   => '^/var/www/html/wp-includes/class-wp-locale.phpp'
}
