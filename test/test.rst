>>> from IPy import IP
>>> IP('::ffff:1.2.3.4').strCompressed()
'::ffff:1.2.3.4'
>>> IP('::ffff:192.168.10.0/120').strCompressed()
'::ffff:192.168.10.0/120'
>>> IP('::ffff:192.168.10.42/120', make_net=True).strCompressed()
'::ffff:192.168.10.0/120'
>>> IP('::/0', make_net=True).net()
IP('::')

