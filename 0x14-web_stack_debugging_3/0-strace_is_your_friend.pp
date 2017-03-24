# Using strace fix apache 500 error and automate fix with puppet.
file_line { 'fix_php':
  path  => '/var/www/html/wp-settings.php',
  line  => '/var/www/html/wp-includes/class-wp-locale.php',
  match => '^/var/www/html/wp-includes/class-wp-locale.phpp.*$'
}
