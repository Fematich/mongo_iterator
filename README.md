mongo_iterator
==============

A more performant way to iterate over a big (unindexed) MongoDB database


operation
==========
based on the timestamp integrated in the standard _id* we split the data in different batches (1 batch per day)
- all these batches are put in a queue
- these batches are handled by different python-workers in parallel (you need to set the number of workers by MAX_PROCESSES)


caveat
=========
currently only implementation to export a big set of tweets stored in a MongoDB database to different text-files

* http://www.kchodorow.com/blog/2011/12/20/querying-for-timestamps-using-objectids/
