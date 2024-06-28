#!/usr/bin/perl

# Detect the operating system
my $os;
if ($^O eq 'MSWin32') {
    $os = 'Windows';
} elsif ($^O eq 'linux') {
    $os = 'Linux';
} elsif ($^O eq 'darwin') {
    $os = 'macOS';
} else {
    $os = 'Unknown';
}

# Print the detected operating system
print "Running on $os\n";

# Perform OS-specific tasks
if ($os eq 'Windows') {
    # Windows-specific code goes here
    print "Performing Windows-specific tasks...\n";
} elsif ($os eq 'Linux') {
    # Linux-specific code goes here
    print "Performing Linux-specific tasks...\n";
} elsif ($os eq 'macOS') {
    # macOS-specific code goes here
    print "Performing macOS-specific tasks...\n";
} else {
    print "Unable to perform OS-specific tasks for unknown operating system.\n";
}
