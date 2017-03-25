# Using strace fix apache 500 error and automate fix with puppet.
node default {
  include stdlib
  file_line { 'fix_php':
    path  => '/var/www/html/wp-settings.php',
    line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
    match => '^require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );.*$'
  }

  service { 'apache2':
    ensure => 'running',
    enable => true
  }
}
