# CC

CC is a command line program written in Python using the cryptocompare API.
Check crypto prices and check conversion values right from the terminal.

## Installation

The easiest way to accomplish this is via git. It can be installed here: [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Access your command line. On Windows this can be the 'Command Prompt' or 'Powershell'. On Mac it is the 'Terminal' (I think?). On Linux, I trust you know what it is.
```
$> git clone https://github.com/MaciejKrzysiak/cc.git
$> cd cc/
$> <See Usage>
```

At this stage, you can use cc. For convenience, I'd add an alias so that you don't need to type 'python3 /path/to/cc/cc.py ....'.
Learn about aliasing here [Aliasize](https://linuxize.com/post/how-to-create-bash-aliases/).

## Usage
```
$> python3 cc.py -s BTC -a 1337 -d NANO
$> 1337 BTC converted to NANO is valued at 13721270.01 NANO

$> python3 cc.py -s NANO -a 420 -d USD
$> 420 NANO converted to USD is valued at 2425.5 USD

$> python3 cc.py -h
$> cc.py -s <source> -a <amount> -d <destination> -h <help> -l <list>
$> Example Usage: python3 cc.py -s BTC -a 1.01 -d USD
A sample of supported currencies are listed below.
To see them all, use the -l or --list flag.
[NANO, XMR, BTC, ETH, XRP, USD, GBP]
```
