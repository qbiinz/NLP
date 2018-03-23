PCFG implementation 

# Usage

cfgparse.pl is a perl script that parses sentences based on a set of non-terminal rules in grammar 
and a set of terminal rules in the lexicon

# example:

./cfgparse grammar2 lexicon < example.sen

cfggen.pl is a perl script that generates sentences bacsed on the sets of grammar and lexicon

# example:

./cfggen.pl --text &lt;N&gt; grammar1 lexicon
  
  --text is a flag for pretty printing the output
  
  &lt;N&gt; is the number of sentences to be generated
