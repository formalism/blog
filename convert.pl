#!/usr/bin/perl

use strict;

sub convert{
    my ($src, $dest) = @_;
    my ($dash);

    $dash = 0;
    open(SRC, $src) or die "$!";
    open(D, ">$dest") or die "$!";
    while (<SRC>){
	if ($_ =~ '^---$'){
	    $dash = $dash + 1;
	    if ($dash == 2){
		if ($dest =~ /.*\/(.*)\.md/){
		    print D "Slug: $1\n";
		}
	    }
	}elsif ($_ =~ '^title:(.*)'){
	    print D "Title:$1\n";
	}elsif ($_ =~ '^published: (\d+)-(\d+)-(\d+)T([^Z]+)Z$'){
	    print D "Date: $1-$2-$3 $4\n";
	}elsif ($_ =~ '^categories: (.*)'){
	    print D "Category: $1\n";
	}elsif ($_ =~ '^tags: (.*)'){
	    print D "Tags: $1\n";
	}else{
	    print D $_;
	}
    }
    close(SRC);
    close(D);
}

sub recurse{
    my ($dir) = @_;
    my (@fileLists, $fileName);
    my ($target,$newdir);

    @fileLists = glob($dir.'/*');
    foreach $fileName (sort(@fileLists)){
	if (-d $fileName){
	    $newdir = $fileName;
	    $newdir =~ s/blog\/posts/blogs\/content/i;
	    system "mkdir $newdir";
	    &recurse($fileName);
	}elsif (-f $fileName){
#	    print $fileName."\n";
	    $target = $fileName;
	    $target =~ s/blog\/posts/blogs\/content/i;
	    $target =~ s/html$/md/i;
	    print $target."\n";
	    convert($fileName, $target);
	}
    }
}

recurse('/home/tomo/blog/posts');
