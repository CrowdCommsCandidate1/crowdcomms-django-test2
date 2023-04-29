Notes from Tamas
================

Unfortunately I ran out of time as I ended up going down the _rabbit hole_ with the geo lookups.

The distance function seems to work fine, however for some reason there's a delta between the numbers in the test files and the numbers I got in the 1st decimal place (> 100 meters).

I also did not have time time to implement the direction check as the Azimuth function I wanted to use is not supported by SpatiaLite.

There's an analytics test failing as well, I was going to figure that out once I completed all other tasks, but I ran out of time (the data looks fine, could the test case itself be wrong?).

Regarding the speeding up test, I should be able to optimise down to 2 queries:
1. Permission checks (and cache user object at this point)
2. Update RabbitHole.objects queryset to raise Http404 after the annotation
