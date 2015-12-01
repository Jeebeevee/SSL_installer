#!/usr/bin/python

import sys
import os
import subprocess

'''
script: ssl_install.py
owner: 
author: 
e-mail: 

    *                             |>>>                    +
+          *                      |                   *       +
                    |>>>      _  _|_  _   *     |>>>
           *        |        |;| |;| |;|        |                 *
     +          _  _|_  _    \\.    .  /    _  _|_  _       +
 *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|
               \\..      /    ||:+++. |    \\.    .  /           *
      +         \\.  ,  /     ||:+++  |     \\:  .  /
                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *
          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +
                 ||+++ ||.    .  SSL .     . ||+++.|   *
+   *            ||: . ||:.     . .   .  ,   ||:   |               *
         *       ||:   ||:  ,     +       .  ||: , |      +
  *              ||:   ||:.     +++++      . ||:   |         *
     +           ||:   ||.     +++++++  .    ||: . |    +
           +     ||: . ||: ,   +++++++ .  .  ||:   |             +
                 ||: . ||: ,   +++++++ .  .  ||:   |        *
                 ||: . ||: ,   +++++++ .  .  ||:   |

'''

SSL_dir = '/etc/apache2/ssl/'

# make private key and csr
def keyGen(domain, CLinput=''):
  if len(CLinput) > 2 and len(CLinput) <= 6:
    print(CLinput)
  else:
    owner = raw_input('Owner: ')
    location = raw_input('Location: ')
    state = raw_input('State: ')
    country = raw_input('Country [NL]: ')
    if not country:
      country = 'NL'

    if not owner or not location or not country:
      print('Owner, Location or State is/are empty.\nStart again.')
      quit()
    

# main function
def main():

  if not os.path.isdir(SSL_dir):
    print('\nERROR: Directory "' + SSL_dir + '" don\'t exist.\n' )
    quit()

  if len(sys.argv) > 1 :
    # expressions in command line
    domain = sys.argv[1] # domain as first variable
  else:
    # no expressions in command line, give menu
    print('== SSL installer ==')
    domain = raw_input('Domain: ')
  
  if not domain:
    print('ERROR: No domain available.')
    quit()
  else:
    if not os.path.isdir(SSL_dir + domain):
      print('make ssl folder for the domain ' + domain + '.\n')
      os.mkdir(SSL_dir + domain, 0664)

  if not os.path.exists(SSL_dir + domain +'/'+ domain +'.key') and not os.path.exists(SSL_dir + domain +'/'+ domain +'.csr'):
    # make private key and csr
    print('make private key and csr.\n')
    keyGen(domain, sys.argv)
  else:
    # private key and csr exist. go ahead with installing public key
    print('installing public key.\n')


main()

