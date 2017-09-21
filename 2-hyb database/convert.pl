#!/bin/perl
use warnings;
use strict;
use Bio::Perl;

my $db = new Bio::DB::RefSeq;

open(F,"<$ARGV[0]") or die $!;

while(<F>){
	chomp;
	my $refseq = $_;

	my $seq = get_sequence('refseq',$refseq);

# most of the time RefSeq_ID eq RefSeq acc
#my $seq = $db->get_Seq_by_id($refseq); # RefSeq ID
#print "accession is ", $seq->accession_number, "\n";

	if ($seq->desc =~ /\((\w+)\)/) {
	    print"$1\n";
	}

}
