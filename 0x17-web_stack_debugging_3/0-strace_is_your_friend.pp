# debug and then automate it using Puppet
exec { 'fix_wp':
	provider => 'shell',
	command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/'
}
