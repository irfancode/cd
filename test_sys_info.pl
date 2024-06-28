#!/usr/bin/perl -w

use strict;
use Test::More;

# Mock the operating system variable
BEGIN {
    # Windows
    $ENV{^O} = 'MSWin32';
    require './sys_info.pl';
    is($os, 'Windows', 'Correctly detected Windows');

    # Linux
    $ENV{^O} = 'linux';
    require './sys_info.pl';
    is($os, 'Linux', 'Correctly detected Linux');

    # macOS
    $ENV{^O} = 'darwin';
    require './sys_info.pl';
    is($os, 'macOS', 'Correctly detected macOS');

    # Unknown
    $ENV{^O} = 'unknown';
    require './sys_info.pl';
    is($os, 'Unknown', 'Correctly detected Unknown');
}

done_testing;
